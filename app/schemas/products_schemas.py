from pydantic import BaseModel
from uuid import UUID
from decimal import Decimal


class ProductCreateSchema(BaseModel):
    name: str
    description: str
    price: float
    currency: str
    stock: int
    category_id: UUID


class ProductUpdateSchema(BaseModel):
    name: str
    description: str
    price: float
    currency: str
    stock: int
    category_id: UUID


class ProductResponseSchema(BaseModel):
    id: UUID
    name: str
    description: str
    price: Decimal
    currency: str
    stock: int
    category_id: UUID

    class Config:
        from_attributes = True