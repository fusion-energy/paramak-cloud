import dash
import dash_core_components as dcc
import dash_html_components as html
import dash.dependencies as dd
from dash.dependencies import Input, Output
import paramak
import dash_daq as daq

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
                {'label': 'EuDemoFrom2015PaperDiagram', 'value': 'EuDemoFrom2015PaperDiagram'},
                {'label': 'BallReactor', 'value': 'BallReactor'},
                {'label': 'SubmersionTokamak', 'value': 'SubmersionTokamak'},
                {'label': 'SingleNullSubmersionTokamak', 'value': 'SingleNullSubmersionTokamak'},
                {'label': 'SingleNullBallReactor', 'value': 'SingleNullBallReactor'},
                {'label': 'SegmentedBlanketBallReactor', 'value': 'SegmentedBlanketBallReactor'},
                {'label': 'CenterColumnStudyReactor', 'value': 'CenterColumnStudyReactor'},
                {'label': 'SparcFrom2020PaperDiagram', 'value': 'SparcFrom2020PaperDiagram'},
                {'label': 'IterFrom2020PaperDiagram', 'value': 'IterFrom2020PaperDiagram'},
                {'label': 'FlfSystemCodeReactor', 'value': 'FlfSystemCodeReactor'},
            ],
            value='NYC'
        ),
        html.Div(id="reactor_input_args"),
        html.Iframe(id='reactor_viewer', height=600, width=1000, src="assets/reactor_3d.html"),
        html.Button(
            "Update reactor",
            title="Click to update the reactor model with the latest parameters",
            id="reactor_update",
        )
    ]
)

@app.callback(
    Output("reactor_viewer", "src"),
    Input("mcnp_download_button", "n_clicks"),
)
def clicked_update_reactor(n_clicks):
    trigger_id = dash.callback_context.triggered[0]["prop_id"].split(".")[0]
    if trigger_id == "mcnp_download_button":
        if n_clicks is None:
            raise dash.exceptions.PreventUpdate
        else:
            global mcnp_downloaded_data
            if len(mcnp_downloaded_data) > 0:
                download_dict = make_download_dict(mcnp_downloaded_data)
                return download_dict


@app.callback(
    Output("reactor_input_args", "children"),
    Input("reactor-selector", "value")
)
def update_graph_from_mcnp(selected_reactor):
    if selected_reactor == 'BallReactor':
        my_reactor = paramak.BallReactor()
        input_boxes = []

        input_variable_names = [
            ('inner_bore_radial_thickness', float),
            ('inboard_tf_leg_radial_thickness', float),
            # 'center_column_shield_radial_thickness',
            # 'divertor_radial_thickness',
            # 'inner_plasma_gap_radial_thickness',
            # 'plasma_radial_thickness',
            # 'outer_plasma_gap_radial_thickness',
            # 'firstwall_radial_thickness',
            # 'blanket_radial_thickness',
            # 'blanket_rear_wall_radial_thickness',
            # # 'elongation',
            # # 'triangularity',
            # 'plasma_gap_vertical_thickness',
            # 'divertor_to_tf_gap_vertical_thickness',
            # 'number_of_tf_coils',
            # 'rear_blanket_to_tf_gap',
            # 'pf_coil_radial_thicknesses',
            # 'pf_coil_vertical_thicknesses',
            # 'pf_coil_radial_position',
            # 'pf_coil_vertical_position',
            # 'pf_coil_case_thicknesses',
            # 'outboard_tf_coil_radial_thickness',
            # 'outboard_tf_coil_poloidal_thickness',
            # 'divertor_position',
            # 'rotation_angle',
        ]
        for input_arg in input_variable_names:
            input_boxes.append(
                html.Div(children=[
                    html.P(input_arg[0]),
                    daq.NumericInput(id=input_arg[0])
                ]
            )
        )
        return input_boxes
    else:
        return []


if __name__ == '__main__':
    app.run_server(port=8050, host='0.0.0.0', debug=True)