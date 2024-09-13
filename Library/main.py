"""This module describes about Library api 
"""
from datetime import date
from fastapi import FastAPI
from api.models import BookReq,BookRes

app=FastAPI()

@app.get("/")
def hello():
    """_summary_

    Returns:
        _type_: _description_
    """
    return {"messge":"Hello Srikanth"}

@app.get("/books",response_model=list[BookRes])
def get_books(request:BookReq):
    """This function returns the books

    Args:
        request (BookReq): user-defined class with args
    """
    response=[]
    response.append(BookRes(
        id='101',
        title='Bhagvadgita',
        author="Srikanth",
        isbn="7569889785",
        published_date=date.today()
    ))
    return response

@app.post("/books",response_model=BookRes)
def create_book(request: BookReq):
    """This function creates a book by taking inputs from user

    Args:
        request (BookReq): user-defined class with args
    """
    return BookRes(
        id="1001",
        title=request.title,
        author=request.author,
        isbn=request.isbn,
        published_date=request.published_date
    )
