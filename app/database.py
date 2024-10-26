from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker  
from sqlalchemy.orm import DeclarativeBase
from app.config import settings
from typing import AsyncGenerator

engine = create_async_engine(settings.DATABASE_URL)
async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

        
class Base(DeclarativeBase):
    pass