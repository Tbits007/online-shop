import asyncio
from fastapi_versioning import version
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from app.domain.users import Users
from app.infrastructure.database import get_session
from uuid import UUID
from app.schemas.orders_schemas import OrderResponseSchema
from app.schemas.users_schemas import UserResponseSchema, UserUpdateSchema
from app.services.users_service import UserService
from app.infrastructure.auth.dependencies.FastAPIUsersObject import fastapi_users
from app.infrastructure.auth.dependencies.UserObject import current_active_superuser

from fastapi_cache.decorator import cache

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


router.include_router(
    fastapi_users.get_users_router(UserResponseSchema, UserUpdateSchema)
)

    
@router.get("/")
@version(1)
@cache(expire=60)
async def get_users(
    session: AsyncSession = Depends(get_session),
    user: Users = Depends(current_active_superuser)
) -> list[UserResponseSchema]:
    """
    Получить список всех пользователей.
    """    
    user_service = UserService(session)
    return await user_service.get_all_users()



@router.get("/{id}/orders/")
@cache(expire=60)
async def get_user_orders(
    user_id: UUID,
    session: AsyncSession = Depends(get_session),
    user: Users = Depends(current_active_superuser)
) -> list[OrderResponseSchema]:
    """
    Получить все заказы пользователя по его ID.
    """
    user_service = UserService(session)
    return await user_service.get_user_orders(user_id)


# @router.post("/create_user/")
# async def create_user(user_data: UserCreateSchema, session: AsyncSession = Depends(get_session)) -> UserResponseSchema:
#     """
#     Создать нового пользователя.
#     """
#     user_service = UserService(session)
#     return await user_service.create_user(user_data)


# @router.get("/{id}/")
# async def get_user_by_id(user_id: UUID, session: AsyncSession = Depends(get_session)) -> UserResponseSchema:
#     """
#     Получить информацию о пользователе по ID.
#     """       
#     user_service = UserService(session)
#     return await user_service.get_user_by_id(user_id)



# @router.put("/{id}/")
# async def update_user(user_id: UUID, user_data: UserUpdateSchema, session: AsyncSession = Depends(get_session)) -> UserResponseSchema:
#     """
#     Обновить информацию о пользователе по ID.
#     """
#     user_service = UserService(session)
#     return await user_service.update_user(user_id, user_data.model_dump())


# @router.delete("/{id}/")
# async def delete_user(user_id: UUID, session: AsyncSession = Depends(get_session)) -> dict:
#     """
#     Удалить пользователя по ID.
#     """
#     user_service = UserService(session)
#     await user_service.delete_user(user_id)    
#     return {"detail": "User deleted successfully"}

