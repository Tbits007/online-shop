from typing import Type
from uuid import UUID
from sqlalchemy import select
from app.domain.orders import Orders
from app.domain.products import Products
from app.repositories.base_repo import BaseRepository


class ProductsRepository(BaseRepository[Products]):
    model: Type[Products] = Products


    async def get_orders_by_product(self, product_id: UUID) -> list[Orders]:
        """
        Получить все заказы по определенному товару.
        """
        query = select(Orders).filter(Orders.product_id == product_id)
        result = await self.session.execute(query)
        return result.scalars().all()
    