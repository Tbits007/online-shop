from fastapi import HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.orders import Orders
from app.repositories.users_repo import UsersRepository
from app.domain.users import Users
from app.schemas.users_schemas import UserCreateSchema


class UserService:
    def __init__(self, session: AsyncSession):
        self.user_repo = UsersRepository(session)  # Используйте ваш репозиторий


    async def get_all_users(self) -> list[Users]:
        # здесь можно добавить дополнительную логику
        return await self.user_repo.get_all()  # Получите всех пользователей через репозиторий


    async def get_user_by_id(self, user_id: int) -> Users | None:
        # здесь можно добавить дополнительную логику
        user = await self.user_repo.get_by_id(user_id)
        if user is None:
            raise HTTPException(status_code=500)
        return user
    

    async def create_user(self, data: UserCreateSchema) -> Users:
        user = Users(
            name=data.name,
            email=data.email,
            password=data.password,
            address=data.address
        )

        return await self.user_repo.create(user)
    

    async def update_user(self, user_id: int, updated_data: dict) -> Users:
        user = await self.get_user_by_id(user_id)
        return await self.user_repo.update(user_id, updated_data)


    async def delete_user(self, user_id: int) -> None:
        user = await self.get_user_by_id(user_id)
        await self.user_repo.delete(user_id)


    async def get_user_orders(self, user_id: int) -> list[Orders]:
        user = await self.get_user_by_id(user_id)
        return await self.user_repo.get_orders_by_user_id(user_id)

        