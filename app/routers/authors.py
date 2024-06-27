from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud_services, schemas
from app.database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)


author_router = APIRouter(prefix="/authors",
    tags=["author"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@author_router.get('/', status_code=status.HTTP_200_OK)
def get_authors(db: Session = Depends(get_db), offset: int = 0, limit: int = 4):
    authors = crud_services.get_authors(db=db, offset=offset, limit=limit)
    return {'message': 'success', 'data': authors}

@author_router.get('/{author_id}', status_code=status.HTTP_200_OK)
def get_author(author_id: int, db: Session = Depends(get_db)):
    author = crud_services.get_author(db, author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return {'message': 'success', 'data': author}

@author_router.post('/', status_code=status.HTTP_201_CREATED)
def create_author(payload: schemas.AuthorCreate, db: Session = Depends(get_db)):
    new_author = crud_services.create_author(db, author_payload= payload)
    return {'message': 'author successfully created '}


@author_router.put('/{author_id}', status_code=status.HTTP_200_OK)
def update_author(author_id: int, update_payload: schemas.AuthorUpdate,  db: Session = Depends(get_db)):
    updated_author = crud_services.update_author(db, author_id, update_payload)
    if updated_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return updated_author

@author_router.delete('/{author_id}', status_code=status.HTTP_202_ACCEPTED)
def delete_author(author_id: int, db: Session = Depends(get_db)):
    author = crud_services.get_author(db, author_id)
    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    crud_services.delete_author(db, author_id)
    
    return {'message': 'Author deleted successfully'}

    
    
    
