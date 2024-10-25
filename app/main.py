from fastapi import FastAPI
from app.api import users, categories, products, orders


app = FastAPI()

# Подключение маршрутов
app.include_router(users.router)
app.include_router(categories.router)
app.include_router(products.router)
app.include_router(orders.router)


# uvicorn app.main:app --reload