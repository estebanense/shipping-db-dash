# app.py

import pandas as pd
from dash import Dash, dcc, html

data = (
    pd.read_csv("shipping.csv")
    .query("type == 'Collect' and R_City =='BENTONVILLE' ")
    .assign(Date=lambda data: pd.to_datetime(data["Date"], format="%m/%d/%Y"))
    .sort_values(by="Date")
)

print(data)

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Shipping Analytics"),
        html.P(
            children=(
                "Analyze the behavior of shiping costs"
                " between years ..."
            ),
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["neto"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "neto"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["Pub"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Pub"},
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)