from pydantic import BaseModel
from uuid import UUID
from enum import Enum
from datetime import datetime


class StatusChoice(str, Enum):
    shipped = "shipped"
    delivered = "delivered"
    pending = "pending"


class OrderCreateSchema(BaseModel):
    user_id: UUID
    status: StatusChoice
    product_id: UUID
    total_price: float


class OrderUpdateSchema(BaseModel):
    user_id: UUID
    status: StatusChoice
    product_id: UUID
    total_price: float


class OrderResponseSchema(BaseModel):
    id: UUID
    user_id: UUID
    status: StatusChoice
    product_id: UUID
    total_price: float
    created_at: datetime

    class Config:
        from_attributes = True