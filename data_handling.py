import pandas as pd
import numpy as np

def photoPath_from_name(name: str):
    students = pd.read_csv('static/data/students.csv')
    photoPath = students[(students["name"]== name)]["photo"].to_list()[0]
    return "static/data/" + photoPath

if __name__=="__main__":
    print(photoPath_from_name("Larson Elda"))
