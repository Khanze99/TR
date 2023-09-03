""" Trade routes module """
from fastapi import APIRouter

trade_router = APIRouter(
    prefix="/trade",
    tags=["trade"]
)


@trade_router.get(
    '/all',
    description="Все сделки"
)
async def trades():
    return []


@trade_router.get(
    '/{trade_id}',
    description="Сделка в деталях"
)
async def trade(trade_id: int):
    return {}


@trade_router.post(
    '/create',
    description="Создать сделку"
)
async def create_trade():
    return {}


@trade_router.post(
    '/{id}/offer',
    description="Предложить сделку"
)
async def create_offer():
    return {}


@trade_router.post(
    '/accept',
    description='Принять сделку'
)
async def accept(): return {}


@trade_router.post(
    "/reject",
    description="Отклонить предложение"
)
async def reject(): return {}
