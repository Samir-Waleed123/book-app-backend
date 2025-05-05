from fastapi import FastAPI, HTTPException,Depends
import uvicorn
from database import get_db, BookData
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from schemas import BookDataSchema


app = FastAPI()



list_of_items = []


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/books")
async def get_books(db: Session = Depends(get_db)):
    books = db.query(BookData).all()
    return books




@app.post("/books/add")
async def add_book(request : BookDataSchema,db: Session = Depends(get_db)):
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
    
@app.put("/books/update/{book_id}")
async def update_book(book_id: int, request: BookDataSchema, db: Session = Depends(get_db)):
    book = db.query(BookData).filter(BookData.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    for key, value in request.dict().items():
        setattr(book, key, value)
    
    db.commit()
    db.refresh(book)
    return book

@app.delete("/books/delete/{book_id}")
async def delete_book(book_id: str, db: Session = Depends(get_db)):
    book = db.query(BookData).filter(BookData.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db.delete(book)
    db.commit()
    return {"detail": "Book deleted successfully"}

@app.get("/books/{book_id}")
async def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(BookData).filter(BookData.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

