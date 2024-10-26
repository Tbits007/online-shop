from typing import Dict, Generic, List, Optional
from fastapi import HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.users_repo import UsersRepository
from app.domain.users import Users

# НУЖНЫ PYDANTIC MODELS ДЛЯ ВАЛИДАЦИИ ОТВЕТА !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    address: str

class UserService:
    def __init__(self, session: AsyncSession):
        self.user_repo = UsersRepository(session)  # Используйте ваш репозиторий

    async def get_all_users(self) -> List[Users]:
        # здесь можно добавить дополнительную логику
        return await self.user_repo.get_all()  # Получите всех пользователей через репозиторий

    async def get_user_by_id(self, user_id: int) -> Optional[Users]:
        # здесь можно добавить дополнительную логику
        user = await self.user_repo.get_by_id(user_id)

        if user is None:
            raise HTTPException(status_code=500)
        
        return user
    
    async def create_user(self, data: UserCreate) -> Users:
        user = Users(
            name=data.name,
            email=data.email,
            password=data.password,
            address=data.address
        )

        try:
            await self.user_repo.create(user)
        except Exception:
            raise HTTPException(status_code=500)
        
        return user
    
    async def update_user(self, user_id: int, updated_data: dict) -> Users:
        user = await self.get_user_by_id(user_id)

        if user is None:
            raise HTTPException(status_code=500)
        
        return await self.user_repo.update(user_id, updated_data)

    async def delete_user(self, user_id: int) -> None:
        user = await self.get_user_by_id(user_id)
        
        if user is None:
            raise HTTPException(status_code=500)
        
        await self.user_repo.delete(user_id)
