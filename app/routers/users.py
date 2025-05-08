from fastapi import HTTPException,Depends,APIRouter,status

from typing import List  # Add this import
from sqlalchemy.orm import Session
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
import os
from dotenv import load_dotenv
from typing import Annotated

from app.database import userBookData, get_db
from app.schemas import BookDataSchema

router= APIRouter(prefix="/users",tags=["users"])


@router.get("/purchase")
async def get_books(emiil:str ,db: Session = Depends(get_db)):
    books = db.query(userBookData).filter(userBookData.email == emiil).all()
    if not books:
        raise HTTPException(status_code=404, detail="Books not found")
    return books

@router.post("/add/purchase")
async def add_book(request : BookDataSchema,db: Session = Depends(get_db)):
    book = BookDataSchema(**request.dict())
    db.add(book)
    db.commit()
    db.refresh(book)
    return book