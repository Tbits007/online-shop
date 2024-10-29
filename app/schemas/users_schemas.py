from typing import Union
from uuid import UUID
from pydantic import BaseModel, EmailStr


class UserCreateSchema(BaseModel):
    email: EmailStr
    password: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


class UserUpdateSchema(BaseModel):
    email: EmailStr
    password: str
    is_active: Union[bool, None] = None
    is_superuser: Union[bool, None] = None
    is_verified: Union[bool, None] = None


class UserResponseSchema(BaseModel):
    id: UUID
    email: EmailStr
    is_active: bool
    is_superuser: bool
    is_verified: bool

    class Config:
        from_attributes = True