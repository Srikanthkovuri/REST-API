"""This module describes about Library api 
"""
from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from api.models import BookReq,BookRes
from db.database import get_db,Base,engine
from db.models import Books

Base.metadata.create_all(bind=engine)

app=FastAPI()

@app.get("/")
def hello():
    """_summary_

    Returns:
        _type_: _description_
    """
    return {"messge":"Hello Srikanth"}

@app.get("/books",response_model=list[BookRes])
def get_books(db: Session=Depends(get_db)):
    """This function returns the books

    Args:
        request (BookReq): user-defined class with args
    """
    return db.query(Books).all()
    

@app.post("/books",response_model=BookRes)
def create_book(request: BookReq, db: Session=Depends(get_db)):
    """This function creates a book by taking inputs from user

    Args:
        request (BookReq): user-defined class with args
    """
    db_books=Books(**request.model_dump())
    db.add(db_books)
    db.commit()
    db.refresh(db_books)
    return db_books
