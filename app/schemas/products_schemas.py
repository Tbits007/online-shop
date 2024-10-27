from typing import Optional
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
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    currency: Optional[str] = None
    stock: Optional[int] = None
    category_id: Optional[UUID] = None
    
    
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