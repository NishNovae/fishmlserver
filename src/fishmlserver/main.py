# src/fishmlserv/main.py

from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "world"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/fish")
def fish(length: float, weight: float):
    prediction = "dunno"

    if length > 30.0:
        prediction = "domi"
    else:
        prediction = "bingeoh"

    return {
        "prediction": prediction,
        "length": length, 
        "weight": weight
    }


