from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import current_user, current_superuser, get_async_session
from app.crud import donation_crud, charity_project_crud
from app.models import User
from app.schemas import DonationDB, DonationCreate, DonationUser
from app.services import investing

router = APIRouter()


@router.get(
    '/',
    summary='Получения списка всех пожертвований',
    response_model=List[DonationDB],
    dependencies=[Depends(current_superuser)],
    response_model_exclude_none=True
)
async def get_all_donation(
        session: AsyncSession = Depends(get_async_session)
) -> List[DonationDB]:

    donations = await donation_crud.get_all(session=session)
    return donations


@router.post(
    '/',
    summary='Создание пожертвования',
    response_model=DonationUser,
    response_model_exclude_none=True
)
async def create_donation(
    donation: DonationCreate,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session),
) -> DonationUser:
    """
    Создание пожертвования

    - **full_amount**: сумма пожертвования
    - **comment**: комментарий к пожертвованию (опционально)
    """
    donation = await donation_crud.create(
        obj_in=donation, session=session, user=user
    )
    sources = await charity_project_crud.get_all_open(session)
    if sources:
        investing(target=donation, sources=sources)
    await session.commit()
    await session.refresh(donation)
    return donation


@router.get(
    '/my',
    summary='Получить список личных пожертвований',
    response_model=List[DonationUser],
    response_model_exclude_none=True
)
async def get_user_donations(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session),
) -> List[DonationUser]:

    donations = await donation_crud.get_by_user_id(
        user=user, session=session
    )
    return donations
