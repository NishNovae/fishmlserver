# src/fishmlserver/curl.py

import requests

def get(l, wl, url="http://localhost:8765/fish"):
    headers = {
        'accept': 'application/json',
    }

    params = {
        'length': '10', 
        'weight': '10',
    }

    response = requests.get(url, params=params, headers=headers)
    j = response.json()
    r = j.get("prediction")

    return r
