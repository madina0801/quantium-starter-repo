# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output, callback
from plotly.express import line
import plotly.express as px
import pandas as pd

app = Dash(__name__)
PATH_NAME = './pink_morsel_data.csv'
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
data = pd.read_csv(PATH_NAME)
data = data.sort_values(by="date")

def generate_figure(chart_data):
    line_chart = line(chart_data, x="date", y="sales", title='Pink Morsel Sales')
    return line_chart

visualization = dcc.Graph(
    id='visualization',
    figure=generate_figure(data)
)

header = html.H1(
    "Pink Morsel Visualizer",
    id="header",
    style={
        "color": "#DE0D56",
        "text-align": "center",
    }
)

choose_region = dcc.RadioItems(
    ["north", "south", "east", "west", "all"],
    "north",
    id="choose_region",
    inline=True
)

choose_region_wrap = html.Div(
    [choose_region],
    style={
        "font-size": "120%"
    }
)

@callback(
    Output('visualization', 'figure'),
    Input('choose_region', 'value'))

def update_figure(selected_region):
    if selected_region == "all":
        filtered_data = data
    else:
        filtered_data = data[data.region == selected_region]

    fig = generate_figure(filtered_data)

    return fig

app.layout = html.Div([
    header,
    visualization,
    choose_region
],
    style={
        "border": "20px"
    }
)

if __name__ == '__main__':
    app.run(debug=True)