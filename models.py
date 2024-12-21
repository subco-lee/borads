from sqlalchemy import Column, Integer, String, Text, DateTime, func
from database import Base

class Post(Base):
    __tablename__ = "posts"
    __table_args__ = {'extend_existing': True}  # 기존 테이블 확장

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    content = Column(Text)
    author = Column(String(100))
    created_at = Column(DateTime, default=func.now()) 
