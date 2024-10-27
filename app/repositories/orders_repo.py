from typing import Type

from sqlalchemy import select
from app.domain.orders import Orders
from app.repositories.base_repo import BaseRepository
from app.schemas.orders_schemas import StatusChoice


class OrdersRepository(BaseRepository[Orders]):
    model: Type[Orders] = Orders


    async def get_orders_by_status(self, status: StatusChoice) -> list[Orders]:
        """
        Получить заказы по статусу ("shipped", "delivered", "pending").
        """
        query = select(Orders).filter(Orders.status == status)
        result = await self.session.execute(query)
        return result.scalars().all()