# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
from plotly.express import line
import pandas as pd

app = Dash(__name__)
PATH_NAME = './pink_morsel_data.csv'
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
data = pd.read_csv(PATH_NAME)
data = data.sort_values(by="date")

line_chart = line(data, x="date", y="sales", title='Pink Morsel Sales')

visualization = dcc.Graph(
    id='visualization',
    figure=line_chart
)

header = html.H1(
    "Pink Morsel Visualizer",
    id="header"
)

app.layout = html.Div([
    header,
    visualization
])

if __name__ == '__main__':
    app.run(debug=True)