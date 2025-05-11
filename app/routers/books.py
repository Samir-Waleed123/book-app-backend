
from fastapi import HTTPException,Depends,APIRouter,status

from typing import List  # Add this import
from sqlalchemy.orm import Session
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
import os
from dotenv import load_dotenv
from typing import Annotated

from app.database import BookData, get_db
from app.schemas import BookDataSchema
from app.utils import verify_credentials

router= APIRouter(prefix="/books",tags=["Books"])


@router.get("")
async def get_books(db: Session = Depends(get_db)):
    books = db.query(BookData).all()
    return books




@router.post("/add")
async def add_book(request : BookDataSchema,db: Session = Depends(get_db),username: str = Depends(verify_credentials)):
    # Check if the book already exists in the database
    existing_book = db.query(BookData).filter(BookData.title == request.title).first()
    if existing_book:
        raise HTTPException(status_code=400, detail="Book already exists")
    else:
        book = BookData(**request.dict())
        db.add(book)
        db.commit()
        db.refresh(book)
        return book
    
@router.put("/update/{book_id}")
async def update_book(book_id: int, request: BookDataSchema, db: Session = Depends(get_db)):
    book = db.query(BookData).filter(BookData.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    for key, value in request.dict().items():
        setattr(book, key, value)
    
    db.commit()
    db.refresh(book)
    return book

@router.delete("/delete/{book_id}")
async def delete_book(book_id: str, db: Session = Depends(get_db)):
    book = db.query(BookData).filter(BookData.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db.delete(book)
    db.commit()
    return {"detail": "Book deleted successfully"}

@router.get("/{book_id}")
async def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookData).filter(BookData.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
