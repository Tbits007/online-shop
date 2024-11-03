from datetime import datetime
import json
import os
from typing import AsyncGenerator
import pytest_asyncio
from sqlalchemy import insert

os.environ["MODE"] = "TEST"

from app.infrastructure.database import Base, async_session_maker, engine
from app.infrastructure.config import settings
from app.domain.users import Users
from app.domain.categories import Categories
from app.domain.products import Products
from app.domain.orders import Orders
from fastapi.testclient import TestClient
from httpx import AsyncClient
from app.main import app as fastapi_app
from sqlalchemy.ext.asyncio import AsyncSession


# $env:MODE = "TEST"; pytest


@pytest_asyncio.fixture(loop_scope="session", autouse=True)
async def prepare_database():
    assert settings.MODE == "TEST"
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_mock_json(model: str):
        with open(f"tests/data_for_test_db/mock_{model}.json", encoding="utf-8") as file:
            return json.load(file)
    
    users = open_mock_json("users")
    categories = open_mock_json("categories")
    products = open_mock_json("products")
    orders = open_mock_json("orders")

    for order in orders:
        order["created_at"] = datetime.fromisoformat(order["created_at"])

    async with async_session_maker() as session:
        add_users = insert(Users).values(users)
        add_categories = insert(Categories).values(categories)
        add_products = insert(Products).values(products)
        add_orders = insert(Orders).values(orders)

        await session.execute(add_users)
        await session.execute(add_categories)
        await session.execute(add_products)
        await session.execute(add_orders)

        await session.commit()

    yield

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture
async def session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session_:
        yield session_


@pytest_asyncio.fixture
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac

