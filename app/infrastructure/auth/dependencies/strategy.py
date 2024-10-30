from fastapi import Depends
from app.infrastructure.auth.dependencies.access_token_db import get_access_token_db
from app.infrastructure.auth.models import AccessToken
from fastapi_users.authentication.strategy.db import AccessTokenDatabase, DatabaseStrategy
from app.infrastructure.config import settings


def get_database_strategy(
    access_token_db: AccessTokenDatabase[AccessToken] = Depends(get_access_token_db),
) -> DatabaseStrategy:
    """
    Получение адаптера для работы со всей таблицей access token.
    """
    return DatabaseStrategy(access_token_db, lifetime_seconds=settings.access_token.lifetime_seconds)