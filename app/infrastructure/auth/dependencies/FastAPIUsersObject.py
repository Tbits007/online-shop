import uuid
from fastapi_users import FastAPIUsers
from app.domain.users import Users
from app.infrastructure.auth.dependencies.user_manager import get_user_manager
from app.infrastructure.auth.dependencies.backend import authentication_backend


fastapi_users = FastAPIUsers[Users, uuid.UUID](
    get_user_manager,
    [authentication_backend],
)