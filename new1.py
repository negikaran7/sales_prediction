from dash import Dash, callback, Input, Output, State, dcc, html, ALL
import plotly.express as px
import plotly.graph_objects as go

import io
from base64 import standard_b64decode, b64decode, b64encode

def fig_to_data(fig: go.Figure, filename: str="plot.html") -> dict:
    buffer = io.StringIO()
    fig.write_html(buffer)
    html_bytes = buffer.getvalue().encode()
    content = b64encode(html_bytes).decode()
    return {
        "base64": True,
        "content": content,
        "type": "text/html",
        "filename": filename
    }


app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id={"type": 'graph', "index": 0}, figure=px.scatter(px.data.iris(), x='sepal_width', y='sepal_length', color='species')),
    dcc.Graph(id={"type": 'graph', "index": 1}, figure=px.scatter(px.data.iris(), x='petal_length', y='petal_width', color='species')),
    html.Button('Download All', id='download-button'),
    *[
        dcc.Download(id={"type": 'download', "index": i}) for i in range(2)
    ]
])

@callback(
    Output({"type": "download", "index": ALL}, "data"),
    [
        Input("download-button", "n_clicks"),
        State({"type": "graph", "index": ALL}, "figure")
    ],
    prevent_initial_call=True
)
def download_figure(n_clicks, figs):
    return [
        fig_to_data(go.Figure(fig), filename=f"plot_{idx}.html") for idx, fig in enumerate(figs)
    ]

if __name__ == "__main__":
    app.run_server(debug=False, host="127.0.0.1", port=8181)
