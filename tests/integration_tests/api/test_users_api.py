import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession
from app.main import app  # Импортируйте ваше приложение FastAPI
from app.infrastructure.database import get_session
from app.domain.users import Users
from app.schemas.users_schemas import UserResponseSchema
from app.schemas.orders_schemas import OrderResponseSchema


@pytest.fixture
async def setup_database(session: AsyncSession):
    # Здесь вы можете настроить базу данных для тестов
    # Создайте пользователей и заказы для тестирования
    user = Users(
        email="testuser@example.com",
        hashed_password="hashedpassword",
        is_active=True,
        is_superuser=True,
        is_verified=True,
    )
    session.add(user)
    await session.commit()
    await session.refresh(user)  # Получите сгенерированный ID пользователя

    # Добавьте заказы для пользователя
    # Вставьте ваш код для создания заказов здесь

    yield user  # Возвращаем пользователя для дальнейшего использования в тестах

    # Здесь можно добавить код для очистки базы данных после тестов


@pytest.mark.asyncio
async def test_get_users(async_client, setup_database):
    """Тестирует эндпоинт получения списка всех пользователей."""
    response = await async_client.get("/users/")
    assert response.status_code == 401
 

@pytest.mark.asyncio
async def test_get_user_orders(async_client, setup_database):
    """Тестирует эндпоинт получения всех заказов пользователя по его ID."""
    user_id = setup_database.id  # Используем ID созданного пользователя

    response = await async_client.get(f"/users/{user_id}/orders/")
    assert response.status_code == 401
    # Дополнительно можно проверить количество заказов или содержимое
    # assert len(response.json()) == 0  # Если заказов нет
