from fastapi import FastAPI
from .routers import authors
# from .database import engine, Base


app = FastAPI()        

app.include_router(authors.author_router)

@app.get('/')
def home():
    return "my blog post"