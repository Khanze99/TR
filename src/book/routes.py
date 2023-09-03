""" Book routes module """
from fastapi import APIRouter, status

book_router = APIRouter(
    prefix='/book',
    tags=['book']
)


@book_router.get(
    '/{book_id}',
    description="Информация о книге"
)
async def get_book(): return {}


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
