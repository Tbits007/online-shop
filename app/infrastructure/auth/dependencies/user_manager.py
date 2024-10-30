from fastapi import Depends
from app.infrastructure.auth.user_manager import UserManager
from app.infrastructure.auth.dependencies.user_db import get_user_db


async def get_user_manager(user_db=Depends(get_user_db)):
    """
    Получение объекта для управления объектами модели Users.
    """
    yield UserManager(user_db)