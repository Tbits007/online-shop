from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyBaseAccessTokenTableUUID,
)
from app.infrastructure.database import Base
from fastapi_users_db_sqlalchemy.generics import GUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey


class AccessToken(SQLAlchemyBaseAccessTokenTableUUID, Base):  
    user_id: Mapped[GUID] = mapped_column(
        GUID,
        ForeignKey("users.id", ondelete="cascade"),
        nullable=False
    )
