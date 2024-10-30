from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.users import Users
from app.infrastructure.auth.models import AccessToken
from app.infrastructure.database import get_session
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
)


async def get_user_db(session: AsyncSession = Depends(get_session)):
    """
    Получение адаптера для работы с пользователями.
    """
    yield SQLAlchemyUserDatabase(session, Users)


async def get_access_token_db(session: AsyncSession = Depends(get_session)):
    """
    Получение адаптера для работы с access token.
    """  
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)