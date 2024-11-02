from typing import Type, TypeVar
import pytest
import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.base_repo import BaseRepository
from app.infrastructure.database import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.future import select
from app.domain.users import Users
from app.domain.categories import Categories
from app.domain.products import Products
from app.domain.orders import Orders


ModelType = TypeVar("ModelType", bound=Base)

# Фикстура для репозитория, принимает сессию как зависимость
@pytest.fixture(
        scope="function",
        params=[Users,
                Categories,
                Orders,
                Products,
               ]
        )
def repository(session: AsyncSession, Model: ModelType) -> BaseRepository[ModelType]:
    repo = BaseRepository[Model](session)
    repo.model = Model
    return repo


def tt(repository: BaseRepository[ModelType]):
    print(type(repository))
    
# @pytest.mark.asyncio
# async def test_get_all(repository: BaseRepository[ModelType], session: AsyncSession):
#     # Добавляем тестовые данные
#     entity1 = TestModel(name="Entity1")
#     entity2 = TestModel(name="Entity2")
#     session.add_all([entity1, entity2])
#     await session.commit()

#     # Выполняем метод get_all
#     results = await repository.get_all()
    
#     # Проверяем, что вернулось 2 записи
#     assert len(results) == 2
#     assert results[0].name == "Entity1"
#     assert results[1].name == "Entity2"

# @pytest.mark.asyncio
# async def test_get_by_id(repository: BaseRepository[TestModel], session: AsyncSession):
#     # Добавляем тестовую запись
#     entity = TestModel(name="Entity")
#     session.add(entity)
#     await session.commit()

#     # Выполняем метод get_by_id
#     result = await repository.get_by_id(entity.id)

#     # Проверяем, что получена правильная запись
#     assert result is not None
#     assert result.id == entity.id
#     assert result.name == "Entity"

# @pytest.mark.asyncio
# async def test_create(repository: BaseRepository[TestModel], session: AsyncSession):
#     # Создаем новую запись
#     new_entity = TestModel(name="New Entity")
#     result = await repository.create(new_entity)

#     # Проверяем, что запись создана
#     assert result.id == new_entity.id
#     assert result.name == "New Entity"

#     # Проверяем, что запись существует в базе данных
#     query = select(TestModel).filter(TestModel.id == new_entity.id)
#     db_result = (await session.execute(query)).scalar_one_or_none()
#     assert db_result is not None

# @pytest.mark.asyncio
# async def test_update(repository: BaseRepository[TestModel], session: AsyncSession):
#     # Добавляем тестовую запись
#     entity = TestModel(name="Old Name")
#     session.add(entity)
#     await session.commit()

#     # Обновляем запись
#     updated_data = {"name": "Updated Name"}
#     result = await repository.update(entity.id, updated_data)

#     # Проверяем, что запись обновлена
#     assert result.name == "Updated Name"

# @pytest.mark.asyncio
# async def test_delete(repository: BaseRepository[TestModel], session: AsyncSession):
#     # Добавляем тестовую запись
#     entity = TestModel(name="Entity to Delete")
#     session.add(entity)
#     await session.commit()

#     # Удаляем запись
#     await repository.delete(entity.id)

#     # Проверяем, что запись удалена
#     result = await repository.get_by_id(entity.id)
#     assert result is None
