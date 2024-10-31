from fastapi import APIRouter
from app.infrastructure.auth.dependencies.FastAPIUsersObject import fastapi_users
from app.infrastructure.auth.dependencies.backend import authentication_backend
from app.schemas.users_schemas import UserCreateSchema, UserResponseSchema


router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

# /login & /logout
router.include_router(
    fastapi_users.get_auth_router(authentication_backend),
)

# /register
router.include_router(
    fastapi_users.get_register_router(UserResponseSchema, UserCreateSchema),
)