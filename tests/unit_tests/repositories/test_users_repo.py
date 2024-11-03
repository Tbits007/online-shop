import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.orders import Orders, Status
from app.domain.users import Users
from app.repositories.users_repo import UsersRepository


@pytest_asyncio.fixture
async def users_repository(session: AsyncSession) -> UsersRepository:
    repo = UsersRepository(session)
    return repo


@pytest.mark.asyncio
async def test_get_orders_by_user_id(users_repository: UsersRepository, session: AsyncSession):
    # Создаём тестового пользователя
    test_user = Users(email="test@example.com", hashed_password="hashed_pwd")
    session.add(test_user)
    await session.commit()
    
    # Создаем тестовые заказы для пользователя
    order1 = Orders(
        user_id=test_user.id,
        status=Status.pending,
        product_id="f7de988d-c198-4bce-baf9-919fccf3b7aa",
        total_price=100.50,
    )
    order2 = Orders(
        user_id=test_user.id,
        status=Status.shipped,
        product_id="f7de988d-c198-4bce-baf9-919fccf3b7aa",
        total_price=200.75,
    )
    session.add_all([order1, order2])
    await session.commit()
    
    # Вызываем метод get_orders_by_user_id
    orders = await users_repository.get_orders_by_user_id(test_user.id)
    
    # Проверяем, что вернулись все заказы, связанные с пользователем
    assert len(orders) == 2
    assert orders[0].user_id == test_user.id
    assert orders[1].user_id == test_user.id
    assert orders[0].status == Status.pending
    assert orders[1].status == Status.shipped
    assert orders[0].total_price == 100.50
    assert orders[1].total_price == 200.75