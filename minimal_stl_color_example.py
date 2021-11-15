import vtk
import dash_vtk
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from dash_vtk.utils import to_mesh_state


app = dash.Dash(
    __name__,
    # prevent_initial_callbacks=True,
)

server = app.server


app.layout = html.Div([
    dcc.Input(
        id="filename_1_input",
        value='assets/filename_1.stl',
    ),
    dcc.Input(
        id="filename_2_input",
        value='assets/filename_2.stl',
    ),
    dcc.Loading(
        id="reactor_viewer",
        type="default",
    )]
)

@app.callback(
    Output("reactor_viewer", "children"),
    Input("filename_1_input", "value"),
    Input("filename_2_input", "value"),
)
def update_reactor(filename_1, filename_2):

    actors = []
    for name in [filename_1, filename_2]:
        reader = vtk.vtkSTLReader()
        reader.SetFileName(name)
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(reader.GetOutputPort())

        actor = vtk.vtkActor()
        actor.SetMapper(mapper)
        actor.GetProperty().SetColor((1,0,0))

        actors.append(actor)

    # how to make use of actors here
    mesh_state = to_mesh_state(reader.GetOutput())
    vtk_view = dash_vtk.View(
        dash_vtk.GeometryRepresentation(
            dash_vtk.Mesh(state=mesh_state),
        )
    )

    return html.Div(
        id="dash_vtk_viewer",
        style={"height": "calc(80vh - 16px)", "width": "100%"},
        children=html.Div(
            vtk_view, style={"height": "100%", "width": "100%"}
        )
    )


if __name__ == "__main__":
    app.run_server()
