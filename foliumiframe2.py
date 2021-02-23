import dash 
import plotly.graph_objects as go # or plotly.express as px
import folium
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from urllib.request import urlopen
import json
import pandas as pd
import plotly.express as px
import numpy as np 
from dash.dependencies import Input, Output
import plotly.graph_objs as go


app = dash.Dash()

app.layout = html.Div([
    html.H1('My first app with folium map'),
    html.Iframe(id='map', srcDoc=open('Map16.html', 'r').read(), width='100%', height='600'),
    html.Button(id='map-submit-button', n_clicks=0, children='Submit')
])


@app.callback(
    dash.dependencies.Output('map', 'srcDoc'),
    [dash.dependencies.Input('map-submit-button', 'n_clicks')])
def update_map(n_clicks):
    if n_clicks is None:
        return dash.no_update
    else:
        return open('Map16.html', 'r').read()


if __name__ == '__main__':
    app.run_server(debug=True)