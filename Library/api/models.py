"""This module has neccessary classes
"""
from datetime import date
from pydantic import BaseModel,Field

class BookReq(BaseModel):
    """It has __class_vars__

    Args:
        BaseModel (class): pre-defined class
    """
    title: str = Field(...,description="This Sherlock Holmes mystery involves a secret pact among four convicts",examples=["Beneath Mystery"])
    author: str = Field(...,description="author name",examples=["SRIKANTH"])
    isbn: str = Field(...,description="isbn number",examples=["7569889785"])
    published_date: date

class BookRes(BaseModel):
    """It has __class_vars__

    Args:
        BaseModel (class): pre-defined class
    """
    id: str=Field(...,description="id",examples=["1001"])
    title: str = Field(...,description="This Sherlock Holmes mystery involves a secret pact among four convicts",examples=["Beneath Mystery"])
    author: str = Field(...,description="author name",examples=["SRIKANTH"])
    isbn: str = Field(...,description="isbn number",examples=["7569889785"])
    published_date: date
