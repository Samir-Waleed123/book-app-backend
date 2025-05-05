from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from datetime import datetime

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
    imageUrl = Column(String)  # Consider using 'image_url' for SQL naming conventions
    category = Column(String)
    rating = Column(Float)
    price = Column(Float, nullable=False)
    discount = Column(String)  # Could also be Float if it represents a percentage
    amount = Column(Integer)   # Nullable as per your model
    isBestDeal = Column(Boolean, default=False)  # Consider 'is_best_deal' for SQL conventions
    isTopBook = Column(Boolean, default=False)    # 'is_top_book'
    isLatestBook = Column(Boolean, default=False) # 'is_latest_book'
    isUpcomingBook = Column(Boolean, default=False) # 'is_upcoming_book'
    created_at = Column(DateTime, default=datetime.utcnow)  # Recommended for tracking
    
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


