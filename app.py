import os
import io
import dash
import dash.dependencies as dd
# import dash_core_components as dcc
# import dash_daq as daq
# import dash_html_components as html

from dash import dcc
# import dash_daq as daq

import dash_vtk
import paramak
import vtk
from dash import html
from dash.dependencies import Input, Output, State
from dash_vtk.utils import to_mesh_state, to_volume_state
from flask import send_file

app = dash.Dash(
    __name__,
    # prevent_initial_callbacks=True,
)

server = app.server


input_args_table = html.Table(
            #Header
            [
                # html.Tr(
                #     [
                #         html.Th('\U0001f449 Input geometric parameters')
                #     ]
                # ),
                html.Tr(
                    [
                        html.Td('inner_bore_radial_thickness'),
                        html.Td(
                            dcc.Input(
                                id="inner_bore_radial_thickness",
                                value=10,
                            )
                        )
                    ]
                ),
                html.Tr(
                    [
                        html.Td('inboard_tf_leg_radial_thickness'),
                        html.Td(
                            dcc.Input(
                                id="inboard_tf_leg_radial_thickness",
                                value=30,
                            )
                        )
                    ]
                ),
                html.Tr(
                    [
                        html.Td('center_column_shield_radial_thickness'),
                        html.Td(
                            dcc.Input(
                                id="center_column_shield_radial_thickness",
                                value=60,
                            )
                        )
                    ]
                ),
                html.Tr(
                    [
                        html.Td('divertor_radial_thickness'),
                        html.Td(
                            dcc.Input(
                                id="divertor_radial_thickness",
                                value=150,
                            )
                        )
                    ]
                ),
                html.Tr(
                    [
                        html.Td('inner_plasma_gap_radial_thickness'),
                        html.Td(
                            dcc.Input(
                                id="inner_plasma_gap_radial_thickness",
                                value=30,
                            )
                        )
                    ]
                ),
                html.Tr(
                    [
                        html.Td('plasma_radial_thickness'),
                        html.Td(
                            dcc.Input(
                                id="plasma_radial_thickness",
                                value=300,
                            )
                        )
                    ]
                ),
                html.Tr(
                    [
                        html.Td('outer_plasma_gap_radial_thickness'),
                        html.Td(
                            dcc.Input(
                                id="outer_plasma_gap_radial_thickness",
                                value=30,
                            )
                        )
                    ]
                ),
                html.Tr(
                    [
                        html.Td('plasma_gap_vertical_thickness'),
                        html.Td(
                            dcc.Input(
                                id="plasma_gap_vertical_thickness",
                                value=50,
                            )
                        )
                    ]
                ),
                html.Tr(
                    [
                        html.Td('firstwall_radial_thickness'),
                        html.Td(
                            dcc.Input(
                                id="firstwall_radial_thickness",
                                value=30,
                            )
                        )
                    ]
                ),
                html.Tr(
                    [
                        html.Td('blanket_radial_thickness'),
                        html.Td(
                            dcc.Input(
                                id="blanket_radial_thickness",
                                value=50,
                            )
                        )
                    ]
                ),
                html.Tr(
                    [
                        html.Td('blanket_rear_wall_radial_thickness'),
                        html.Td(
                            dcc.Input(
                                id="blanket_rear_wall_radial_thickness",
                                value=30,
                            )
                        )
                    ]
                ),
                html.Tr(
                    [
                        html.Td('divertor_to_tf_gap_vertical_thickness'),
                        html.Td(
                            dcc.Input(
                                id="divertor_to_tf_gap_vertical_thickness",
                                value=0,
                            )
                        )
                    ]
                ),
                html.Tr(
                    [
                        html.Td('number_of_tf_coils'),
                        html.Td(
                            dcc.Input(
                                id="number_of_tf_coils",
                                value=12,
                            )
                        )
                    ]
                ),
                html.Tr(
                    [
                        html.Td('rear_blanket_to_tf_gap'),
                        html.Td(
                            dcc.Input(
                                id="rear_blanket_to_tf_gap",
                                value='',
                            )
                        )
                    ]
                ),
                html.Tr(
                    [
                        html.Td('pf_coil_radial_thicknesses'),
                        html.Td(
                            dcc.Input(
                                id="pf_coil_radial_thicknesses",
                                value='',
                            )
                        )
                    ]
                ),
                html.Tr(
                    [
                        html.Td('pf_coil_vertical_thicknesses'),
                        html.Td(
                            dcc.Input(
                                id="pf_coil_vertical_thicknesses",
                                value='',
                            )
                        )
                    ]
                ),
                html.Tr(
                    [
                        html.Td('pf_coil_radial_position'),
                        html.Td(
                            dcc.Input(
                                type='text',
                                id="pf_coil_radial_position",
                                value='',
                            )
                        )
                    ]
                ),
                html.Tr(
                    [
                        html.Td('pf_coil_vertical_position'),
                        html.Td(
                            dcc.Input(
                                type='text',
                                id="pf_coil_vertical_position",
                                value='',
                            )
                        )
                    ]
                ),
                html.Tr(
                    [
                        html.Td('pf_coil_case_thicknesses'),
                        html.Td(
                            dcc.Input(
                                id="pf_coil_case_thicknesses",
                                value='',
                            )
                        )
                    ]
                ),
                html.Tr(
                    [
                        html.Td('outboard_tf_coil_radial_thickness'),
                        html.Td(
                            dcc.Input(
                                id="outboard_tf_coil_radial_thickness",
                                value='',
                            )
                        )
                    ]
                ),
                html.Tr(
                    [
                        html.Td('outboard_tf_coil_poloidal_thickness'),
                        html.Td(
                            dcc.Input(
                                id="outboard_tf_coil_poloidal_thickness",
                                value='',
                            )
                        )
                    ]
                ),
                html.Tr(
                    [
                        html.Td('divertor_position'),
                        html.Td(
                            dcc.Dropdown(
                                id="divertor_position",
                                options=[
                                    {'label': 'lower', 'value': 'lower'},
                                    {'label': 'upper', 'value': 'upper'},
                                    {'label': 'both', 'value': 'both'}
                                ],
                                value='lower',
                                clearable=False
                            )
                        )
                    ]
                ),
                html.Tr(
                    [
                        html.Td('rotation_angle'),
                        html.Td(
                            dcc.Input(
                                id="rotation_angle",
                                value=180,
                            )
                        )
                    ]
                ),
            ],
        )

material_parameters = html.Table(
            #Header
            [
                html.Tr(
                    [
                        html.Td('first wall armour material'),
                        html.Td(
                            dcc.Input(
                                id="mat_first_wall_armour",
                                value='tungsten',
                            )
                        )
                    ]
                ),
                html.Tr(
                    [
                        html.Td('first wall material'),
                        html.Td(
                            dcc.Input(
                                id="mat_first_wall",
                                value='eurofer',
                            )
                        )
                    ]
                ),
            ]
)

neutronics_parameters = html.Table(
            #Header
            [
                html.Tr(
                    [
                        html.Td('batches'),
                        html.Td(
                            dcc.Input(
                                id="neutronics_batches",
                                value=10,
                            )
                        )
                    ]
                ),
                html.Tr(
                    [
                        html.Td('particles per batch'),
                        html.Td(
                            dcc.Input(
                                id="neutronics_particles_per_batch",
                                value=1000,
                            )
                        )
                    ]
                ),
                html.Tr(
                    [
                        html.Td('tallies required'),
                        html.Td(
                            dcc.Dropdown(
                                options=[
                                    {'label': 'TBR', 'value': 'tbr'},
                                    {'label': 'blanket heating', 'value': 'blanket_heating'},
                                    {'label': 'dose maps', 'value': 'dose_maps'},
                                    {'label': 'dose vtk', 'value': 'dose_vtk'}
                                ],
                                value=[],
                                multi=True
                            )
                        )
                    ]
                ),
            ]
)

app.layout = html.Div(
    children=[
        html.Iframe(
            src="https://ghbtns.com/github-btn.html?user=fusion-energy&repo=paramak&type=star&count=true&size=large",
            width="170",
            height="30",
            title="GitHub",
            style={"border": 0, "scrolling": "0"},
        ),
        html.H1("Paramak GUI", style={"text-align":"center"}),
        html.H2("Create 3D fusion reactor models and perform neutronics simulations on demand.", style={"text-align":"center"}),
        html.H2("This webpage is under development and not fully functional yet.", style={"color":"red", "text-align":"center"}),
        html.H2("\U0001f449 Select a reactor"),
        # html.H2("Select a reactor \U0001f449"),
        dcc.Dropdown(
            id="reactor_seclector",
            options=[
                {'label': 'BallReactor', 'value': 'BallReactor'},
                {'label': 'Work in progress', 'value': 'upper'},
                {'label': 'Work in progress', 'value': 'both'}
            ],
            value='BallReactor',
            clearable=False,
            style={'width': '50%'}
        ),
        html.H2('\U0001f449 Input geometric parameters'),
        html.Div(
            input_args_table,
            style={'width': '25%', 'display': 'inline-block'}
        ),
        html.Div(
            dcc.Loading(
                id="reactor_viewer",
                type="default",
            ),
            style={'width': '75%', 'display': 'inline-block'}
        ),
        html.Button(
            "Download reactor CAD files",
            title="Click to dowload STL and STP files of the reactor",
            id="download_button",
        ),
        html.Br(),
        html.Br(),
        html.H2('\U0001f449 Select materials'),
        material_parameters,
        html.Br(),
        html.Br(),
        html.H2('\U0001f449 Specify neutronics settings'),
        neutronics_parameters,
        html.Button(
            "Simulate reactor",
            title="Click to start a neutronics simulation",
            id="simulate_button",
        ),
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

    ]
)


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
    Output("reactor_viewer", "children"),
    Input("inner_bore_radial_thickness", "value"),
    Input("inboard_tf_leg_radial_thickness", "value"),
    Input("center_column_shield_radial_thickness", "value"),
    Input('blanket_radial_thickness', "value"),
    Input('blanket_rear_wall_radial_thickness', "value"),
    Input('plasma_gap_vertical_thickness', "value"),
    Input('divertor_to_tf_gap_vertical_thickness', "value"),
    Input('number_of_tf_coils', "value"),
    Input('rear_blanket_to_tf_gap', "value"),
    Input('pf_coil_radial_thicknesses', "value"),
    Input('pf_coil_vertical_thicknesses', "value"),
    Input('pf_coil_radial_position', "value"),
    Input('pf_coil_vertical_position', "value"),
    Input('pf_coil_case_thicknesses', "value"),
    Input('outboard_tf_coil_radial_thickness', "value"),
    Input('outboard_tf_coil_poloidal_thickness', "value"),
    Input('divertor_position', "value"),
    Input('rotation_angle', "value")
)

# def update_reactor(n_clicks, inboard_tf_leg_radial_thickness, rotation_angle):
def update_reactor(
    inner_bore_radial_thickness,
    inboard_tf_leg_radial_thickness,
    center_column_shield_radial_thickness,
    blanket_radial_thickness,
    blanket_rear_wall_radial_thickness,
    plasma_gap_vertical_thickness,
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
    if pf_coil_radial_thicknesses == '':
        pf_coil_radial_thicknesses=None
    else:
        pf_coil_radial_thicknesses = [float(val) for val in str(pf_coil_radial_thicknesses).split(',')]
        
    if pf_coil_vertical_thicknesses == '':
        pf_coil_vertical_thicknesses=None
    else:
        pf_coil_vertical_thicknesses = [float(val) for val in str(pf_coil_vertical_thicknesses).split(',')]
    
    if pf_coil_radial_position == '':
        pf_coil_radial_position=None
    else:
        pf_coil_radial_position = [float(val) for val in str(pf_coil_radial_position).split(',')]
    
    if pf_coil_vertical_position == '':
        pf_coil_vertical_position=None
    else:
        pf_coil_vertical_position = [float(val) for val in str(pf_coil_vertical_position).split(',')]
    
    if pf_coil_case_thicknesses == '':
        pf_coil_case_thicknesses=None
    else:
        pf_coil_case_thicknesses = [float(val) for val in str(pf_coil_case_thicknesses).split(',')]

    if rear_blanket_to_tf_gap == '':
        rear_blanket_to_tf_gap = None

    if outboard_tf_coil_radial_thickness == '':
        outboard_tf_coil_radial_thickness = None

    if outboard_tf_coil_poloidal_thickness == '':
        outboard_tf_coil_poloidal_thickness = None

    my_reactor = paramak.BallReactor(
        inner_bore_radial_thickness=float(inner_bore_radial_thickness),
        inboard_tf_leg_radial_thickness=float(inboard_tf_leg_radial_thickness),
        center_column_shield_radial_thickness=float(center_column_shield_radial_thickness),
        blanket_radial_thickness=float(blanket_radial_thickness),
        blanket_rear_wall_radial_thickness=float(blanket_rear_wall_radial_thickness),
        plasma_gap_vertical_thickness=float(plasma_gap_vertical_thickness),
        divertor_to_tf_gap_vertical_thickness=float(divertor_to_tf_gap_vertical_thickness),
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
    actor.GetProperty().SetColor((1,0,0))
    # actor.GetProperty().SetDiffuse(0.8)
    # actor.GetProperty().SetDiffuseColor(colors.GetColor3d('LightSteelBlue'))
    # actor.GetProperty().SetSpecular(0.3)
    # actor.GetProperty().SetSpecularPower(60.0)

    background = [1,1,1]

    mesh_state = to_mesh_state(reader.GetOutput())

    vtk_view = dash_vtk.View(
        dash_vtk.GeometryRepresentation(
            dash_vtk.Mesh(state=mesh_state),
        ),
        # cameraViewUp=[0,0,0],
        # cameraPosition=[1000,-1000,-1000],
        background=background
    )

    return html.Div(
        id="reactor_viewer",
        # children=[html.Div(vtk_view)]
        # style={"height": "calc(80vh - 16px)", "width": "75%"},
        style={"height": "calc(65vh - 16px)", "width": "75%"},
        children=html.Div(
            vtk_view, style={"height": "100%", "width": "100%"}
        )
    )


if __name__ == "__main__":
    app.run_server(
        debug=True,
        # # https://github.com/plotly/dash/issues/1293
        dev_tools_hot_reload=False
    )
