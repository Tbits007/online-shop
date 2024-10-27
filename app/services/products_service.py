from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.domain.products import Products
from app.domain.orders import Orders
from app.repositories.products_repo import ProductsRepository
from app.schemas.products_schemas import ProductCreateSchema, ProductUpdateSchema


class ProductService:
    def __init__(self, session: AsyncSession):
        self.product_repo = ProductsRepository(session)


    async def get_all_products(self) -> list[Products]:
        return await self.product_repo.get_all()


    async def get_product_by_id(self, product_id: UUID) -> Products | None:
        product = await self.product_repo.get_by_id(product_id)
        if product is None:
            raise HTTPException(status_code=500)
        return product


    async def create_product(self, data: ProductCreateSchema) -> Products:
        product = Products(
            name=data.name,
            description=data.description,
            price=data.price,
            currency=data.currency,
            stock=data.stock,
            category_id=data.category_id
        )
        return await self.product_repo.create(product)


    async def update_product(self, product_id: UUID, updated_data: dict) -> Products:
        product = await self.get_product_by_id(product_id)
        return await self.product_repo.update(product_id, updated_data)


    async def delete_product(self, product_id: UUID) -> None:
        product = await self.get_product_by_id(product_id)
        await self.product_repo.delete(product_id)


    async def get_orders_by_product(self, product_id: UUID) -> list[Orders]:
        return await self.product_repo.get_orders_by_product(product_id)
    
