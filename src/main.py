""" main module """
from fastapi import FastAPI

from src.auth.routes import auth_router
from src.trade.routes import trade_router
from src.book.routes import book_router


app = FastAPI(title="TradeBook")
app.include_router(auth_router)
app.include_router(trade_router)
app.include_router(book_router)
