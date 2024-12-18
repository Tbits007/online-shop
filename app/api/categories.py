from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.database import get_session
from app.schemas.categories_schemas import CategoryCreateSchema, CategoryResponseSchema, CategoryUpdateSchema
from app.schemas.products_schemas import ProductResponseSchema
from app.services.categories_service import CategoryService
from fastapi_cache.decorator import cache
from app.infrastructure.utils import clear_cache

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


@router.post("/create_category/")
async def create_category(data: CategoryCreateSchema, session: AsyncSession = Depends(get_session)) -> CategoryResponseSchema:
    """
    Создать новую категорию.
    """
    category_service = CategoryService(session)
    result = await category_service.create_category(data)
    await clear_cache()
    return result


@router.get("/")
@cache(expire=60)
async def get_categories(session: AsyncSession = Depends(get_session)) -> list[CategoryResponseSchema]:
    """
    Получить список всех категорий.
    """
    category_service = CategoryService(session)
    return await category_service.get_all_categories()


@router.get("/{id}/")
@cache(expire=60)
async def get_category(category_id: UUID, session: AsyncSession = Depends(get_session)) -> CategoryResponseSchema:
    """
    Получить информацию о категории по ID.
    """
    category_service = CategoryService(session)
    return await category_service.get_category_by_id(category_id)



@router.put("/{id}/")
async def update_category(category_id: UUID, updated_data: CategoryUpdateSchema, session: AsyncSession = Depends(get_session)) -> CategoryResponseSchema:
    """
    Обновить информацию о категории по ID.
    """
    category_service = CategoryService(session)
    result = await category_service.update_category(category_id, updated_data.model_dump())
    await clear_cache()
    return result

@router.delete("/{id}/")
async def delete_category(category_id: UUID, session: AsyncSession = Depends(get_session)) -> dict:
    """
    Удалить категорию по ID.
    """
    category_service = CategoryService(session)
    await category_service.delete_category(category_id)
    await clear_cache()
    return {"detail": "Category deleted successfully"}


@router.get("/{id}/products/")
@cache(expire=60)
async def get_category_products(category_id: UUID, session: AsyncSession = Depends(get_session)) -> list[ProductResponseSchema]:
    """
    Получить все продукты в категории по ее ID.
    """
    category_service = CategoryService(session)
    return await category_service.get_products_by_category(category_id)

