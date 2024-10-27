from typing import Type
from uuid import UUID
from sqlalchemy import select
from app.domain.categories import Categories
from app.domain.products import Products
from app.repositories.base_repo import BaseRepository


class CategoriesRepository(BaseRepository[Categories]):
    model: Type[Categories] = Categories


    async def get_products_by_category(self, category_id: UUID) -> list[Products]:
        """
        Получить все продукты в категории по ее ID.
        """
        query = select(Products).filter(Products.category_id == category_id)
        result = await self.session.execute(query)
        return result.scalars().all()