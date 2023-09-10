from datetime import datetime

from pydantic import BaseModel


class BookSchema(BaseModel):
    id: int
    name: str
    author: str
    created_at: datetime
