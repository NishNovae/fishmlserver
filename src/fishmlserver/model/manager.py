# src/fishmlserver/model/manager.py
import os

def get_model_path():
    this_path = os.path.abspath(__file__)
    dir_path = os.path.dirname(this_path)
    model_path = dir_path + "/model.pkl" 

    print(f"this_path: {this_path}")
    print(f"dir_path: {dir_path}")
    print(f"model_path: {model_path}")

    return model_path
# debug
#get_model_path()
