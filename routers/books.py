from typing import Annotated
import uuid
from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Book, Rating
from database import get_db
from datetime import datetime
from pydantic import BaseModel, Field


router = APIRouter()

class BookCreateRequest(BaseModel):
    title: str = Field(max_length=255)
    author: str = Field(max_length=100)
    content: str | None = Field(max_length=255)
    rating: Rating
    review: str | None = Field(max_length=255)

class BookResponse(BookCreateRequest):
    id: uuid.UUID
    created_at: datetime


@router.get("/books", response_model=list[BookResponse])
def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()

@router.post("/books", response_model=BookResponse)
def create_post(book: Annotated[BookCreateRequest, Body()], db: Session = Depends(get_db)):
    db_post = Book(
        title=book.title, 
        content=book.content,
        review=book.review,
        rating=book.rating,
        author=book.author
        )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@router.get("/books/{book_id}", response_model=BookResponse)
def read_post(book_id: int, db: Session = Depends(get_db)):
    db_post = db.query(Book).filter(Book.id == book_id).first()

    if db_post is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_post
