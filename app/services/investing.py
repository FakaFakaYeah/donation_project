from datetime import datetime
from typing import Union, List

from sqlalchemy import select, false
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.charity_project import CharityProject
from app.models.donation import Donation


async def close_obj(
        obj: Union[Donation, CharityProject]
) -> None:
    obj.close_date = datetime.now()
    obj.fully_invested = True


async def get_all_open(
        model: Union[Donation, CharityProject],
        session: AsyncSession
) -> List[Union[Donation, CharityProject]]:
    objs = await session.scalars(
        select(model).where(
            model.fully_invested == false()
        ).order_by(model.create_date)
    )
    return objs.all()


async def investing(
        obj: Union[Donation, CharityProject],
        model,
        session: AsyncSession
) -> None:
    open_objs = await get_all_open(model=model, session=session)
    if open_objs:
        can_invest = obj.full_amount
        for open_obj in open_objs:
            can_obj_invest = open_obj.full_amount - open_obj.invested_amount
            invest = min(can_invest, can_obj_invest)
            open_obj.invested_amount += invest
            obj.invested_amount += invest
            can_invest -= invest

            if open_obj.full_amount == open_obj.invested_amount:
                await close_obj(open_obj)

            if not can_invest:
                await close_obj(obj)
                break
        await session.commit()
        await session.refresh(obj)
