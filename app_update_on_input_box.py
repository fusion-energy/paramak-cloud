import os

import dash
import dash.dependencies as dd
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
import dash_vtk
import paramak
import vtk
from dash import html
from dash.dependencies import Input, Output, State
from dash_vtk.utils import to_mesh_state, to_volume_state


app = dash.Dash(
    __name__,
    # prevent_initial_callbacks=True,
)

server = app.server


app.layout = html.Div(
    children=[
        html.H1(children="Paramak GUI"),
        html.Table(
            #Header
            [
                html.Tr(
                    [
                        html.Th('Geometric parameters')
                    ]
                ),
                html.Tr(
                    [
                        html.Td('inboard_tf_leg_radial_thickness'),
                        html.Td(
                            dcc.Input(
                                id="inboard_tf_leg_radial_thickness",
                                value=10,
                                style={"display": "inline-block"},
                            )
                        )
                    ]
                ),
                html.Tr(
                    [
                        html.Td('1'),
                        html.Td('1')
                    ]
                ),
            ],
        ),
        html.Div(
            [
                html.H4(
                    "inboard_tf_leg_radial_thickness", style={"display": "inline-block"}
                ),
                # dcc.Input(
                #     id="inboard_tf_leg_radial_thickness",
                #     value=10,
                #     style={"display": "inline-block"},
                # ),
                html.Br(),
                html.H4("rotation_angle", style={"display": "inline-block"}),
                dcc.Input(
                    id="rotation_angle", value=180, style={"display": "inline-block"}
                ),
            ]
        ),
        html.Button(
            "Simulate reactor",
            title="Click to perform an OpenMC simulation of the reactor",
            id="reactor_update",
        ),
        dcc.Loading(
            id="reactor_viewer",
            type="default",
        ),
    ]
)


@app.callback(
    Output("reactor_viewer", "children"),
    # Output("reactor_viewer", "children"),
    Input("inboard_tf_leg_radial_thickness", "value"),
    Input("rotation_angle", "value"),
    # Input("reactor_update", "n_clicks"),
    # State("inboard_tf_leg_radial_thickness", "value"),
    # State("rotation_angle", "value"),
)

# def update_reactor(n_clicks, inboard_tf_leg_radial_thickness, rotation_angle):
def update_reactor(inboard_tf_leg_radial_thickness, rotation_angle):
    # trigger_id = dash.callback_context.triggered[0]["prop_id"].split(".")[0]
    # if trigger_id == "reactor_update":
    #     if n_clicks is None or n_clicks == 0:
    #         raise dash.exceptions.PreventUpdate
        # else:
    my_reactor = paramak.BallReactor(
        inboard_tf_leg_radial_thickness=float(inboard_tf_leg_radial_thickness),
        rotation_angle=float(rotation_angle),
    )
    # my_reactor.export_html_3d("assets/reactor_3d.html")
    my_reactor.export_stl("assets/reactor_3d.stl")

    demo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    head_vti = os.path.join(
        demo_dir, "paramak-cloud", "assets", "reactor_3d.stl"
    )

    # Load dataset from dist
    reader = vtk.vtkSTLReader()
    reader.SetFileName(head_vti)
    reader.Update()

    mesh_state = to_mesh_state(reader.GetOutput())

    vtk_view = dash_vtk.View(
        dash_vtk.GeometryRepresentation(
            dash_vtk.Mesh(state=mesh_state),
        )
    )

    return html.Div(
        id="reactor_viewer",
        # children=[html.Div(vtk_view)]
        style={"height": "calc(80vh - 16px)", "width": "100%"},
        children=html.Div(
            vtk_view, style={"height": "100%", "width": "100%"}
        )
    )


if __name__ == "__main__":
    app.run_server(
        # debug=True,
        # # https://github.com/plotly/dash/issues/1293
        # dev_tools_hot_reload=False
    )
