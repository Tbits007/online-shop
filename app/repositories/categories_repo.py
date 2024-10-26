from typing import Type
from app.domain.categories import Categories
from app.repositories.base_repo import BaseRepository


class CategoriesRepository(BaseRepository[Categories]):
    model: Type[Categories] = Categories