from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key= True)
    email = Column(String, unique=True, index=True)
    genger = Column(String)
    age = Column(Integer)
    is_active = Column(Boolean, default=True)
    
    posts = relationship("Post", back_populates="author")
    
class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    content = Column(String)
    date_created = Column(String)
    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship("Author", back_populates="posts")
    