from typing import List, Optional
from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: str
    date_created:str
    
    
class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    author_id: int
    
    class Config:
        orm_mode = True


class AuthorBase(BaseModel):
    email: str
    genger: str
    age: int
    is_active: bool


class AuthorCreate(AuthorBase):
    pass

class AuthorUpdate(BaseModel):
    email: Optional[str] = None
    gender: Optional[str] = None
    age: Optional[int] = None
    is_active: Optional[bool] = None


class Author(AuthorBase):
    id: int
    posts: List[Post] = []

    class Config:
        orm_mode = True










