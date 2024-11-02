from typing import TypeVar
import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.base_repo import BaseRepository
from app.infrastructure.database import Base, async_session_maker
from app.domain.users import Users
from app.domain.categories import Categories
from app.domain.products import Products
from app.domain.orders import Orders
from typing import AsyncGenerator


# ModelType = TypeVar("ModelType", bound=Base)


# @pytest.fixture
# async def session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session_maker() as session_:
#         yield session_


# # Фикстура для репозитория, принимает сессию как зависимость
# @pytest.fixture(
#         scope="function",
#         params=[Users,
#                 Categories,
#                 Orders,
#                 Products,
#                ]
#         )
# def repository(session: AsyncSession, request) -> BaseRepository[ModelType]:
#     Model = request.param
#     repo = BaseRepository[Model](session)
#     repo.model = Model
#     return repo


# async def test_get_all(repository: BaseRepository[ModelType]):
#     result = await repository.get_all()
#     assert result is not None
   

# async def test_get_by_id(repository: BaseRepository[ModelType], session: AsyncSession):
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
