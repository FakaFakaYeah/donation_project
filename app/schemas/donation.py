from datetime import datetime
from typing import Optional

from pydantic import BaseModel, PositiveInt, Field, Extra

from app.core.config import EXAMPLE_AMOUNT


class DonationBase(BaseModel):

    full_amount: PositiveInt = Field(example=EXAMPLE_AMOUNT)
    comment: Optional[str] = Field(example='Котикам на корм')


class DonationCreate(DonationBase):

    class Config:
        extra = Extra.forbid


class DonationUser(DonationBase):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationDB(DonationUser):

    user_id: int
    invested_amount: int = Field(example=EXAMPLE_AMOUNT)
    fully_invested: bool
    close_date: Optional[datetime]
