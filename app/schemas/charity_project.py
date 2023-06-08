from datetime import datetime
from typing import Optional

from pydantic import BaseModel, PositiveInt, Field, Extra, validator

from app.core.config import (
    MIN_LENGTH, MAX_LENGTH, EXAMPLE_AMOUNT, REG_NAME
)


class CharityProjectBase(BaseModel):

    name: str = Field(
        min_length=MIN_LENGTH, max_length=MAX_LENGTH,
        regex=REG_NAME, example='Сбор на корм котикам'
    )
    description: str = Field(
        min_length=MIN_LENGTH, example='Пусть котики всегда буду сытыми'
    )
    full_amount: PositiveInt = Field(example=EXAMPLE_AMOUNT)


class CharityProjectCreate(CharityProjectBase):

    class Config:
        extra = Extra.forbid
        schema_extra = {
            'example': {
                'name': 'Сбор на корм котикам',
                'description': 'Пусть котики всегда буду сытыми',
                'full_amount': EXAMPLE_AMOUNT
            }
        }

    @validator('name', 'description')
    def check_string_not_space(cls, value: str):
        if not value or value.isspace():
            raise ValueError('Значение не может состоять только из пробелов!')
        return value


class CharityProjectUpdate(CharityProjectCreate):

    name: Optional[str] = Field(
        min_length=MIN_LENGTH, max_length=MAX_LENGTH,
        regex=REG_NAME,
    )
    description: Optional[str] = Field(min_length=MIN_LENGTH)
    full_amount: Optional[PositiveInt]


class CharityProjectDB(CharityProjectBase):

    id: int
    invested_amount: int = Field(example=EXAMPLE_AMOUNT)
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
