# src/fishmlserv/main.py

from typing import Union
from fastapi import FastAPI
import pickle
from fishmlserver.model.manager import get_model_path

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

    with open(get_model_path()) as f:
        fish_model = pickle.load(f)

    prediction = fish_model.predict([[length, weight]])

    fish_class = "빙어"
    if prediction[0] == 1:
        fish_class = "도미"

    #debug
    print(f"prediction: {fish_class}")

    return {
        "prediction": prediction,
        "length": length, 
        "weight": weight
    }

