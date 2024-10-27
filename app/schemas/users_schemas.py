from uuid import UUID
from pydantic import BaseModel, EmailStr


class UserCreateSchema(BaseModel):
    name: str
    email: EmailStr
    password: str
    address: str


class UserUpdateSchema(BaseModel):
    name: str
    email: EmailStr
    password: str
    address: str


class UserResponseSchema(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    address: str

    class Config:
        from_attributes = True