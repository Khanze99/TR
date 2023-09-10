from datetime import datetime

from src.database import BaseModel

from sqlalchemy import Integer, Column, String, DateTime


class BookModel(BaseModel):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    author = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
