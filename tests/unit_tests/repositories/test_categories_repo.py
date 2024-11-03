import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.categories import Categories
from app.domain.products import Products
from app.repositories.categories_repo import CategoriesRepository


@pytest_asyncio.fixture
async def setup_category_data(session: AsyncSession):
    """Создает тестовые данные для категории и продуктов, связанных с ней."""
    
    # Создаем категорию
    category = Categories(
        name="Test Category",
        description="Description of Test Category",
    )
    session.add(category)
    await session.commit()

    # Создаем продукты, связанные с этой категорией
    product1 = Products(
        name="Test Product 1",
        description="Description of Test Product 1",
        price=100.0,
        currency="USD",
        stock=10,
        category_id=category.id,  # Ссылка на созданную категорию
    )
    
    product2 = Products(
        name="Test Product 2",
        description="Description of Test Product 2",
        price=150.0,
        currency="USD",
        stock=5,
        category_id=category.id,  # Ссылка на созданную категорию
    )

    session.add_all([product1, product2])
    await session.commit()

    return category


@pytest_asyncio.fixture
async def categories_repository(session: AsyncSession) -> CategoriesRepository:
    repo = CategoriesRepository(session)
    return repo


@pytest.mark.asyncio
async def test_get_category_by_id(setup_category_data, categories_repository):
    """Тестирует метод get_category_by_id для получения категории по ID."""
    category = setup_category_data

    # Проверяем получение категории по ID
    fetched_category = await categories_repository.get_products_by_category(category.id)
    assert fetched_category is not None