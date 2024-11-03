import pytest
import pytest_asyncio
from uuid import uuid4
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.domain.products import Products
from app.schemas.products_schemas import ProductCreateSchema
from app.services.products_service import ProductService


@pytest_asyncio.fixture
async def setup_product_service(session: AsyncSession):
    """Создает экземпляр ProductService для тестов."""
    return ProductService(session)


@pytest_asyncio.fixture
async def mock_product(session: AsyncSession):
    """Создает тестовый продукт."""
    product = Products(
        name="Test Product",
        description="Description of Test Product",
        price=100.0,
        currency="USD",
        stock=10,
        category_id="973e3c4d-7ac7-405d-be90-110a46431bbc",  # Укажите реальный category_id, если необходимо
    )
    session.add(product)
    await session.commit()
    return product


@pytest.mark.asyncio
async def test_get_all_products(setup_product_service, mock_product):
    """Тестирует метод get_all_products."""
    products = await setup_product_service.get_all_products()
    assert len(products) > 0


@pytest.mark.asyncio
async def test_get_product_by_id(setup_product_service, mock_product):
    """Тестирует метод get_product_by_id."""
    product = await setup_product_service.get_product_by_id(mock_product.id)
    assert product.name == mock_product.name


@pytest.mark.asyncio
async def test_create_product(setup_product_service):
    """Тестирует метод create_product."""
    product_data = ProductCreateSchema(
        name="New Product",
        description="Description of New Product",
        price=200.0,
        currency="USD",
        stock=5,
        category_id="973e3c4d-7ac7-405d-be90-110a46431bbc", 
    )
    product = await setup_product_service.create_product(product_data)
    assert product.name == product_data.name


@pytest.mark.asyncio
async def test_update_product(setup_product_service, mock_product):
    """Тестирует метод update_product."""
    updated_data = {
        "name": "Updated Product",
        "description": "Updated Description",
        "price": 150.0,
        "currency": "USD",
        "stock": 15,
    }
    updated_product = await setup_product_service.update_product(mock_product.id, updated_data)
    assert updated_product.name == updated_data["name"]
    assert updated_product.price == updated_data["price"]


@pytest.mark.asyncio
async def test_delete_product(setup_product_service, mock_product):
    """Тестирует метод delete_product."""
    await setup_product_service.delete_product(mock_product.id)
    with pytest.raises(HTTPException):
        await setup_product_service.get_product_by_id(mock_product.id)


@pytest.mark.asyncio
async def test_get_orders_by_product(setup_product_service, mock_product):
    """Тестирует метод get_orders_by_product."""
    orders = await setup_product_service.get_orders_by_product(mock_product.id)
    # Здесь проверка должна зависеть от того, есть ли у продукта заказы.
    assert len(orders) == 0
