from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.user import current_user, current_superuser, get_async_session
from app.crud.donation import donation_crud
from app.models.user import User
from app.models.charity_project import CharityProject
from app.schemas.donation import DonationDB, DonationCreate, DonationUser
from app.services.investing import investing

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
    await investing(donation, CharityProject, session)
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

    donations = await donation_crud.get_user_donations(
        user=user, session=session
    )
    return donations
