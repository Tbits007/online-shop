from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.database import get_session
from app.schemas.orders_schemas import OrderCreateSchema, OrderResponseSchema, OrderUpdateSchema, StatusChoice
from app.services.orders_service import OrderService


router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
)


@router.post("/create_order/")
async def create_order(data: OrderCreateSchema, session: AsyncSession = Depends(get_session)) -> OrderResponseSchema:
    """
    Создать новый заказ.
    """
    order_service = OrderService(session)
    return await order_service.create_order(data)


@router.get("/")
async def get_orders(session: AsyncSession = Depends(get_session)) -> list[OrderResponseSchema]:
    """
    Получить список всех заказов.
    """
    order_service = OrderService(session)
    return await order_service.get_all_orders()


@router.get("/{id}/")
async def get_order(order_id: UUID, session: AsyncSession = Depends(get_session)) -> OrderResponseSchema:
    """
    Получить информацию о заказе по ID.
    """
    order_service = OrderService(session)
    return await order_service.get_order_by_id(order_id)


@router.put("/{id}/")
async def update_order(order_id: UUID, updated_data: OrderUpdateSchema, session: AsyncSession = Depends(get_session)) -> OrderResponseSchema:
    """
    Обновить информацию о заказе по ID.
    """
    order_service = OrderService(session)
    return await order_service.update_order(order_id, updated_data)


@router.delete("/{id}/")
async def delete_order(order_id: UUID, session: AsyncSession = Depends(get_session)) -> dict:
    """
    Удалить заказ по ID.
    """
    order_service = OrderService(session)
    await order_service.delete_order(order_id)
    return {"detail": "Order deleted successfully"} 


@router.get("/status/{status}/")
async def get_orders_by_status(status: StatusChoice, session: AsyncSession = Depends(get_session)) -> list[OrderResponseSchema]:
    """
    Получить заказы по статусу (например, "shipped", "delivered", "pending").
    """
    order_service = OrderService(session)
    return await order_service.get_orders_by_status(status)
