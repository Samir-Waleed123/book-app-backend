from fastapi import FastAPI, Depends
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from app.routers import books, users, library
from app.utils import verify_credentials



app = FastAPI()


app.include_router(books.router)
app.include_router(users.router)
app.include_router(library.router)




list_of_items = []


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Book API"}

@app.post("/login")
async def login(username: str = Depends(verify_credentials)):
    return {"message": f"Welcome {username}!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)

