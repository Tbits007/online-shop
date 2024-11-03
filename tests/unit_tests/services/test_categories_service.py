import pytest
import pytest_asyncio
from uuid import uuid4
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.domain.categories import Categories
from app.schemas.categories_schemas import CategoryCreateSchema
from app.services.categories_service import CategoryService


@pytest_asyncio.fixture
async def setup_category_service(session: AsyncSession):
    """Создает экземпляр CategoryService для тестов."""
    return CategoryService(session)


@pytest_asyncio.fixture
async def mock_category(session: AsyncSession):
    """Создает тестовую категорию."""
    category = Categories(
        name="Test Category",
        description="Description of Test Category"
    )
    session.add(category)
    await session.commit()
    return category


@pytest.mark.asyncio
async def test_get_all_categories(setup_category_service, mock_category):
    """Тестирует метод get_all_categories."""
    categories = await setup_category_service.get_all_categories()
    assert len(categories) > 0


@pytest.mark.asyncio
async def test_get_category_by_id(setup_category_service, mock_category):
    """Тестирует метод get_category_by_id."""
    category = await setup_category_service.get_category_by_id(mock_category.id)
    assert category.id == mock_category.id


@pytest.mark.asyncio
async def test_create_category(setup_category_service):
    """Тестирует метод create_category."""
    category_data = CategoryCreateSchema(
        name="New Category",
        description="Description of New Category"
    )
    category = await setup_category_service.create_category(category_data)
    assert category.name == category_data.name


@pytest.mark.asyncio
async def test_update_category(setup_category_service, mock_category):
    """Тестирует метод update_category."""
    updated_data = {
        "name": "Updated Category",
        "description": "Updated Description"
    }
    updated_category = await setup_category_service.update_category(mock_category.id, updated_data)
    assert updated_category.name == updated_data["name"]


@pytest.mark.asyncio
async def test_delete_category(setup_category_service, mock_category):
    """Тестирует метод delete_category."""
    await setup_category_service.delete_category(mock_category.id)
    with pytest.raises(HTTPException):
        await setup_category_service.get_category_by_id(mock_category.id)


@pytest.mark.asyncio
async def test_get_products_by_category(setup_category_service, mock_category):
    """Тестирует метод get_products_by_category."""
    products = await setup_category_service.get_products_by_category(mock_category.id)
    assert len(products) == 0