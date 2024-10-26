from typing import Type
from app.domain.users import Users
from app.repositories.base_repo import BaseRepository


class UsersRepository(BaseRepository[Users]):
    model: Type[Users] = Users