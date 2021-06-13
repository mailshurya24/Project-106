import pandas as pd
import plotly.express as px
import csv
import numpy as np

with open("Sleep.csv") as file:
    df = csv.DictReader(file)
    fig = px.scatter(df, x = "coffee", y = "sleep")
    fig.show()

def getData(path):
    coffData = []
    sleepData = []

    with open(path) as f:
        dataf = csv.DictReader(f)

        for row in dataf:
            coffData.append(float(row["coffee"]))
            sleepData.append(float(row["sleep"]))

    return {"x": coffData, "y": sleepData}

def correlation(data):
    corr = np.corrcoef(data["x"], data["y"])
    print("Correlation is: ", corr[0,1])

def setup():
    dataPath = "Sleep.csv"
    data = getData(dataPath)
    correlation(data)

setup()