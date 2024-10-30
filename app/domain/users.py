from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from app.infrastructure.database import Base


class Users(Base, SQLAlchemyBaseUserTableUUID):
    __tablename__ = "users"

