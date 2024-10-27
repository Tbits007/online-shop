from typing import Type
from uuid import UUID

from sqlalchemy import select
from app.domain.orders import Orders
from app.domain.users import Users
from app.repositories.base_repo import BaseRepository


class UsersRepository(BaseRepository[Users]):
    model: Type[Users] = Users


    async def get_orders_by_user_id(self, user_id: UUID) -> list[Orders]:
        """
        Получить все заказы пользователя по его ID.
        """
        query = select(Orders).filter(Orders.user_id == user_id)
        result = await self.session.execute(query)
        return result.scalars().all()