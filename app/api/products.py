from fastapi import APIRouter


router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


@router.post("/create_product/")
def create_product():
    """
    Создать новый продукт.
    """
    pass
    

@router.get("/")
def get_products():
    """
    Получить список всех продуктов.
    """
    pass


@router.get("/{id}/")
def get_product():
    """
    Получить информацию о продукте по ID.
    """
    pass 


@router.put("/{id}/")
def update_product():
    """
    Обновить информацию о продукте по ID.
    """
    pass


@router.delete("/{id}/")
def delete_product():
    """
    Удалить продукт по ID.
    """
    pass
