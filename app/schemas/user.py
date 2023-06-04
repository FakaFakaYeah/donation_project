from typing import Optional

from fastapi_users import schemas
from pydantic import Field, EmailStr


class UserRead(schemas.BaseUser[int]):
    pass


class UserCreate(schemas.BaseUserCreate):
    email: EmailStr = Field(example='Your email address')
    password: str = Field(example='Your password')


class UserUpdate(schemas.BaseUserUpdate):
    password: Optional[str] = Field(example='Your password')
    email: Optional[EmailStr] = Field(example='Your email address')
