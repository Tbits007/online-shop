import uuid
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column
from app.infrastructure.database import Base
from sqlalchemy.dialects.postgresql import UUID


class Users(Base, SQLAlchemyBaseUserTableUUID):
    __tablename__ = "users"

