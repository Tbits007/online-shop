from uuid import UUID
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.orders import Orders
from app.repositories.orders_repo import OrdersRepository
from app.schemas.orders_schemas import (
    OrderCreateSchema,
    OrderUpdateSchema,
    StatusChoice,
)


class OrderService:
    def __init__(self, session: AsyncSession):
        self.order_repo = OrdersRepository(session)

    async def get_all_orders(self) -> list[Orders]:
        return await self.order_repo.get_all()

    async def get_order_by_id(self, order_id: UUID) -> Orders | None:
        order = await self.order_repo.get_by_id(order_id)
        if order is None:
            raise HTTPException(status_code=500)
        return order

    async def create_order(self, data: OrderCreateSchema) -> Orders:
        order = Orders(
            user_id=data.user_id,
            status=data.status,
            product_id=data.product_id,
            total_price=data.total_price,
        )
        return await self.order_repo.create(order)

    async def update_order(
        self, order_id: UUID, updated_data: OrderUpdateSchema
    ) -> Orders:
        order = await self.get_order_by_id(order_id)
        return await self.order_repo.update(order_id, updated_data.model_dump())

    async def delete_order(self, order_id: UUID) -> None:
        order = await self.get_order_by_id(order_id)
        await self.order_repo.delete(order_id)

    async def get_orders_by_status(self, status: StatusChoice) -> list[Orders]:
        return await self.order_repo.get_orders_by_status(status)
