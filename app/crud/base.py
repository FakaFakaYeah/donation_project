from typing import Optional, Union, List

from sqlalchemy import select, update, false
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User, CharityProject, Donation
from app.schemas import DonationDB


class CRUDBase:

    def __init__(self, model):
        self.__model = model

    async def get_by_attribute(
            self,
            session: AsyncSession,
            **param
    ):
        obj = await session.scalars(select(self.__model).filter_by(**param))
        return obj.first()

    async def get_all(
            self,
            session: AsyncSession
    ):
        objs = await session.scalars(select(self.__model))
        return objs.all()

    async def create(
            self,
            obj_in,
            session: AsyncSession,
            user: Optional[User] = None
    ):
        obj_in_data = obj_in.dict()
        if user:
            obj_in_data['user_id'] = user.id
        obj = self.__model(**obj_in_data)
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj

    async def update(
            self,
            obj,
            obj_in,
            session: AsyncSession,
    ):
        update_data = obj_in.dict(exclude_unset=True)
        await session.execute(
            update(self.__model).filter_by(id=obj.id).values(**update_data)
        )
        await session.commit()
        await session.refresh(obj)
        return obj

    @staticmethod
    async def remove(
            obj,
            session: AsyncSession
    ):
        await session.delete(obj)
        await session.commit()
        return obj

    async def get_all_open(
            self,
            session: AsyncSession
    ) -> List[Union[Donation, CharityProject]]:
        objs = await session.scalars(
            select(self.__model).where(
                self.__model.fully_invested == false()
            ).order_by(self.__model.create_date)
        )
        return objs.all()

    async def get_by_user_id(
            self,
            user: User,
            session: AsyncSession
    ) -> List[DonationDB]:
        donations = await session.scalars(
            select(self.__model).where(self.__model.user_id == user.id)
        )
        return donations.all()
