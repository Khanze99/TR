from typing import AsyncIterator

from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine

engine = create_async_engine('postgresql+asyncpg://user:password@localhost:5432/bookstore')
async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


BaseModel = declarative_base()


async def get_session() -> AsyncIterator[AsyncSession]:
    async with async_session() as session:
        yield session
