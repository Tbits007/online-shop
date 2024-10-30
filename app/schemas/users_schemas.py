import uuid
from fastapi_users import schemas


class UserCreateSchema(schemas.BaseUserCreate):
    pass


class UserUpdateSchema(schemas.BaseUserUpdate):
    pass


class UserResponseSchema(schemas.BaseUser[uuid.UUID]):
    pass
