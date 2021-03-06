
import json, os
from utils import make_ballreactor_paramak_object, make_flfsystemcodereactor_paramak_object
import dash

import requests
from dash import dcc, html
from dash.dependencies import Input, Output, State
import string
import random
from dash_daq import NumericInput

from html_layouts_ball_reactor import ball_reactor_geometry_input_args_table, ball_reactor_material_input_args_table, ballreactor_neutronics_parameters
from html_layouts_flf_system_code_reactor import flf_system_code_reactor_geometry_input_args_table, flf_system_code_reactor_material_input_args_table, flf_system_code_reactor_neutronics_parameters

app = dash.Dash(
    __name__,
    # prevent_initial_callbacks=True,
)

server = app.server


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
            "Create 3D fusion reactors and perform neutronics on demand.",
            style={"text-align": "center"},
        ),
        html.H2(
            "This is under development and not fully functional yet.",
            style={"color": "red", "text-align": "center"},
        ),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Div(
            style={"text-align": "center"},
            children=[
                html.H2(
                    "\U0001f449 Select a reactor",
                    style={"width": "300px", "display": "inline-block", "text-align": "center"},
                ),
                dcc.Dropdown(
                    id="reactor_selector",
                    options=[
                        {"label": "BallReactor", "value": "BallReactor"},
                        {
                            "label": "FLF System Code Reactor",
                            "value": "FlfSystemCodeReactor",
                        },
                        # {"label": "Work in progress", "value": "another reactor"},
                    ],
                    # value="",
                    clearable=False,
                    style={"width": "300px", "display": "inline-block", "text-align": "center"},
                ),
            ]
        ),
        dcc.Tabs(
            id="tabs",
            value="geometry",
            children=[
                dcc.Tab(label="Geometry", value="geometry"),
                dcc.Tab(label="Materials", value="materials"),
                dcc.Tab(label="Settings", value="settings"),
            ],
            style={"display": "none"},
        ),
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
                            id="flfsystemcodereactor_geometry_inputs",
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
                    ], style={"width": "75%"}),
                ]),
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
                    id="flfsystemcodereactor_material_inputs",
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
                    children=[
                        html.Div(
                            id="ballreactor_settings_inputs",
                            style={"width": "25%", "display": "none"},
                            children=[
                                html.H2("\U0001f449 Specify neutronics settings"),
                                ballreactor_neutronics_parameters,
                            ],
                        ),
                        html.Div(
                            id="flfsystemcodereactor_settings_inputs",
                            style={"width": "25%", "display": "none"},
                            children=[
                                html.H2("\U0001f449 Specify neutronics settings"),
                                flf_system_code_reactor_neutronics_parameters,
                            ],
                        ),
                    ],
                ),
            ],
        ),
        dcc.Download(id="download-stp"),
        dcc.Download(id="download-stl"),
        dcc.Download(id="download-html"),
        dcc.Download(id="download-ballreactor-stp"),
        dcc.Download(id="download-ballreactor-stl"),
        dcc.Download(id="download-ballreactor-html"),
    ]
)


@app.callback(
    Output("download-stl", "data"),
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
    Input("download_flf_stl_button", "n_clicks"),
    prevent_initial_call=True,
)
def make_stl_for_download(
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
    n_clicks
):

    my_reactor = make_flfsystemcodereactor_paramak_object(
        inner_blanket_radius=inner_blanket_radius,
        blanket_thickness=blanket_thickness,
        blanket_height=blanket_height,
        lower_blanket_thickness=lower_blanket_thickness,
        upper_blanket_thickness=upper_blanket_thickness,
        blanket_vv_gap=blanket_vv_gap,
        upper_vv_thickness=upper_vv_thickness,
        vv_thickness=vv_thickness,
        lower_vv_thickness=lower_vv_thickness,
        rotation_angle=float(flf_rotation_angle),
    )

    my_reactor.export_stl(f"assets/flfsystemcodereactor.stl")
    return dcc.send_file(
        "assets/flfsystemcodereactor.stl"
    )


@app.callback(
    Output("download-ballreactor-stl", "data"),
    State("inner_bore_radial_thickness", "value"),
    State("inboard_tf_leg_radial_thickness", "value"),
    State("center_column_shield_radial_thickness", "value"),
    State("divertor_radial_thickness", "value"),
    State("inner_plasma_gap_radial_thickness", "value"),
    State("plasma_radial_thickness", "value"),
    State("outer_plasma_gap_radial_thickness", "value"),
    State("firstwall_radial_thickness", "value"),
    State("blanket_radial_thickness", "value"),
    State("blanket_rear_wall_radial_thickness", "value"),
    State("plasma_gap_vertical_thickness", "value"),
    State("elongation", "value"),
    State("triangularity", "value"),
    State("divertor_to_tf_gap_vertical_thickness", "value"),
    State("number_of_tf_coils", "value"),
    State("rear_blanket_to_tf_gap", "value"),
    State("pf_coil_radial_thicknesses", "value"),
    State("pf_coil_vertical_thicknesses", "value"),
    State("pf_coil_radial_position", "value"),
    State("pf_coil_vertical_position", "value"),
    State("pf_coil_case_thicknesses", "value"),
    State("outboard_tf_coil_radial_thickness", "value"),
    State("outboard_tf_coil_poloidal_thickness", "value"),
    State("divertor_position", "value"),
    State("rotation_angle", "value"),
    Input("download_ballreactor_stl_button", "n_clicks"),
    prevent_initial_call=True,
)
def make_ballreactor_stl_for_download(
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
    n_clicks
):

    my_reactor = make_ballreactor_paramak_object(
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
    )

    my_reactor.export_stl(f"assets/ballreactor.stl")
    return dcc.send_file(
        "assets/ballreactor.stl"
    )

@app.callback(
    Output("download-ballreactor-html", "data"),
    State("inner_bore_radial_thickness", "value"),
    State("inboard_tf_leg_radial_thickness", "value"),
    State("center_column_shield_radial_thickness", "value"),
    State("divertor_radial_thickness", "value"),
    State("inner_plasma_gap_radial_thickness", "value"),
    State("plasma_radial_thickness", "value"),
    State("outer_plasma_gap_radial_thickness", "value"),
    State("firstwall_radial_thickness", "value"),
    State("blanket_radial_thickness", "value"),
    State("blanket_rear_wall_radial_thickness", "value"),
    State("plasma_gap_vertical_thickness", "value"),
    State("elongation", "value"),
    State("triangularity", "value"),
    State("divertor_to_tf_gap_vertical_thickness", "value"),
    State("number_of_tf_coils", "value"),
    State("rear_blanket_to_tf_gap", "value"),
    State("pf_coil_radial_thicknesses", "value"),
    State("pf_coil_vertical_thicknesses", "value"),
    State("pf_coil_radial_position", "value"),
    State("pf_coil_vertical_position", "value"),
    State("pf_coil_case_thicknesses", "value"),
    State("outboard_tf_coil_radial_thickness", "value"),
    State("outboard_tf_coil_poloidal_thickness", "value"),
    State("divertor_position", "value"),
    State("rotation_angle", "value"),
    Input("download_ballreactor_html_button", "n_clicks"),
    prevent_initial_call=True,
)
def make_ballreactor_html_for_download(
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
    n_clicks
):

    my_reactor = make_ballreactor_paramak_object(
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
    )

    my_reactor.export_html_3d(f"assets/ballreactor.html")
    return dcc.send_file(
        "assets/ballreactor.html"
    )


@app.callback(
    Output("download-html", "data"),
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
    Input("download_flf_html_button", "n_clicks"),
    prevent_initial_call=True,
)
def make_html_for_download(
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
    n_clicks
):
    my_reactor = make_flfsystemcodereactor_paramak_object(
        inner_blanket_radius=inner_blanket_radius,
        blanket_thickness=blanket_thickness,
        blanket_height=blanket_height,
        lower_blanket_thickness=lower_blanket_thickness,
        upper_blanket_thickness=upper_blanket_thickness,
        blanket_vv_gap=blanket_vv_gap,
        upper_vv_thickness=upper_vv_thickness,
        vv_thickness=vv_thickness,
        lower_vv_thickness=lower_vv_thickness,
        rotation_angle=float(flf_rotation_angle),
    )

    my_reactor.export_html_3d(f"assets/flfsystemcodereactor.html")
    return dcc.send_file(
        "assets/flfsystemcodereactor.html"
    )


@app.callback(
    Output("download-stp", "data"),
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
    Input("download_flf_stp_button", "n_clicks"),
    prevent_initial_call=True,
)
def make_stp_for_download(
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
    n_clicks
):

    my_reactor = make_flfsystemcodereactor_paramak_object(
        inner_blanket_radius=inner_blanket_radius,
        blanket_thickness=blanket_thickness,
        blanket_height=blanket_height,
        lower_blanket_thickness=lower_blanket_thickness,
        upper_blanket_thickness=upper_blanket_thickness,
        blanket_vv_gap=blanket_vv_gap,
        upper_vv_thickness=upper_vv_thickness,
        vv_thickness=vv_thickness,
        lower_vv_thickness=lower_vv_thickness,
        rotation_angle=float(flf_rotation_angle),
    )

    my_reactor.export_stp(f"assets/flfsystemcodereactor.stp")
    return dcc.send_file(
        "assets/flfsystemcodereactor.stp"
    )


@app.callback(
    Output("download-ballreactor-stp", "data"),
    State("inner_bore_radial_thickness", "value"),
    State("inboard_tf_leg_radial_thickness", "value"),
    State("center_column_shield_radial_thickness", "value"),
    State("divertor_radial_thickness", "value"),
    State("inner_plasma_gap_radial_thickness", "value"),
    State("plasma_radial_thickness", "value"),
    State("outer_plasma_gap_radial_thickness", "value"),
    State("firstwall_radial_thickness", "value"),
    State("blanket_radial_thickness", "value"),
    State("blanket_rear_wall_radial_thickness", "value"),
    State("plasma_gap_vertical_thickness", "value"),
    State("elongation", "value"),
    State("triangularity", "value"),
    State("divertor_to_tf_gap_vertical_thickness", "value"),
    State("number_of_tf_coils", "value"),
    State("rear_blanket_to_tf_gap", "value"),
    State("pf_coil_radial_thicknesses", "value"),
    State("pf_coil_vertical_thicknesses", "value"),
    State("pf_coil_radial_position", "value"),
    State("pf_coil_vertical_position", "value"),
    State("pf_coil_case_thicknesses", "value"),
    State("outboard_tf_coil_radial_thickness", "value"),
    State("outboard_tf_coil_poloidal_thickness", "value"),
    State("divertor_position", "value"),
    State("rotation_angle", "value"),
    Input("download_ballreactor_stp_button", "n_clicks"),
    prevent_initial_call=True,
)
def make_ballreactor_stp_for_download(
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
    n_clicks
):

    my_reactor = make_ballreactor_paramak_object(
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
    )

    my_reactor.export_stp(f"assets/ballreactor.stp")
    return dcc.send_file(
        "assets/ballreactor.stp"
    )

    
@app.callback(
    [
        Output("tabs", "style"),
        Output("ballreactor_geometry_inputs", "style"),
        Output("flfsystemcodereactor_geometry_inputs", "style"),
        Output("ballreactor_viewer_div", "style"),
        Output("flfreactor_viewer_div", "style"),
        Output("ballreactor_material_inputs", "style"),
        Output("flfsystemcodereactor_material_inputs", "style"),
        Output("ballreactor_settings_inputs", "style"),
        Output("flfsystemcodereactor_settings_inputs", "style"),
    ],
    [Input("reactor_selector", "value"), Input("tabs", "value")],
    prevent_initial_call=True,
)
def render_tab_content(active_reactor, active_tab):
    """
    This callback takes the 'active_tab' property as input, as well as the
    stored graphs, and renders the tab content depending on what the value of
    'active_tab' is.
    """
    on = {"display": "inline-block"}
    off = {"display": "none"}
    input_column_on = {"display": "block"} 
    # input_column_off = {"display": "none"}
    print(active_reactor, active_tab)

    if active_tab is not None:
        if active_reactor == "BallReactor" and active_tab == "geometry":
            return on, on, off, input_column_on, off, off, off, off, off
        if active_reactor == "BallReactor" and active_tab == "materials":
            return on, off, off, off, off, input_column_on, off, off, off
        if active_reactor == "BallReactor" and active_tab == "settings":
            return on, off, off, off, off, off, off, on, off
        if active_reactor == "FlfSystemCodeReactor" and active_tab == "geometry":
            return on, off, on, off, input_column_on, off, off, off, off
        if active_reactor == "FlfSystemCodeReactor" and active_tab == "materials":
            return on, off, off, off, off, off, on, off, off
        if active_reactor == "FlfSystemCodeReactor" and active_tab == "settings":
            return on, off, off, off, off, off, off, off, on
        if active_reactor == "BallReactor":
            return on, on, off, input_column_on, off, off, off, off, off
        if active_reactor == "FlfSystemCodeReactor":
            return on, off, on, off, input_column_on, off, off, off, off
    return f"No tab selected {active_tab}"


@app.callback(
    Output("simulate_flfsystemcodereactor_results", "children"),
    State("results_flfsystemcodereactor_required", "value"),
    State("simulation_flfsystemcodereactor_batches", "value"),
    State("simulation_flfsystemcodereactor_particles", "value"),
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
    Input("simulate_flfsystemcodereactor_button", "n_clicks"),
    prevent_initial_call=True,
)
def clicked_flf_simulate(
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
    n_clicks,
):
    # trigger_id = dash.callback_context.triggered[0]["prop_id"].split(".")[0]
    # if trigger_id == "simulate_flfsystemcodereactor_button":
    #     if n_clicks is None or n_clicks == 0:
    #         raise dash.exceptions.PreventUpdate
    print('triggered')
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
                    f'tbr ={response["TBR"]["result"]} ?? {response["TBR"]["std. dev."]}'
                )
            )

    if "heating" in results_required:
        if simulation_batches == 1:
            children.append(html.H1(f'heating ={response["heating"]["result"]}'))
        else:
            children.append(
                html.H1(
                    f'heating ={response["heating"]["MeV per source particle"]["result"]} ?? {response["heating"]["MeV per source particle"]["std. dev."]} MeV per source particle'
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

    if dash.callback_context.triggered == [{'prop_id': '.', 'value': None}]:

        return html.Iframe(
            src=f"assets/ballreactor_default.html",
            width="100%",
            height="100vh",
            title="Paramak.export_html",
            style={"border": 0, "scrolling": "0", "height": "100vh "},
        )

    my_reactor = make_ballreactor_paramak_object(
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
    )

    # os.system('rm assets/*.html')
    letters = string.ascii_lowercase
    fn = ''.join(random.choice(letters) for i in range(20)) 
    my_reactor.export_html_3d(f"assets/{fn}.html")

    return html.Iframe(
        src=f"assets/{fn}.html",
        width="100%",
        height="100vh",
        title="Paramak.export_html",
        style={"border": 0, "scrolling": "0", "height": "100vh "},
    )



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
    if dash.callback_context.triggered == [{'prop_id': '.', 'value': None}]:

        return html.Iframe(
            src=f"assets/flfsystemcodereactor_default.html",
            width="100%",
            height="100vh",
            title="Paramak.export_html",
            style={"border": 0, "scrolling": "0", "height": "100vh "},
        )

    my_reactor = make_flfsystemcodereactor_paramak_object(
        inner_blanket_radius=inner_blanket_radius,
        blanket_thickness=blanket_thickness,
        blanket_height=blanket_height,
        lower_blanket_thickness=lower_blanket_thickness,
        upper_blanket_thickness=upper_blanket_thickness,
        blanket_vv_gap=blanket_vv_gap,
        upper_vv_thickness=upper_vv_thickness,
        vv_thickness=vv_thickness,
        lower_vv_thickness=lower_vv_thickness,
        rotation_angle=rotation_angle,
    )

    # os.system('rm assets/*.html')
    letters = string.ascii_lowercase
    fn = ''.join(random.choice(letters) for i in range(20)) 
    my_reactor.export_html_3d(f"assets/{fn}.html")

    return html.Iframe(
        src=f"assets/{fn}.html",
        width="100%",
        height="100vh",
        title="Paramak.export_html",
        style={"border": 0, "scrolling": "0", "height": "100vh "},
    )


if __name__ == "__main__":
    app.run_server(
        # debug=True,
        # when setting debug to True then also set dev_tools_hot_reload to
        # false to avoid bug https://github.com/plotly/dash/issues/1293
        # dev_tools_hot_reload=False,
    )
