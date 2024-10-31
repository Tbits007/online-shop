import asyncio
import contextlib
from app.domain.users import Users
from app.infrastructure.auth.dependencies.user_db import get_user_db
from app.infrastructure.auth.dependencies.user_manager import get_user_manager
from app.infrastructure.auth.user_manager import UserManager
from app.infrastructure.database import get_session
from app.schemas.users_schemas import UserCreateSchema
from fastapi_users.exceptions import UserAlreadyExists
from app.infrastructure.database import async_session_maker

# get_async_session_context = contextlib.asynccontextmanager(get_async_session)
get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


default_email = "admin@admin.com"
default_password = "admin"
default_is_active = True
default_is_superuser = True
default_is_verified = True

async def create_user(
    user_manager: UserManager,
    user_create: UserCreateSchema,
) -> Users:
    user = await user_manager.create(
        user_create=user_create,
        safe=False,
    )
    return user


async def create_superuser(     
    email: str = default_email,
    password: str = default_password,
    is_active: bool = default_is_active,
    is_superuser: bool = default_is_superuser,
    is_verified: bool = default_is_verified,
):    
    user_create = UserCreateSchema(
        email=email,
        password=password,
        is_active=is_active,
        is_superuser=is_superuser,
        is_verified=is_verified,
    )
    async with async_session_maker() as session:
        async with get_user_db_context(session) as user_db:
            async with get_user_manager_context(user_db) as user_manager:
                return await create_user(
                    user_manager=user_manager,
                    user_create=user_create,
                )


if __name__ == '__main__':
    asyncio.run(create_superuser())