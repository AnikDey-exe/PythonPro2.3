import numpy as np
import csv
import plotly.express as px

def GDS(DP):
    ICS = []
    CDS = []
    with open(DP) as csv_file:
        c_r = csv.DictReader(csv_file)
        for R in c_r:
            ICS.append(float(R["Coffee in ml"]))
            CDS.append(float(R["sleep in hours"]))
    return {
        "x": ICS,
        "y": CDS
    }

def FC(DS):
    c = np.corrcoef(DS["x"],DS["y"])
    print("Correlation Between Coffee vs Hrs of Sleep: ",c[0,1])

def ST():
    DP = "coffee.csv"
    DS = GDS(DP)
    FC(DS)

ST()