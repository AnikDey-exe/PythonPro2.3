import pandas as pd
import plotly.express as px

df = pd.read_csv("corona.csv")

fig = px.scatter(df, x = "date", y = "cases", color = "country", title = "Corona Cases In Different Countries")
fig.show()