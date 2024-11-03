import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.orders import Orders, Status
from app.domain.products import Products
from app.domain.users import Users
from app.repositories.products_repo import ProductsRepository


@pytest_asyncio.fixture
async def products_repository(session: AsyncSession) -> ProductsRepository:
    repo = ProductsRepository(session)
    return repo


@pytest.mark.asyncio
async def test_get_orders_by_product(products_repository: ProductsRepository, session: AsyncSession):
    # Создаём тестового пользователя
    test_user = Users(email="test@example.com", hashed_password="hashed_pwd")
    session.add(test_user)
    await session.commit()

    # Создаем тестовый товар
    test_product = Products(
        name="Test Product",
        description="Description of Test Product",
        price=100.0,
        currency="USD",
        stock=10,
        category_id="1a3244de-7a99-413c-8e6f-dc0fa530d7d6",
    )
    session.add(test_product)
    await session.commit()
    
    # Создаем тестовые заказы
    order1 = Orders(
        user_id=test_user.id,
        status=Status.pending,
        product_id=test_product.id,
        total_price=100.50,
    )
    order2 = Orders(
        user_id=test_user.id,
        status=Status.shipped,
        product_id=test_product.id,
        total_price=200.75,
    )
    session.add_all([order1, order2])
    await session.commit()

    # Вызываем метод get_orders_by_product
    orders = await products_repository.get_orders_by_product(test_product.id)
    
    # Проверяем, что вернулись только заказы, связанные с тестовым товаром
    assert len(orders) == 2
    assert all(order.product_id == test_product.id for order in orders)
    assert orders[0].status == Status.pending
    assert orders[1].status == Status.shipped