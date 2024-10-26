from typing import Type
from app.domain.orders import Orders
from app.repositories.base_repo import BaseRepository


class OrdersRepository(BaseRepository[Orders]):
    model: Type[Orders] = Orders