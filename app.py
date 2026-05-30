import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load data

df = pd.read_csv("output.csv")
df["Date"] = pd.to_datetime(df["Date"])

app = Dash(__name__)

app.layout = html.Div([
    html.H1(
        "Pink Morsel Sales Dashboard",
        style={
            "textAlign": "center",
            "color": "#2c3e50",
            "marginBottom": "20px"
        },
        id="dashboard-header"
    ),

    html.Div([
        html.Label(
            "Select Region:",
            style={
                "fontWeight": "bold",
                "fontSize": "18px"
            }
        ),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"}
            ],
            value="all",
            inline=True
        )
    ],
    style={
        "textAlign": "center",
        "marginBottom": "20px"
    }),

    dcc.Graph(id="sales-chart")
],
style={
    "backgroundColor": "#f4f6f7",
    "padding": "20px"
})

@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    filtered_df = df.copy()

    if selected_region != "all":
        filtered_df = filtered_df[
            filtered_df["Region"].str.lower() == selected_region
        ]

    daily_sales = (
        filtered_df
        .groupby("Date")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Date")
    )

    fig = px.line(
        daily_sales,
        x="Date",
        y="Sales",
        markers=True,
        title=f"Pink Morsel Sales - {selected_region.title()}"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales ($)",
        template="plotly_white"
    )

    fig.add_shape(
    type="line",
    x0="2021-01-15",
    x1="2021-01-15",
    y0=0,
    y1=daily_sales["Sales"].max(),
    line=dict(
        dash="dash",
        width=2
    )
)

    return fig

if __name__ == "__main__":
    app.run(debug=True)
