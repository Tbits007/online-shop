from typing import Type
from app.domain.products import Products
from app.repositories.base_repo import BaseRepository


class ProductsRepository(BaseRepository[Products]):
    model: Type[Products] = Products