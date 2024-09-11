"""This is simple hello restapi
"""
from fastapi import FastAPI
#from pydantic import BaseModel

app=FastAPI()

@app.get("/")
def hello():
    """Function returns simple msg
    """
    return {"message": "Hello Srikanth"}
