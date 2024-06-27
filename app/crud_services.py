from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

# from schema import  author, post
from . import models, schemas

# from app import models,

def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()

def get_authors(db: Session,  offset: int = 0, limit: int = 4 ):
    return db.query(models.Author).offset(offset).limit(limit).all()


def create_author(db: Session, author_payload: schemas.AuthorCreate):
    new_author = models.Author(**author_payload.model_dump())
    db.add(new_author)
    db.commit()
    db.refresh(new_author) 
    return new_author   


def update_author(db: Session, author_id: int, author_update: schemas.AuthorUpdate):
    # author = db.query(models.Author).filter(models.Author.id == author_id).first()
    author = get_author(db, author_id)
    
    # author_update.dict(exclude_unset=True) converts the Pydantic model to a dictionary, excluding any unset (i.e., None) fields. This ensures that only provided fields are updated.
    # convert to dict
    if author:
        update_data = author_update.dict(exclude_unset=True)
        
        # jsonable_encoder is used to convert the author object to a JSON-serializable dictionary. This step is optional and not directly used in the provided code.
        # author_dict = jsonable_encoder(author)
        
        # This loop iterates over the 'update_data' dictionary and updates the corresponding attributes of the author object with new values.
        for key, value in update_data.items():
            setattr(author, key, value)
        db.commit()
        db.refresh(author)
        return author
    return None

def delete_author(db: Session, author_id: int,):
    author = get_author(db, author_id)
    
    db.delete(author)
    db.commit()
    
    return None    


 