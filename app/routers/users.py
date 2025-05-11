from fastapi import HTTPException,Depends,APIRouter,status

from typing import List  # Add this import
from sqlalchemy.orm import Session
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
import os
from dotenv import load_dotenv
from typing import Annotated

from app.database import userBookData, get_db
from app.schemas import BookDataSchema, userBookDataSchema

router= APIRouter(prefix="/users",tags=["users"])
z

@router.post("/purchase")
async def get_books(email:str ,db: Session = Depends(get_db)):
    books = db.query(userBookData).filter(userBookData.email == email).all()
    if not books:
        raise HTTPException(status_code=404, detail="Books not found")
    return books

@router.post("/add/purchase")
async def add_book(request : userBookDataSchema,db: Session = Depends(get_db)):
    book = userBookData(**request.dict())
    db.add(book)
    db.commit()
    db.refresh(book)
    return book