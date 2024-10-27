from pydantic import BaseModel
from uuid import UUID
from enum import Enum
from datetime import datetime


class Status(str, Enum):
    shipped = "shipped"
    delivered = "delivered"
    pending = "pending"


class OrderCreateSchema(BaseModel):
    pass


class OrderResponseSchema(BaseModel):
    id: UUID
    user_id: UUID
    status: Status
    product_id: UUID
    total_price: float
    created_at: datetime

    class Config:
        from_attributes = True