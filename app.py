import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

df = pd.read_csv("output.csv")

df["Date"] = pd.to_datetime(df["Date"])

daily_sales = df.groupby("Date")["Sales"].sum().reset_index()

daily_sales = daily_sales.sort_values("Date")

fig = px.line(
    daily_sales,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales ($)"
)

app = Dash(__name__)

app.layout = html.Div([
    html.H1(
        "Impact of Pink Morsel Price Increase on Sales",
        style={"textAlign": "center"}
    ),

    dcc.Graph(
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)