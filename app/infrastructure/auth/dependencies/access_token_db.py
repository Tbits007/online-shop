from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.auth.models import AccessToken
from app.infrastructure.database import get_session
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
)


async def get_access_token_db(session: AsyncSession = Depends(get_session)):
    """
    Получение адаптера для работы с токеном из таблицы accesstoken.
    """  
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)
