from pydantic import BaseModel


class BookDataSchema(BaseModel):
    title : str
    description : str
    author : str
    imageUrl : str  
    category : str
    rating : float
    price : float
    discount :float
    amount : int
    isBestDeal : bool = False  
    isTopBook : bool = False
    isLatestBook : bool = False
    isUpcomingBook : bool = False


class userBookDataSchema(BaseModel):
    email : str
    books_title : str

class libraryBookSchema(BaseModel):
    bookid : int
    author : str
    title : str

    class Config:
        orm_mode = True  # Enable ORM mode to work with SQLAlchemy models

class borrowBookSchema(BaseModel):
    bookid : int
    email : str


    


