"""This module has class,function for numeric calucations
"""
from fastapi import FastAPI
from pydantic import BaseModel

class NumericReq(BaseModel):
    """This defines __class-vars__

    Args:
        BaseModel (class): passing pre-defined class
    """
    value_1: int
    value_2: int

class NumericRes(BaseModel):
    """This defines __class-vars__

    Args:
        BaseModel (class): pre-defined class
    """
    value_1: int
    value_2: int
    result: int

app=FastAPI()

@app.get("/")
def hello():
    """simple function

    Returns:
        str: string
    """
    return "Hey! Srikanth"

@app.post("/add",response_model=NumericRes)
def add(request: NumericReq):
    """This function will return addition of 2 values

    Args:
        request (NumericReq): class
    """
    response=NumericRes(
        value_1=request.value_1,
        value_2=request.value_2,
        result=request.value_1 + request.value_2
    )
    return response

@app.post("/sub",response_model=NumericRes)
def sub(request: NumericReq):
    """This function will return subtraction of 2 values

    Args:
        request (NumericReq): class
    """
    response=NumericRes(
        value_1=request.value_1,
        value_2=request.value_2,
        result=request.value_1 - request.value_2
    )
    return response

@app.post("/mul",response_model=NumericRes)
def mul(request: NumericReq):
    """This function will return multiplication of 2 values

    Args:
        request (NumericReq): class
    """
    response=NumericRes(
        value_1=request.value_1,
        value_2=request.value_2,
        result=request.value_1 * request.value_2
    )
    return response

@app.post("/div",response_model=NumericRes)
def div(request: NumericReq):
    """This function will return division of 2 values

    Args:
        request (NumericReq): class
    """
    response=NumericRes(
        value_1=request.value_1,
        value_2=request.value_2,
        result=request.value_1 / request.value_2
    )
    return response

