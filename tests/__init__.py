import uuid
from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column
from app.infrastructure.database import Base
from sqlalchemy.dialects.postgresql import UUID


class Categories(Base):
    __tablename__ = "categories"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str]

from sqlalchemy import text, ForeignKey, Numeric, Enum
from sqlalchemy.orm import Mapped, mapped_column
from app.infrastructure.database import Base
from sqlalchemy.dialects.postgresql import UUID
import datetime
import uuid
import enum


class Status(enum.Enum):
    shipped = "shipped"
    delivered = "delivered"
    pending = "pending"


class Orders(Base):
    __tablename__ = "orders"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id", ondelete='CASCADE'))
    status: Mapped[Status] = mapped_column(Enum(Status), nullable=False)
    product_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("products.id", ondelete='CASCADE'))
    total_price: Mapped[float] = mapped_column(Numeric)
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from app.infrastructure.database import Base


class Users(Base, SQLAlchemyBaseUserTableUUID):
    __tablename__ = "users"

import uuid
from sqlalchemy import text, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column
from app.infrastructure.database import Base
from sqlalchemy.dialects.postgresql import UUID


class Products(Base):
    __tablename__ = "products"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    name: Mapped[str]
    description: Mapped[str]
    price: Mapped[float] = mapped_column(Numeric)
    currency: Mapped[str]
    stock: Mapped[int]
    category_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("categories.id", ondelete='CASCADE'))
