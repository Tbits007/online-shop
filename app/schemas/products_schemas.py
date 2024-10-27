from pydantic import BaseModel
from uuid import UUID
from decimal import Decimal


class ProductResponseSchema(BaseModel):
    id: UUID
    name: str
    description: str
    price: Decimal
    currency: str
    stock: int
    category_id: UUID