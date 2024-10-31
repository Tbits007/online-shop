from fastapi import Depends, FastAPI
from fastapi.security import HTTPBearer
from app.api import users, categories, products, orders
from app.infrastructure.auth import auth


http_bearer = HTTPBearer(auto_error=False)


app = FastAPI(
    dependencies=[Depends(http_bearer)],
)

# Подключение маршрутов
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(categories.router)
app.include_router(products.router)
app.include_router(orders.router)

# uvicorn app.main:app --reload