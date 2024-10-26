from fastapi import APIRouter
from pydantic import BaseModel, EmailStr # это убрать !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from app.database import async_session_maker, get_session
from app.repositories.users_repo import UsersRepository
from uuid import UUID
from app.services.users_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

# НУЖНЫ PYDANTIC MODELS ДЛЯ ВАЛИДАЦИИ ОТВЕТА !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    address: str

    
@router.get("/")
async def get_users(session: AsyncSession = Depends(get_session)):
    """
    Получить список всех пользователей.
    """    
    user_service = UserService(session)
    return await user_service.get_all_users()


@router.post("/create_user/")
async def create_user(user_data: UserCreate, session: AsyncSession = Depends(get_session)):
    """
    Создать нового пользователя.
    """
    print(user_data)
    user_service = UserService(session)
    return await user_service.create_user(user_data)


@router.get("/{id}/")
async def get_current_user(id: UUID, session: AsyncSession = Depends(get_session)):
    """
    Получить информацию о пользователе по ID.
    """       
    async with async_session_maker() as session:
        users_repo = UsersRepository(session)
        result = await users_repo.get_by_id(id)
        return result



@router.put("/{id}/")
async def update_user(session: AsyncSession = Depends(get_session)):
    """
    Обновить информацию о пользователе по ID.
    """
    pass


@router.delete("/{id}/")
async def delete_user(session: AsyncSession = Depends(get_session)):
    """
    Удалить пользователя по ID.
    """
    pass


@router.get("/{id}/orders/")
async def get_user_orders(session: AsyncSession = Depends(get_session)):
    """
    Получить все заказы пользователя по его ID.
    """
    pass