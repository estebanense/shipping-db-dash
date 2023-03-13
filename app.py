# app.py

import pandas as pd
from dash import Dash, dcc, html

data = (
    pd.read_csv("shipping.csv")
    .query("Source_Area == 'Collect'")
    .assign(Date=lambda data: pd.to_datetime(data["InvDate"], format="%m/%d/%Y"))
    .sort_values(by="InvDate")
)

print(data)

app = Dash(__name__)