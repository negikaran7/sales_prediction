import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.io as pio
import base64
import zipfile
import io

app = dash.Dash(__name__)

# Create some sample figures
fig1 = go.Figure(data=go.Scatter(x=[1, 2, 3], y=[4, 5, 6]))
fig2 = go.Figure(data=go.Bar(x=[1, 2, 3], y=[4, 5, 6]))
fig3 = go.Figure(data=go.Pie(labels=['A', 'B', 'C'], values=[4, 5, 6]))

# Define the callback function to handle the download request
@app.callback(
    dash.dependencies.Output('download-button', 'href'),
    dash.dependencies.Input('download-button', 'n_clicks')
)
def download_images(n_clicks):
    if n_clicks is not None:
        # Create a zip file to store the images
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
            # Save each figure as a separate image file in the zip file
            for i, fig in enumerate([fig1, fig2, fig3]):
                image_bytes = pio.to_image(fig, format='png', width=800, height=600)
                zip_file.writestr(f'plot{i+1}.png', image_bytes)

        # Encode the zip file as base64 and return it as a data URI
        zip_data = zip_buffer.getvalue()
        encoded_zip = base64.b64encode(zip_data).decode('utf-8')
        return f'data:application/zip;base64,{encoded_zip}'

# Define the layout
app.layout = html.Div([
    html.H1('Download Multiple Images'),
    html.A('Download All Images', id='download-button', download='images.zip', href='/', target='_blank')
])

if __name__ == '__main__':
    app.run_server(debug=True)
