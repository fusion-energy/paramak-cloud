
import json

import dash
import dash_vtk
import paramak
import requests
import vtk
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dash_vtk.utils import to_mesh_state


app = dash.Dash(
    __name__,
    # prevent_initial_callbacks=True,
)

server = app.server


ball_reactor_geometry_input_args_table = html.Table(
    [
        html.Tr(
            [
                html.Td("inner_bore_radial_thickness"),
                html.Td(
                    dcc.Input(
                        id="inner_bore_radial_thickness",
                        value=10,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("inboard_tf_leg_radial_thickness"),
                html.Td(
                    dcc.Input(
                        id="inboard_tf_leg_radial_thickness",
                        value=30,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("center_column_shield_radial_thickness"),
                html.Td(
                    dcc.Input(
                        id="center_column_shield_radial_thickness",
                        value=60,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("divertor_radial_thickness"),
                html.Td(
                    dcc.Input(
                        id="divertor_radial_thickness",
                        value=150,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("inner_plasma_gap_radial_thickness"),
                html.Td(
                    dcc.Input(
                        id="inner_plasma_gap_radial_thickness",
                        value=30,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("plasma_radial_thickness"),
                html.Td(
                    dcc.Input(
                        id="plasma_radial_thickness",
                        value=300,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("outer_plasma_gap_radial_thickness"),
                html.Td(
                    dcc.Input(
                        id="outer_plasma_gap_radial_thickness",
                        value=30,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("plasma_gap_vertical_thickness"),
                html.Td(
                    dcc.Input(
                        id="plasma_gap_vertical_thickness",
                        value=50,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("firstwall_radial_thickness"),
                html.Td(
                    dcc.Input(
                        id="firstwall_radial_thickness",
                        value=30,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("blanket_radial_thickness"),
                html.Td(
                    dcc.Input(
                        id="blanket_radial_thickness",
                        value=50,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("blanket_rear_wall_radial_thickness"),
                html.Td(
                    dcc.Input(
                        id="blanket_rear_wall_radial_thickness",
                        value=30,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("elongation"),
                html.Td(
                    dcc.Input(
                        id="elongation",
                        value=2.0,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("triangularity"),
                html.Td(
                    dcc.Input(
                        id="triangularity",
                        value=0.55,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("divertor_to_tf_gap_vertical_thickness"),
                html.Td(
                    dcc.Input(
                        id="divertor_to_tf_gap_vertical_thickness",
                        value=0,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("number_of_tf_coils"),
                html.Td(
                    dcc.Input(
                        id="number_of_tf_coils",
                        value=12,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("rear_blanket_to_tf_gap"),
                html.Td(
                    dcc.Input(
                        id="rear_blanket_to_tf_gap",
                        value="",
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("pf_coil_radial_thicknesses"),
                html.Td(
                    dcc.Input(
                        id="pf_coil_radial_thicknesses",
                        value="",
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("pf_coil_vertical_thicknesses"),
                html.Td(
                    dcc.Input(
                        id="pf_coil_vertical_thicknesses",
                        value="",
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("pf_coil_radial_position"),
                html.Td(
                    dcc.Input(
                        type="text",
                        id="pf_coil_radial_position",
                        value="",
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("pf_coil_vertical_position"),
                html.Td(
                    dcc.Input(
                        type="text",
                        id="pf_coil_vertical_position",
                        value="",
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("pf_coil_case_thicknesses"),
                html.Td(
                    dcc.Input(
                        id="pf_coil_case_thicknesses",
                        value="",
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("outboard_tf_coil_radial_thickness"),
                html.Td(
                    dcc.Input(
                        id="outboard_tf_coil_radial_thickness",
                        value="",
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("outboard_tf_coil_poloidal_thickness"),
                html.Td(
                    dcc.Input(
                        id="outboard_tf_coil_poloidal_thickness",
                        value="",
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("divertor_position"),
                html.Td(
                    dcc.Dropdown(
                        id="divertor_position",
                        options=[
                            {"label": "lower", "value": "lower"},
                            {"label": "upper", "value": "upper"},
                            {"label": "both", "value": "both"},
                        ],
                        value="lower",
                        clearable=False,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("rotation_angle"),
                html.Td(
                    dcc.Input(
                        id="rotation_angle",
                        value=180,
                    )
                ),
            ]
        ),
    ],
)

flf_system_code_reactor_geometry_input_args_table = html.Table(
    [
        html.Tr(
            [
                html.Td("inner_blanket_radius"),
                html.Td(
                    dcc.Input(
                        id="inner_blanket_radius",
                        value=100,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("blanket_thickness"),
                html.Td(
                    dcc.Input(
                        id="blanket_thickness",
                        value=70,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("blanket_height"),
                html.Td(
                    dcc.Input(
                        id="blanket_height",
                        value=500,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("lower_blanket_thickness"),
                html.Td(
                    dcc.Input(
                        id="lower_blanket_thickness",
                        value=50,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("upper_blanket_thickness"),
                html.Td(
                    dcc.Input(
                        id="upper_blanket_thickness",
                        value=40,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("blanket_vv_gap"),
                html.Td(
                    dcc.Input(
                        id="blanket_vv_gap",
                        value=20,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("upper_vv_thickness"),
                html.Td(
                    dcc.Input(
                        id="upper_vv_thickness",
                        value=10,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("vv_thickness"),
                html.Td(
                    dcc.Input(
                        id="vv_thickness",
                        value=10,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("lower_vv_thickness"),
                html.Td(
                    dcc.Input(
                        id="lower_vv_thickness",
                        value=10,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("rotation_angle"),
                html.Td(
                    dcc.Input(
                        id="flf_rotation_angle",
                        value=180,
                    )
                ),
            ]
        ),
    ],
)


ball_reactor_material_input_args_table = html.Table(
    # Header
    [
        html.Tr(
            [
                html.Td("first wall armour material"),
                html.Td(
                    dcc.Input(
                        id="mat_first_wall_armour",
                        value="tungsten",
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("first wall material"),
                html.Td(
                    dcc.Input(
                        id="mat_first_wall",
                        value="eurofer",
                    )
                ),
            ]
        ),
    ]
)

flf_system_code_reactor_material_input_args_table = html.Table(
    # Header
    [
        html.Tr(
            [
                html.Td("breeder material"),
                html.Td(
                    dcc.Input(
                        id="blanket_material",
                        value="Li",
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("Li enrichment"),
                html.Td(
                    dcc.Input(
                        id="lithium_enrichment",
                        value=7.59,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("vessel material"),
                html.Td(
                    dcc.Dropdown(
                        id="vessel_material",
                        options=[
                            {"label": "P91 steel", "value": "P91"},
                            {"label": "Iron", "value": "Iron"},
                        ],
                        value="P91",
                        clearable=False,
                    )
                ),
            ]
        ),
    ]
)

neutronics_parameters = html.Table(
    # Header
    [
        html.Tr(
            [
                html.Td("batches"),
                html.Td(
                    dcc.Input(
                        id="simulation_batches",
                        value=10,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("particles per batch"),
                html.Td(
                    dcc.Input(
                        id="simulation_particles",
                        value=1000,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("results required"),
                html.Td(
                    dcc.Dropdown(
                        options=[
                            {"label": "TBR", "value": "tbr"},
                            {"label": "blanket heating", "value": "heating"},
                            {"label": "DPA - not implemented yet", "value": "dpa"},
                            {"label": "dose maps - not implemented yet", "value": "dose_maps"},
                            {"label": "dose vtk - not implemented yet", "value": "dose_vtk"},
                        ],
                        value=["tbr"],
                        multi=True,
                        id="results_required",
                    )
                ),
            ]
        ),
    ]
)

app.layout = html.Div(
    [
        html.Iframe(
            src="https://ghbtns.com/github-btn.html?user=fusion-energy&repo=paramak-cloud&type=star&count=true&size=large",
            width="170",
            height="30",
            title="GitHub",
            style={"border": 0, "scrolling": "0"},
        ),
        html.H1("Paramak GUI", style={"text-align": "center"}),
        html.H2(
            "Create 3D fusion reactor models and perform neutronics simulations on demand.",
            style={"text-align": "center"},
        ),
        html.H2(
            "This webpage is under development and not fully functional yet.",
            style={"color": "red", "text-align": "center"},
        ),
        html.H2(
            "\U0001f449 Select a reactor",
            style={"width": "300px", "display": "inline-block"},
        ),
        dcc.Dropdown(
            id="reactor_selector",
            options=[
                {"label": "BallReactor", "value": "BallReactor"},
                {
                    "label": "FLF System Code Reactor",
                    "value": "FlfSystemCodeReactor",
                },
                {"label": "Work in progress", "value": "another reactor"},
            ],
            value="FlfSystemCodeReactor",
            clearable=False,
            style={"width": "300px", "display": "inline-block"},
        ),
        dcc.Tabs(
            id="tabs",
            value="geometry",
            children=[
                dcc.Tab(label="Geometry", value="geometry"),
                dcc.Tab(label="Materials", value="materials"),
                dcc.Tab(label="Settings", value="settings"),
            ],
        ),
        # html.Div(id='tabs-content-example-graph'),
        html.Div(
            id="geometry-tab",
            # style={"display": "none"},
            children=[
                html.Tr([
                    html.Td([
                        html.Div(
                            id="ballreactor_geometry_inputs",
                            style={"display": "none"},
                            children=[
                                html.H2("\U0001f449 Input geometric parameters"),
                                ball_reactor_geometry_input_args_table,
                            ],
                        ),
                        html.Div(
                            id="flfsystemcodereactorreactor_geometry_inputs",
                            style={"display": "none"},
                            children=[
                                html.H2("\U0001f449 Input geometric parameters"),
                                flf_system_code_reactor_geometry_input_args_table,
                            ],
                        ),
                    ], style={"width": "25%", "vertical-align": "top"}),
                    html.Td([
                        html.Div(
                            dcc.Loading(
                                id="ballreactor_viewer",
                                type="default",
                            ),
                            id="ballreactor_viewer_div",
                            style={"display": "none"},
                        ),
                        html.Div(
                            dcc.Loading(
                                id="flfreactor_viewer",
                                type="default",
                            ),
                            id="flfreactor_viewer_div",
                            style={"display": "none"},
                        ),
                    ], style={"width": "75%"})
                ])
                    # html.Button(
                    #     "Download reactor CAD files",
                    #     title="Click to dowload STL and STP files of the reactor",
                    #     id="download_button",
                    # ),
            ],
        ),
        html.Div(
            id="materials-div",
            # style={"display": "none"},
            children=[
                html.Div(
                    id="ballreactor_material_inputs",
                    style={"width": "25%", "display": "none"},
                    children=[
                        html.H2("\U0001f449 Select materials"),
                        ball_reactor_material_input_args_table,
                    ],
                ),
                html.Div(
                    id="flfsystemcodereactorreactor_material_inputs",
                    style={"width": "25%", "display": "none"},
                    children=[
                        html.H2("\U0001f449 Select materials"),
                        flf_system_code_reactor_material_input_args_table,
                    ],
                ),
            ],
        ),
        html.Div(
            id="settings-div",
            # style={"display": "none"},
            children=[
                html.Div(
                    id="settings_inputs",
                    style={"width": "25%", "display": "none"},
                    children=[
                        html.H2("\U0001f449 Specify neutronics settings"),
                        neutronics_parameters,
                        html.Br(),
                        html.Button(
                            "Simulate reactor",
                            title="Click to start a neutronics simulation",
                            id="simulate_button",
                        ),
                        html.Br(),
                        html.Br(),
                        html.A(
                            "Link to simulation API",
                            href="https://tgkubvki8f.execute-api.eu-west-2.amazonaws.com/flf_neutronics_api",
                            target="_blank",
                        ),
                        dcc.Loading(
                            id="simulate_results",
                            type="default",
                        ),
                    ],
                ),
            ],
        ),
    ]
)


@app.callback(
    [
        Output("ballreactor_geometry_inputs", "style"),
        Output("flfsystemcodereactorreactor_geometry_inputs", "style"),
        Output("ballreactor_viewer_div", "style"),
        Output("flfreactor_viewer_div", "style"),
        Output("ballreactor_material_inputs", "style"),
        Output("flfsystemcodereactorreactor_material_inputs", "style"),
        Output("settings_inputs", "style"),
    ],
    [Input("reactor_selector", "value"), Input("tabs", "value")],
)
def render_tab_content(active_reactor, active_tab):
    """
    This callback takes the 'active_tab' property as input, as well as the
    stored graphs, and renders the tab content depending on what the value of
    'active_tab' is.
    """
    on = {"display": "inline-block"}
    off = {"display": "none"}
    input_column_on = {"display": "block"} #"width": "70%", 
    input_column_off = {"display": "none"}
    print(active_reactor, active_tab)
    if active_tab is not None:
        if active_reactor == "BallReactor" and active_tab == "geometry":
            return on, off, input_column_on, off, off, off, off
        if active_reactor == "BallReactor" and active_tab == "materials":
            print('active_reactor == "BallReactor" and active_tab=="materials"')
            return off, off, off, off, input_column_on, off, off
        if active_reactor == "BallReactor" and active_tab == "settings":
            return off, off, off, off, off, off, on
        if active_reactor == "FlfSystemCodeReactor" and active_tab == "geometry":
            return off, on, off, input_column_on, off, off, off
        if active_reactor == "FlfSystemCodeReactor" and active_tab == "materials":
            return off, off, off, off, off, on, off
        if active_reactor == "FlfSystemCodeReactor" and active_tab == "settings":
            return off, off, off, off, off, off, on
    return f"No tab selected {active_tab}"


# https://dash.plotly.com/dash-core-components/dropdown
# https://community.plotly.com/t/create-and-download-zip-file/53704
# https://stackoverflow.com/questions/67917360/plotly-dash-download-bytes-stream/67918580#67918580
# html.Button(
#     "Download reactor CAD files",
#     title="Click to dowload STL and STP files of the reactor",
#     id="download_button",
# ),
# dcc.Download(id="download_files"),
# html.Button(
#     "Simulate reactor",
#     title="Click to perform an OpenMC simulation of the reactor",
#     id="reactor_update",
# ),


# @app.callback(
#     Output("download_files", "data"),
#     Input("download_button", "n_clicks"),
#     prevent_initial_call=True,
# )
# def clicked_download(n_clicks):
#     def write_archive(bytes_io):
#         with open("assets/reactor_3d.stl", 'rb') as fh:
#             buf = io.BytesIO(fh.read())
#     return dcc.send_bytes(write_archive, "some_name.zip")
#    return send_file("assets/reactor_3d.stl", as_attachment=True)


@app.callback(
    Output("simulate_results", "children"),
    Input("simulate_button", "n_clicks"),
    State("results_required", "value"),
    State("simulation_batches", "value"),
    State("simulation_particles", "value"),
    State("inner_blanket_radius", "value"),
    State("blanket_thickness", "value"),
    State("blanket_height", "value"),
    State("lower_blanket_thickness", "value"),
    State("upper_blanket_thickness", "value"),
    State("blanket_vv_gap", "value"),
    State("upper_vv_thickness", "value"),
    State("vv_thickness", "value"),
    State("lower_vv_thickness", "value"),
    State("flf_rotation_angle", "value"),
    State("blanket_material", "value"),
    State("lithium_enrichment", "value"),
    State("vessel_material", "value"),
    prevent_initial_call=True,
)
def clicked_simulate(
    n_clicks,
    results_required,
    simulation_batches,
    simulation_particles,
    inner_blanket_radius,
    blanket_thickness,
    blanket_height,
    lower_blanket_thickness,
    upper_blanket_thickness,
    blanket_vv_gap,
    upper_vv_thickness,
    vv_thickness,
    lower_vv_thickness,
    flf_rotation_angle,
    blanket_material,
    lithium_enrichment,
    vessel_material,
):
    trigger_id = dash.callback_context.triggered[0]["prop_id"].split(".")[0]
    if trigger_id == "simulate_button":
        if n_clicks is None or n_clicks == 0:
            raise dash.exceptions.PreventUpdate

    payload = {
        "results_required": ','.join(results_required),
        "simulation_batches": simulation_batches,
        "simulation_particles": simulation_particles,
        "inner_blanket_radius": inner_blanket_radius,
        "blanket_thickness": blanket_thickness,
        "blanket_height": blanket_height,
        "lower_blanket_thickness": lower_blanket_thickness,
        "upper_blanket_thickness": upper_blanket_thickness,
        "blanket_vv_gap": blanket_vv_gap,
        "upper_vv_thickness": upper_vv_thickness,
        "vv_thickness": vv_thickness,
        "lower_vv_thickness": lower_vv_thickness,
        "rotation_angle": flf_rotation_angle,
        "blanket_material": blanket_material,
        "lithium_enrichment": lithium_enrichment,
        "vessel_material": vessel_material,
    }

    session = requests.Session()

    # form the request from the URL and arguments
    url = "https://tgkubvki8f.execute-api.eu-west-2.amazonaws.com/flf_neutronics_api/simulate"
    response = requests.get(url, params=payload, headers=session.headers).json()

    # converts the response to json and prints to terminal
    print(json.dumps(response, indent=4, sort_keys=True))

    children = []
    print("results_required", results_required)
    print("response", response)
    if "tbr" in results_required:
        if simulation_batches == 1:
            children.append(html.H1(f'tbr ={response["TBR"]["result"]}'))
        else:
            children.append(
                html.H1(
                    f'tbr ={response["TBR"]["result"]} ± {response["TBR"]["std. dev."]}'
                )
            )

    if "heating" in results_required:
        if simulation_batches == 1:
            children.append(html.H1(f'heating ={response["heating"]["result"]}'))
        else:
            children.append(
                html.H1(
                    f'heating ={response["heating"]["MeV per source particle"]["result"]} ± {response["heating"]["MeV per source particle"]["std. dev."]} MeV per source particle'
                )
            )

    return children


@app.callback(
    Output("ballreactor_viewer", "children"),
    # Output("ballreactor_viewer_div", "style")],
    Input("inner_bore_radial_thickness", "value"),
    Input("inboard_tf_leg_radial_thickness", "value"),
    Input("center_column_shield_radial_thickness", "value"),
    Input("divertor_radial_thickness", "value"),
    Input("inner_plasma_gap_radial_thickness", "value"),
    Input("plasma_radial_thickness", "value"),
    Input("outer_plasma_gap_radial_thickness", "value"),
    Input("firstwall_radial_thickness", "value"),
    Input("blanket_radial_thickness", "value"),
    Input("blanket_rear_wall_radial_thickness", "value"),
    Input("plasma_gap_vertical_thickness", "value"),
    Input("elongation", "value"),
    Input("triangularity", "value"),
    Input("divertor_to_tf_gap_vertical_thickness", "value"),
    Input("number_of_tf_coils", "value"),
    Input("rear_blanket_to_tf_gap", "value"),
    Input("pf_coil_radial_thicknesses", "value"),
    Input("pf_coil_vertical_thicknesses", "value"),
    Input("pf_coil_radial_position", "value"),
    Input("pf_coil_vertical_position", "value"),
    Input("pf_coil_case_thicknesses", "value"),
    Input("outboard_tf_coil_radial_thickness", "value"),
    Input("outboard_tf_coil_poloidal_thickness", "value"),
    Input("divertor_position", "value"),
    Input("rotation_angle", "value"),
    # prevent_initial_call=True
)
def update_ballreactor(
    inner_bore_radial_thickness,
    inboard_tf_leg_radial_thickness,
    center_column_shield_radial_thickness,
    divertor_radial_thickness,
    inner_plasma_gap_radial_thickness,
    plasma_radial_thickness,
    outer_plasma_gap_radial_thickness,
    firstwall_radial_thickness,
    blanket_radial_thickness,
    blanket_rear_wall_radial_thickness,
    plasma_gap_vertical_thickness,
    elongation,
    triangularity,
    divertor_to_tf_gap_vertical_thickness,
    number_of_tf_coils,
    rear_blanket_to_tf_gap,
    pf_coil_radial_thicknesses,
    pf_coil_vertical_thicknesses,
    pf_coil_radial_position,
    pf_coil_vertical_position,
    pf_coil_case_thicknesses,
    outboard_tf_coil_radial_thickness,
    outboard_tf_coil_poloidal_thickness,
    divertor_position,
    rotation_angle,
):
    # trigger_id = dash.callback_context.triggered[0]["prop_id"].split(".")[0]
    # if trigger_id == "reactor_update":
    #     if n_clicks is None or n_clicks == 0:
    #         raise dash.exceptions.PreventUpdate
    # else:
    if pf_coil_radial_thicknesses == "":
        pf_coil_radial_thicknesses = None
    else:
        pf_coil_radial_thicknesses = [
            float(val) for val in str(pf_coil_radial_thicknesses).split(",")
        ]

    if pf_coil_vertical_thicknesses == "":
        pf_coil_vertical_thicknesses = None
    else:
        pf_coil_vertical_thicknesses = [
            float(val) for val in str(pf_coil_vertical_thicknesses).split(",")
        ]

    if pf_coil_radial_position == "":
        pf_coil_radial_position = None
    else:
        pf_coil_radial_position = [
            float(val) for val in str(pf_coil_radial_position).split(",")
        ]

    if pf_coil_vertical_position == "":
        pf_coil_vertical_position = None
    else:
        pf_coil_vertical_position = [
            float(val) for val in str(pf_coil_vertical_position).split(",")
        ]

    if pf_coil_case_thicknesses == "":
        pf_coil_case_thicknesses = None
    else:
        pf_coil_case_thicknesses = [
            float(val) for val in str(pf_coil_case_thicknesses).split(",")
        ]

    if rear_blanket_to_tf_gap == "":
        rear_blanket_to_tf_gap = None

    if outboard_tf_coil_radial_thickness == "":
        outboard_tf_coil_radial_thickness = None

    if outboard_tf_coil_poloidal_thickness == "":
        outboard_tf_coil_poloidal_thickness = None

    my_reactor = paramak.BallReactor(
        inner_bore_radial_thickness=float(inner_bore_radial_thickness),
        inboard_tf_leg_radial_thickness=float(inboard_tf_leg_radial_thickness),
        center_column_shield_radial_thickness=float(
            center_column_shield_radial_thickness
        ),
        divertor_radial_thickness=float(divertor_radial_thickness),
        inner_plasma_gap_radial_thickness=float(inner_plasma_gap_radial_thickness),
        plasma_radial_thickness=float(plasma_radial_thickness),
        outer_plasma_gap_radial_thickness=float(outer_plasma_gap_radial_thickness),
        blanket_radial_thickness=float(blanket_radial_thickness),
        blanket_rear_wall_radial_thickness=float(blanket_rear_wall_radial_thickness),
        plasma_gap_vertical_thickness=float(plasma_gap_vertical_thickness),
        elongation=float(elongation),
        triangularity=float(triangularity),
        firstwall_radial_thickness=float(firstwall_radial_thickness),
        divertor_to_tf_gap_vertical_thickness=float(
            divertor_to_tf_gap_vertical_thickness
        ),
        number_of_tf_coils=float(number_of_tf_coils),
        rear_blanket_to_tf_gap=rear_blanket_to_tf_gap,
        outboard_tf_coil_radial_thickness=outboard_tf_coil_radial_thickness,
        outboard_tf_coil_poloidal_thickness=outboard_tf_coil_poloidal_thickness,
        rotation_angle=float(rotation_angle),
        divertor_position=divertor_position,
        pf_coil_radial_thicknesses=pf_coil_radial_thicknesses,
        pf_coil_vertical_thicknesses=pf_coil_vertical_thicknesses,
        pf_coil_radial_position=pf_coil_radial_position,
        pf_coil_vertical_position=pf_coil_vertical_position,
        pf_coil_case_thicknesses=pf_coil_case_thicknesses,
    )
    # my_reactor.export_html_3d("assets/reactor_3d.html")
    my_reactor.export_stl("assets/reactor_3d.stl")

    # demo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # head_vti = os.path.join(
    #     demo_dir, "paramak-cloud", "assets", "reactor_3d.stl"
    # )

    # Load dataset from dist
    reader = vtk.vtkSTLReader()
    reader.SetFileName("assets/reactor_3d.stl")
    reader.Update()

    # sets colors
    # colors = vtk.vtkNamedColors()
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor((1, 0, 0))
    # actor.GetProperty().SetDiffuse(0.8)
    # actor.GetProperty().SetDiffuseColor(colors.GetColor3d('LightSteelBlue'))
    # actor.GetProperty().SetSpecular(0.3)
    # actor.GetProperty().SetSpecularPower(60.0)

    background = [0.9, 0.9, 1.0]  # 1,1,1, is white

    mesh_state = to_mesh_state(reader.GetOutput())

    vtk_view = dash_vtk.View(
        dash_vtk.GeometryRepresentation(
            dash_vtk.Mesh(state=mesh_state),
        ),
        # cameraViewUp=[0,0,0],
        # cameraPosition=[1000,-1000,-1000],
        background=background,
    )

    return html.Div(
        id="reactor_viewer",
        # children=[html.Div(vtk_view)]
        # style={"height": "calc(80vh - 16px)", "width": "75%"},
        style={"height": "calc(65vh - 16px)", "width": "75%"},
        children=html.Div(vtk_view, style={"height": "100%", "width": "100%"}),
    )  # , {"width": "75%", "display": "inline-block"}


@app.callback(
    Output("flfreactor_viewer", "children"),
    # Output("flfreactor_viewer_div", "style")],
    Input("inner_blanket_radius", "value"),
    Input("blanket_thickness", "value"),
    Input("blanket_height", "value"),
    Input("lower_blanket_thickness", "value"),
    Input("upper_blanket_thickness", "value"),
    Input("blanket_vv_gap", "value"),
    Input("upper_vv_thickness", "value"),
    Input("vv_thickness", "value"),
    Input("lower_vv_thickness", "value"),
    Input("flf_rotation_angle", "value"),
    # prevent_initial_call=True
)
def update_flfreactor(
    inner_blanket_radius,
    blanket_thickness,
    blanket_height,
    lower_blanket_thickness,
    upper_blanket_thickness,
    blanket_vv_gap,
    upper_vv_thickness,
    vv_thickness,
    lower_vv_thickness,
    rotation_angle,
):

    print("updating flf")
    my_reactor = paramak.FlfSystemCodeReactor(
        inner_blanket_radius=float(inner_blanket_radius),
        blanket_thickness=float(blanket_thickness),
        blanket_height=float(blanket_height),
        lower_blanket_thickness=float(lower_blanket_thickness),
        upper_blanket_thickness=float(upper_blanket_thickness),
        blanket_vv_gap=float(blanket_vv_gap),
        upper_vv_thickness=float(upper_vv_thickness),
        vv_thickness=float(vv_thickness),
        lower_vv_thickness=float(lower_vv_thickness),
        rotation_angle=float(rotation_angle),
    )
    # my_reactor.export_html_3d("assets/reactor_3d.html")
    my_reactor.export_stl("assets/reactor_3d.stl")

    # demo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # head_vti = os.path.join(
    #     demo_dir, "paramak-cloud", "assets", "reactor_3d.stl"
    # )

    # Load dataset from dist
    reader = vtk.vtkSTLReader()
    reader.SetFileName("assets/reactor_3d.stl")
    reader.Update()

    # sets colors
    # colors = vtk.vtkNamedColors()
    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(reader.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetColor((1, 0, 0))
    # actor.GetProperty().SetDiffuse(0.8)
    # actor.GetProperty().SetDiffuseColor(colors.GetColor3d('LightSteelBlue'))
    # actor.GetProperty().SetSpecular(0.3)
    # actor.GetProperty().SetSpecularPower(60.0)

    background = [0.9, 0.9, 1.0]

    mesh_state = to_mesh_state(reader.GetOutput())

    vtk_view = dash_vtk.View(
        dash_vtk.GeometryRepresentation(
            dash_vtk.Mesh(state=mesh_state),
        ),
        # cameraViewUp=[0,0,0],
        # cameraPosition=[1000,-1000,-1000],
        background=background,
    )

    return html.Div(
        id="reactor_viewer",
        # children=[html.Div(vtk_view)]
        # style={"height": "calc(80vh - 16px)", "width": "75%"},
        style={"height": "calc(65vh - 16px)", "width": "75%"},
        children=html.Div(vtk_view, style={"height": "100%", "width": "100%"}),
    )  # , {"width": "75%", "display": "inline-block"}


if __name__ == "__main__":
    app.run_server(
        debug=True,
        # when setting debug to True then also set dev_tools_hot_reload to
        # false to avoid bug https://github.com/plotly/dash/issues/1293
        dev_tools_hot_reload=False,
    )
