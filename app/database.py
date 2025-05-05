from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

# Database setup
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Sessionlocal = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()

class BookData(Base):
    __tablename__ = 'books_data'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    author = Column(String, nullable=False)
    imageUrl = Column(String)  
    category = Column(String)
    rating = Column(Float)
    price = Column(Float, nullable=False)
    discount = Column(String)  
    amount = Column(Integer)  
    isBestDeal = Column(Boolean, default=False)  
    isTopBook = Column(Boolean, default=False)    
    isLatestBook = Column(Boolean, default=False) 
    isUpcomingBook = Column(Boolean, default=False) 
    created_at = Column(DateTime, default=datetime.utcnow)  

class userBookData(Base):
    __tablename__ = 'user_books_data'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False)
    books = Column(String, nullable=False)  


    
    def __repr__(self):
        return f"<BookData(title='{self.title}', author='{self.author}')>"

def initialize_database():
    Base.metadata.create_all(bind=engine)

# Dependency

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()


if __name__ == "__main__":
    initialize_database()
    print("Database initialized and tables created.")


