import dash
import dash_core_components as dcc
import dash_html_components as html
import dash.dependencies as dd
from dash.dependencies import Input, Output, State
import paramak
import dash_daq as daq

# @server.route('/static/<path:path>')
# def serve_static(path):
#     root_dir = os.getcwd()
#     return flask.send_from_directory(os.path.join(root_dir, 'static'), path)

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(
    __name__,
    prevent_initial_callbacks=True,
)

# paramak.BallReactor()
# def generate_input_boxes():

#                     # html.Div(children=[
#     input_boxes = 
    

    # html.H4('Customer Name',style={'display':'inline-block','margin-right':20}),
    # dcc.Input(id='customer-name',type='text',placeholder='',style={'display':'inline-block'}),
            #  ('inboard_tf_leg_radial_thickness', float),
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
        
        # for input_arg in input_variable_names:
        #     input_boxes.append(
    # return input_boxes


app.layout = html.Div(
    children=[
        html.H1(children='Paramak GUI'),
        html.Div([
                html.H4('inboard_tf_leg_radial_thickness', style={'display':'inline-block'}),
                dcc.Input(id='inboard_tf_leg_radial_thickness', value=10,style={'display':'inline-block'}),
                html.Br(),
                html.H4('rotation_angle', style={'display':'inline-block'}),
                dcc.Input(id='rotation_angle',value=16,style={'display':'inline-block'})
            ]),
        # html.Div(id="reactor_viewer"),
        dcc.Loading(
            id="loading-1",
            type="default",
            # children=html.Div(
            #     id="reactor_viewer"
            children=html.Iframe(id='new_reactor_viewer', target='_parent', height=600, width=1000, src="assets/reactor_3d.html")
            # )
        ),
        # html.Iframe(id='new_reactor_viewer', height=600, width=1000, src="assets/reactor_3d.html"),
        html.Button(
            "Update reactor",
            title="Click to update the reactor model with the latest parameters",
            id="reactor_update",
        )
    ]
)

@app.callback(
    Output("new_reactor_viewer", "src"),
    # Output("reactor_viewer", "children"),
    Input("inboard_tf_leg_radial_thickness", "value"),
    Input("rotation_angle", "value"),
)
def update_reactor(inboard_tf_leg_radial_thickness, rotation_angle):
    my_reactor = paramak.BallReactor(
        inboard_tf_leg_radial_thickness=float(inboard_tf_leg_radial_thickness),
        rotation_angle=float(rotation_angle)
    )
    my_reactor.export_html_3d("assets/reactor_3d.html")
    print('new assets/reactor_3d.html')
    return 'new assets/reactor_3d.html'
    # return html.Iframe(id='new_reactor_viewer', height=600, width=1000, src="assets/reactor_3d.html")


# @app.callback(
#     Output("reactor_viewer", "children"),
#     Input("reactor_update", "n_clicks"),
#     State("inboard_tf_leg_radial_thickness", "value"),
#     State("rotation_angle", "value"),
# )
# def clicked_update_reactor(n_clicks, inboard_tf_leg_radial_thickness, rotation_angle):
#     trigger_id = dash.callback_context.triggered[0]["prop_id"].split(".")[0]
#     if trigger_id == "reactor_update":
#         if n_clicks is None or n_clicks==0:
#             raise dash.exceptions.PreventUpdate
#         else:
#             my_reactor = paramak.BallReactor(
#                 inboard_tf_leg_radial_thickness=float(inboard_tf_leg_radial_thickness),
#                 rotation_angle=float(rotation_angle)
#             )
#             my_reactor.export_html_3d("assets/reactor_3d.html")
#             print('new assets/reactor_3d.html')
#             return html.Iframe(id=f'{n_clicks}new_reactor_viewer', height=600, width=1000, src="assets/reactor_3d.html")

# @app.callback(
#     Output("reactor_input_args", "children"),
#     Input("reactor-selector", "value")
# )
# def update_graph_from_mcnp(selected_reactor):
#     if selected_reactor == 'BallReactor':
#         my_reactor = paramak.BallReactor()
#         input_boxes = []


#         for input_arg in input_variable_names:
#             input_boxes.append(
#                 html.Div(children=[
#                     html.P(input_arg[0]),
#                     daq.NumericInput(id=input_arg[0])
#                 ]
#             )
#         )
#         return input_boxes
#     else:
#         return []


if __name__ == '__main__':
    app.run_server(port=8050, host='0.0.0.0', debug=True)