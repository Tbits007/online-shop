from uuid import UUID
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.categories import Categories
from app.domain.products import Products
from app.repositories.categories_repo import CategoriesRepository
from app.schemas.categories_schemas import CategoryCreateSchema


class CategoryService:
    def __init__(self, session: AsyncSession):
        self.category_repo = CategoriesRepository(session)


    async def get_all_categories(self) -> list[Categories]:
        # Здесь можно добавить дополнительную логику
        return await self.category_repo.get_all()


    async def get_category_by_id(self, category_id: UUID) -> Categories | None:
        category = await self.category_repo.get_by_id(category_id)
        if category is None:
            raise HTTPException(status_code=500)
        return category


    async def create_category(self, data: CategoryCreateSchema) -> Categories:
        category = Categories(
            name=data.name,
            description=data.description
        )
        return await self.category_repo.create(category)


    async def update_category(self, category_id: UUID, updated_data: dict) -> Categories:
        category = await self.get_category_by_id(category_id)
        return await self.category_repo.update(category_id, updated_data)


    async def delete_category(self, category_id: UUID) -> None:
        category = await self.get_category_by_id(category_id)
        await self.category_repo.delete(category_id)


    async def get_products_by_category(self, category_id: UUID) -> list[Products]:
        category = await self.get_category_by_id(category_id)
        return await self.category_repo.get_products_by_category(category_id)