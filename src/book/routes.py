""" Book routes module """
from fastapi import APIRouter, status, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_session

from .schemas import BookSchema
from .models import BookModel

book_router = APIRouter(
    prefix='/book',
    tags=['book']
)


@book_router.get(
    '/{book_id}',
    description="Информация о книге",
    response_model=BookSchema
)
async def get_book(
        book_id: int,
        session: AsyncSession = Depends(get_session)
):
    results = await session.execute(select(BookModel).filter_by(id=book_id))
    item = results.scalars().first()
    return item


@book_router.post(
    '/create',
    description='Создать запись о книге'
)
async def create_book(): return "OK"


@book_router.delete(
    '/delete',
    description='Удалить запись о книге',
    status_code=status.HTTP_200_OK
)
async def delete_book(): return "OK"
