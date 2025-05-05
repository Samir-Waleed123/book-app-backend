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
    books : list[str]  


