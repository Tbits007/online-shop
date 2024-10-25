from fastapi import APIRouter


router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


@router.post("/create_category/")
def create_category():
    """
    Создать новую категорию.
    """
    pass


@router.get("/")
def get_categories():
    """
    Получить список всех категорий.
    """
    pass


@router.get("/{id}/")
def get_category():
    """
    Получить информацию о категории по ID.
    """
    pass


@router.put("/{id}/")
def update_category():
    """
    Обновить информацию о категории по ID.
    """
    pass


@router.put("/{id}/")
def delete_category():
    """
    Удалить категорию по ID.
    """
    pass


@router.get("/{id}/products/")
def get_category_products():
    """
    Получить все продукты в категории по ее ID.
    """
    pass

