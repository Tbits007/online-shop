import pytest
import pytest_asyncio
from uuid import uuid4
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.domain.orders import Orders
from app.schemas.orders_schemas import OrderCreateSchema, OrderUpdateSchema, StatusChoice
from app.services.orders_service import OrderService


@pytest_asyncio.fixture
async def setup_order_service(session: AsyncSession):
    """Создает экземпляр OrderService для тестов."""
    return OrderService(session)


@pytest_asyncio.fixture
async def mock_order(session: AsyncSession):
    """Создает тестовый заказ."""
    order = Orders(
        user_id="3d90525e-eb5e-4ea9-805e-6012175efdf9",
        status=StatusChoice.pending,
        product_id="541d7d88-6cef-49fe-a210-c978ef012cfd",
        total_price=100.0,
    )
    session.add(order)
    await session.commit()
    return order


@pytest.mark.asyncio
async def test_get_all_orders(setup_order_service, mock_order):
    """Тестирует метод get_all_orders."""
    orders = await setup_order_service.get_all_orders()
    assert len(orders) > 0


@pytest.mark.asyncio
async def test_get_order_by_id(setup_order_service, mock_order):
    """Тестирует метод get_order_by_id."""
    order = await setup_order_service.get_order_by_id(mock_order.id)
    assert order.id == mock_order.id


@pytest.mark.asyncio
async def test_create_order(setup_order_service):
    """Тестирует метод create_order."""
    order_data = OrderCreateSchema(
        user_id="3d90525e-eb5e-4ea9-805e-6012175efdf9",  # Укажите реальный user_id
        status=StatusChoice.pending,
        product_id="541d7d88-6cef-49fe-a210-c978ef012cfd",  # Укажите реальный product_id
        total_price=200.0,
    )
    order = await setup_order_service.create_order(order_data)
    assert order.status == order_data.status
    assert order.total_price == order_data.total_price


@pytest.mark.asyncio
async def test_update_order(setup_order_service, mock_order):
    """Тестирует метод update_order."""
    updated_data = OrderUpdateSchema(
        user_id="3d90525e-eb5e-4ea9-805e-6012175efdf9",  # Укажите реальный user_id
        status=StatusChoice.pending,
        product_id="541d7d88-6cef-49fe-a210-c978ef012cfd",  # Укажите реальный product_id
        total_price=200.0,
    )
    updated_order = await setup_order_service.update_order(mock_order.id, updated_data)
    assert updated_order.status == updated_data.status
    assert updated_order.total_price == updated_data.total_price


@pytest.mark.asyncio
async def test_delete_order(setup_order_service, mock_order):
    """Тестирует метод delete_order."""
    await setup_order_service.delete_order(mock_order.id)
    with pytest.raises(HTTPException):
        await setup_order_service.get_order_by_id(mock_order.id)


@pytest.mark.asyncio
async def test_get_orders_by_status(setup_order_service, mock_order):
    """Тестирует метод get_orders_by_status."""
    orders = await setup_order_service.get_orders_by_status(StatusChoice.pending)
    assert any(order.status == StatusChoice.pending for order in orders)
