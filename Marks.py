import pandas as pd
import plotly.express as px
import csv
import numpy as np

with open("Marks.csv") as file:
    df = csv.DictReader(file)
    fig = px.scatter(df, x = "Marks", y = "Days")
    fig.show()

def getData(path):
    marksData = []
    daysData = []

    with open(path) as f:
        dataf = csv.DictReader(f)

        for row in dataf:
            marksData.append(float(row["Marks"]))
            daysData.append(float(row["Days"]))

    return {"x": marksData, "y": daysData}

def correlation(data):
    corr = np.corrcoef(data["x"], data["y"])
    print("Correlation is: ", corr[0,1])

def setup():
    dataPath = "Marks.csv"
    data = getData(dataPath)
    correlation(data)

setup()