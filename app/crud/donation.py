from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User, Donation
from app.schemas import DonationDB
from .base import CRUDBase


class CrudDonation(CRUDBase):

    @staticmethod
    async def get_user_donations(
            user: User,
            session: AsyncSession
    ) -> List[DonationDB]:
        donations = await session.scalars(
            select(Donation).where(Donation.user_id == user.id)
        )
        return donations.all()


donation_crud = CrudDonation(Donation)
