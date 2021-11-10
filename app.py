import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_core_components as dcc

# @server.route('/static/<path:path>')
# def serve_static(path):
#     root_dir = os.getcwd()
#     return flask.send_from_directory(os.path.join(root_dir, 'static'), path)

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children='Paramak GUI'),
        dcc.Dropdown(
            id='reactor-selector',
            options=[
                {'label': 'BallReactor', 'value': 'NYC'},
                {'label': 'S', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            value='NYC'
        ),
        html.Iframe(height=600, width=1000, src="assets/reactor_3d.html")
    ]
)




if __name__ == '__main__':
    app.run_server(port=8050, host='0.0.0.0')