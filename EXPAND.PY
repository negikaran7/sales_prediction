import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Button('Expand', id='expand-button'),
    dcc.Graph(id='graph')
])

@app.callback(
    Output('graph', 'style'),
    [Input('expand-button', 'n_clicks')],
    [State('graph', 'style')]
)
def expand_graph(n_clicks, graph_style):
    if n_clicks is None:
        return graph_style
    elif n_clicks % 2 == 1:
        return {'width': '100vw', 'height': '100vh'}
    else:
        return {'width': '100%', 'height': '500px'}

if __name__ == '__main__':
    app.run_server(debug=True)
