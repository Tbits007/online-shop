import pytest
import pytest_asyncio
from uuid import uuid4
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.domain.users import Users
from app.schemas.users_schemas import UserCreateSchema
from app.services.users_service import UserService


@pytest_asyncio.fixture
async def setup_user_service(session: AsyncSession):
    """Создает экземпляр UserService для тестов."""
    return UserService(session)


@pytest_asyncio.fixture
async def mock_user(session: AsyncSession):
    """Создает тестового пользователя."""
    user = Users(
        email="test@example.com",
        hashed_password="hashedpassword",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )
    session.add(user)
    await session.commit()
    return user


@pytest.mark.asyncio
async def test_get_all_users(setup_user_service, mock_user):
    """Тестирует метод get_all_users."""
    users = await setup_user_service.get_all_users()
    assert len(users) > 0


@pytest.mark.asyncio
async def test_get_user_by_id(setup_user_service, mock_user):
    """Тестирует метод get_user_by_id."""
    user = await setup_user_service.get_user_by_id(mock_user.id)
    assert user.email == mock_user.email


@pytest.mark.asyncio
async def test_create_user(setup_user_service):
    """Тестирует метод create_user."""
    user_data = UserCreateSchema(
        email="newuser@example.com",
        password="hashedpassword",
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )
    user = await setup_user_service.create_user(user_data)
    assert user.email == user_data.email


@pytest.mark.asyncio
async def test_update_user(setup_user_service, mock_user):
    """Тестирует метод update_user."""
    updated_data = {
        "email": "updated@example.com",
        "is_active": False,
    }
    updated_user = await setup_user_service.update_user(mock_user.id, updated_data)
    assert updated_user.email == updated_data["email"]
    assert updated_user.is_active == updated_data["is_active"]


@pytest.mark.asyncio
async def test_delete_user(setup_user_service, mock_user):
    """Тестирует метод delete_user."""
    await setup_user_service.delete_user(mock_user.id)
    with pytest.raises(HTTPException):
        await setup_user_service.get_user_by_id(mock_user.id)


@pytest.mark.asyncio
async def test_get_user_orders(setup_user_service, mock_user):
    """Тестирует метод get_user_orders."""
    orders = await setup_user_service.get_user_orders(mock_user.id)
    # Здесь проверка должна зависеть от того, есть ли у пользователя заказы.
    assert len(orders) == 0  # Или проверьте конкретное условие, если есть заказы.
