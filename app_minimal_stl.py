import os
import dash
from dash import html

import dash_vtk
from dash_vtk.utils import to_volume_state, to_mesh_state

import vtk

demo_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
head_vti = os.path.join(demo_dir, "paramak-cloud", "data", "example.stl")

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

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(
    style={"height": "calc(100vh - 16px)", "width": "100%"},
    children=[html.Div(vtk_view, style={"height": "100%", "width": "100%"})],
)

if __name__ == "__main__":
    app.run_server(debug=True)
