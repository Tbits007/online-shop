from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.users import Users
from app.infrastructure.auth.models import AccessToken
from app.infrastructure.database import get_session
from fastapi_users.authentication.strategy.db import AccessTokenDatabase, DatabaseStrategy
from app.infrastructure.config import settings
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
    Получение адаптера для работы с токеном из таблицы accesstoken.
    """  
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)


def get_database_strategy(
    access_token_db: AccessTokenDatabase[AccessToken] = Depends(get_access_token_db),
) -> DatabaseStrategy:
    """
    Получение адаптера для работы со всей таблицей access token.
    """
    return DatabaseStrategy(access_token_db, lifetime_seconds=settings.access_token.lifetime_seconds)