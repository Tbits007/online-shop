from fastapi import APIRouter


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/")
def get_users():
    """
    Получить список всех пользователей.
    """    
    pass


@router.post("/create_user/")
def create_user():
    """
    Создать нового пользователя.
    """
    pass


@router.get("/me/")
def get_current_user():
    """
    Получить информацию о пользователе по ID.
    """       
    pass


@router.put("/{id}/")
def update_user():
    """
    Обновить информацию о пользователе по ID.
    """
    pass


@router.delete("/{id}/")
def delete_user():
    """
    Удалить пользователя по ID.
    """
    pass


@router.get("/{id}/orders/")
def get_user_orders():
    """
    Получить все заказы пользователя по его ID.
    """
    pass