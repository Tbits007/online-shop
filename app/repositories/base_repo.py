from typing import Generic, Type, TypeVar, List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


T = TypeVar("T")  # Тип сущности, с которой работает репозиторий


class BaseRepository(Generic[T]):
    model: Type[T] = None
    

    def __init__(self, session: AsyncSession) -> None:
        self.session = session


    async def get_all(self) -> List[T]:
        """
        Получить все записи.
        """
        query = select(self.model)
        result = await self.session.execute(query)

        return result.scalars().all() # [<app.domain.users.Users object at 0x0000018CBC3CDD00>, ...]


    async def get_by_id(self, entity_id: int) -> Optional[T]:
        """
        Получить запись по ID.
        """
        query = select(self.model).filter(self.model.id == entity_id)
        result = await self.session.execute(query)

        return result.scalar_one_or_none() # <app.domain.users.Users object at 0x0000018CBC3CDD00> | None


    async def create(self, entity: T) -> T:
        """
        Создать новую запись.
        """
        async with self.session.begin():
            self.session.add(entity)

        await self.session.commit() 
        return entity

    async def update(self, entity_id: int, updated_data: dict) -> T:
        """
        Обновить существующую запись.
        """
        async with self.session.begin():
            stmt = select(self.model).filter(self.model.id == entity_id)
            result = await self.session.execute(stmt)
            obj = result.scalar_one_or_none()

            if obj is None:
                raise ValueError("Object is not found")

            for key, value in updated_data.items():
                setattr(obj, key, value)

        await self.session.commit()
        return obj

    async def delete(self, entity_id: int) -> None:
        """
        Удалить запись по ID.
        """
        entity = await self.get_by_id(entity_id)

        if entity is None:
            raise ValueError("Object is not found")
           
        async with self.session.begin():
            await self.session.delete(entity)  # Удаляем сущность

        await self.session.commit()
