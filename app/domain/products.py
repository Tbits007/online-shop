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
