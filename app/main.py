from fastapi import Depends, FastAPI
from fastapi.security import HTTPBearer
from app.api import users, categories, products, orders
from app.infrastructure.admin_panel.veiws import UsersAdmin, CategoriesAdmin, ProductsAdmin, OrdersAdmin
from app.infrastructure.auth import auth
from sqladmin import Admin
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis
from app.infrastructure.database import engine

# uvicorn app.main:app --reload
# celery -A app.tasks.celery:celery worker --loglevel=INFO --pool=solo
# celery -A app.infrastructure.tasks.celery_app:celery flower

@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield


http_bearer = HTTPBearer(auto_error=False)

app = FastAPI(
    lifespan=lifespan,
    dependencies=[Depends(http_bearer)],
)


# Подключение админ-панели
admin = Admin(app, engine)

# Подключение представлений к админ-панели
admin.add_view(UsersAdmin)
admin.add_view(CategoriesAdmin)
admin.add_view(ProductsAdmin)
admin.add_view(OrdersAdmin)


# Подключение маршрутов
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(categories.router)
app.include_router(products.router)
app.include_router(orders.router)


