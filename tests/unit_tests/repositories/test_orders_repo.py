import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.orders import Orders
from app.repositories.orders_repo import OrdersRepository
from app.schemas.orders_schemas import StatusChoice
from app.domain.products import Products
from app.domain.users import Users
from app.domain.categories import Categories


@pytest_asyncio.fixture
async def setup_data(session: AsyncSession):
    """Создает тестовые данные для категорий, пользователей, продуктов и заказов."""

    # Создаем категорию
    category = Categories(
        name="Test Category",
        description="Description of Test Category",
    )
    session.add(category)
    await session.commit()

    # Создаем пользователя
    user = Users(
        email="test@example.com",
        hashed_password="hashedpassword",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )
    session.add(user)
    await session.commit()

    # Создаем продукт
    product = Products(
        name="Test Product",
        description="Description of Test Product",
        price=100.0,
        currency="USD",
        stock=10,
        category_id=category.id,
    )
    session.add(product)
    await session.commit()

    # Создаем заказы с разными статусами
    order1 = Orders(
        user_id=user.id,
        status=StatusChoice.shipped,
        product_id=product.id,
        total_price=100.0,
    )
    order2 = Orders(
        user_id=user.id,
        status=StatusChoice.delivered,
        product_id=product.id,
        total_price=100.0,
    )
    order3 = Orders(
        user_id=user.id,
        status=StatusChoice.pending,
        product_id=product.id,
        total_price=100.0,
    )
    session.add_all([order1, order2, order3])
    await session.commit()

    return order1, order2, order3


@pytest_asyncio.fixture
async def orders_repository(session: AsyncSession) -> OrdersRepository:
    repo = OrdersRepository(session)
    return repo


@pytest.mark.asyncio
async def test_get_orders_by_status(setup_data, orders_repository):
    """Тестирует метод get_orders_by_status для различных статусов."""
    order1, order2, order3 = setup_data

    # Проверяем заказы со статусом 'shipped'
    shipped_orders = await orders_repository.get_orders_by_status(StatusChoice.shipped)
    assert shipped_orders is not None

    # Проверяем заказы со статусом 'delivered'
    delivered_orders = await orders_repository.get_orders_by_status(StatusChoice.delivered)
    assert delivered_orders is not None

    # Проверяем заказы со статусом 'pending'
    pending_orders = await orders_repository.get_orders_by_status(StatusChoice.pending)
    assert pending_orders is not None
