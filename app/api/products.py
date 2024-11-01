from uuid import UUID
from fastapi import APIRouter, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from app.infrastructure.database import get_session
from app.infrastructure.tasks.tasks import process_pic
from app.schemas.orders_schemas import OrderResponseSchema
from app.schemas.products_schemas import ProductCreateSchema, ProductResponseSchema, ProductUpdateSchema
from app.services.products_service import ProductService
from fastapi_cache.decorator import cache
from app.infrastructure.utils import clear_cache
import shutil

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


@router.post("/add_image/")
async def add_product_image(name: int, file: UploadFile):
    img_path = f"app/infrastructure/frontend/static/images/{name}.webp"
    
    with open(img_path, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)

    process_pic.delay(img_path)
    await clear_cache()
    return {"message": "Image uploaded"}


@router.post("/create_product/")
async def create_product(data: ProductCreateSchema, session: AsyncSession = Depends(get_session)) -> ProductResponseSchema:
    """
    Создать новый продукт.
    """
    product_service = ProductService(session)
    result = await product_service.create_product(data)
    await clear_cache()
    return result


@router.get("/")
@cache(expire=60)
async def get_products(session: AsyncSession = Depends(get_session)) -> list[ProductResponseSchema]:
    """
    Получить список всех продуктов.
    """
    product_service = ProductService(session)
    return await product_service.get_all_products()


@router.get("/{id}/")
@cache(expire=60)
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
    result = await product_service.update_product(product_id, updated_data)
    await clear_cache()
    return result


@router.delete("/{id}/")
async def delete_product(product_id: UUID, session: AsyncSession = Depends(get_session)) -> dict:
    """
    Удалить продукт по ID.
    """
    product_service = ProductService(session)
    await product_service.delete_product(product_id)
    await clear_cache()
    return {"detail": "Product deleted successfully"}


@router.get("/{id}/get_orders/")
@cache(expire=60)
async def get_orders_by_product(product_id: UUID, session: AsyncSession = Depends(get_session)) -> list[OrderResponseSchema]:
    """
    Получить все заказы по определенному товару.
    """
    product_service = ProductService(session)
    return await product_service.get_orders_by_product(product_id)
