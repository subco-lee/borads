import uuid
from sqlalchemy import UUID, Column, Enum, Integer, String, Text, DateTime, func
from database import Base
import enum

class Rating(enum.Enum):
    perfect= "perfect"
    great= "great"
    not_bad="not_bad"
    bad= "bad"
    worst= "worst"


class Book(Base):
    __tablename__ = "books"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False) 
    title = Column(String(255), index=True)
    content = Column(String(255), nullable=True)
    review= Column(String(255), nullable=True)
    author = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=func.now())
    rating = Column(Enum(Rating), nullable=False)
