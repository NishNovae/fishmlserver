# src/fishmlserv/main.py

from typing import Union
from fastapi import FastAPI
import pickle
from fishmlserver.model.manager import get_model_path

import fire

def fish(length: float, weight: float):
    prediction = "dunno"

    with open(get_model_path(), "rb") as f:
        fish_model = pickle.load(f)

    prediction = fish_model.predict([[length, weight]])

    fish_class = "빙어"
    if prediction[0] == 1:
        fish_class = "도미"

    #print(f"prediction: {fish_class}")

    return {
        "prediction": fish_class,
        "length": length, 
        "weight": weight
    }

def run_fish():
    fire.Fire(fish)

def model_path():
    fire.Fire(get_model_path())
