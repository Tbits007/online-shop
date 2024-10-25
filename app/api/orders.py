from fastapi import APIRouter


router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
)


@router.post("/create_order/")
def create_order():
    """
    Создать новый заказ.
    """
    pass


@router.get("/")
def get_orders():
    """
    Получить список всех заказов.
    """
    pass


@router.get("/{id}/")
def get_order():
    """
    Получить информацию о заказе по ID.
    """
    pass


@router.put("/{id}/")
def update_order():
    """
    Обновить информацию о заказе по ID.
    """
    pass


@router.delete("/{id}/")
def delete_order():
    """
    Удалить заказ по ID.
    """
    pass


@router.get("/status/{status}/")
def get_orders_by_status():
    """
    Получить заказы по статусу (например, "shipped", "delivered", "pending").
    """
    pass
