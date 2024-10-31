from fastapi import Depends, FastAPI
from fastapi.security import HTTPBearer
from app.api import users, categories, products, orders
from app.infrastructure.auth import auth

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from redis import asyncio as aioredis

# uvicorn app.main:app --reload

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

# Подключение маршрутов
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(categories.router)
app.include_router(products.router)
app.include_router(orders.router)
