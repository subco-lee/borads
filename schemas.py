from datetime import datetime
from pydantic import BaseModel

class PostCreate(BaseModel):
    title: str
    content: str
    author: str

    class Config:
        orm_mode = True  # Enable ORM mode to handle SQLAlchemy models

class PostResponse(PostCreate):
    id: int
    created_at: datetime


    class Config:
        orm_mode = True
        arbitrary_types_allowed = True 