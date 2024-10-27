from uuid import UUID
from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from app.infrastructure.database import get_session
from app.schemas.orders_schemas import OrderResponseSchema
from app.schemas.products_schemas import ProductCreateSchema, ProductResponseSchema, ProductUpdateSchema
from app.services.products_service import ProductService


router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


@router.post("/create_product/")
async def create_product(data: ProductCreateSchema, session: AsyncSession = Depends(get_session)) -> ProductResponseSchema:
    """
    Создать новый продукт.
    """
    product_service = ProductService(session)
    return await product_service.create_product(data)
    

@router.get("/")
async def get_products(session: AsyncSession = Depends(get_session)) -> list[ProductResponseSchema]:
    """
    Получить список всех продуктов.
    """
    product_service = ProductService(session)
    return await product_service.get_all_products()


@router.get("/{id}/")
async def get_product(product_id: UUID, session: AsyncSession = Depends(get_session)) -> ProductResponseSchema:
    """
    Получить информацию о продукте по ID.
    """
    product_service = ProductService(session)
    return await product_service.get_product_by_id(product_id) 


@router.put("/{id}/")
async def update_product(product_id: UUID, updated_data: ProductUpdateSchema, session: AsyncSession = Depends(get_session)) -> ProductResponseSchema:
    """
    Обновить информацию о продукте по ID.
    """
    product_service = ProductService(session)
    updated_data = updated_data.model_dump(exclude_unset=True)
    return await product_service.update_product(product_id, updated_data)


@router.delete("/{id}/")
async def delete_product(product_id: UUID, session: AsyncSession = Depends(get_session)) -> dict:
    """
    Удалить продукт по ID.
    """
    product_service = ProductService(session)
    await product_service.delete_product(product_id)
    return {"detail": "Product deleted successfully"}


@router.get("/{id}/get_orders/")
async def get_orders_by_product(product_id: UUID, session: AsyncSession = Depends(get_session)) -> list[OrderResponseSchema]:
    """
    Получить все заказы по определенному товару.
    """
    product_service = ProductService(session)
    return await product_service.get_orders_by_product(product_id)
