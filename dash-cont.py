from dash import Dash, Output, Input, dcc, html
import dash_bootstrap_components as dbc
import plotly
import random
import plotly.graph_objs as go
from collections import deque

X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(1)

#layout
app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])
app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1000,
            n_intervals = 0
        )
    ]
)

#wrapper and func
@app.callback(Output('live-graph', 'figure'),
        [Input('graph-update', 'n_intervals')])

def update_graph_scatter(n):
    X.append(X[-1]+1)
    Y.append(Y[-1]+Y[-1]*random.uniform(-0.1,0.1))

    data = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Scatter',
            mode= 'lines+markers'
            )

    return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
                                                yaxis=dict(range=[min(Y),max(Y)]),)}

if __name__ == '__main__':
    app.run_server(debug=True)