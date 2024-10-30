from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.users import Users
from app.infrastructure.database import get_session


async def get_user_db(session: AsyncSession = Depends(get_session)):
    """
    Получение адаптера для работы с пользователями.
    """
    yield SQLAlchemyUserDatabase(session, Users)