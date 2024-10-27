import uuid
from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column
from app.infrastructure.database import Base
from sqlalchemy.dialects.postgresql import UUID


class Users(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] 
    address: Mapped[str]
