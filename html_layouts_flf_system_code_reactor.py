from dash import dcc, html
from dash_daq import NumericInput


flf_system_code_reactor_geometry_input_args_table = html.Table(
    [
        html.Tr(
            [
                html.Td("Inner blanket radius (cm)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        id="inner_blanket_radius",
                        value=100.,
                        type="number",
                        min=1,
                        max=1000,
                        size=10,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("blanket thickness (cm)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        id="blanket_thickness",
                        value=70,
                        type="number",
                        min=1,
                        max=1000,
                        size=10,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("blanket height  (cm)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        id="blanket_height",
                        value=500,
                        type="number",
                        min=1,
                        max=1000,
                        size=10,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("lower blanket thickness (cm)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        id="lower_blanket_thickness",
                        value=50,
                        type="number",
                        min=1,
                        max=1000,
                        size=10,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("upper blanket thickness (cm)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        id="upper_blanket_thickness",
                        value=40,
                        type="number",
                        min=1,
                        max=1000,
                        size=10,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("blanket vessel gap (cm)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        id="blanket_vv_gap",
                        value=20,
                        type="number",
                        min=1,
                        max=1000,
                        size=10,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("upper vessel thickness (cm)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        id="upper_vv_thickness",
                        value=10,
                        type="number",
                        min=1,
                        max=1000,
                        size=10,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("vessel thickness (cm)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        id="vv_thickness",
                        value=10,
                        type="number",
                        min=1,
                        max=1000,
                        size=10,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("lower vessel thickness (cm)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        id="lower_vv_thickness",
                        value=10,
                        type="number",
                        min=1,
                        max=1000,
                        size=10,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("rotation angle (degrees)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        id="flf_rotation_angle",
                        value=180,
                        type="number",
                        min=1,
                        max=360,
                        size=10,
                    )
                ),
            ]
        ),
        html.Br(),
        html.Br(),
        html.Div(
            children=[
                html.Button(
                    "Download STL",
                    title="Click to dowload the reactor CAD in STL file format",
                    id="download_flf_stl_button",
                    style={'margin': '5px'}
                ),
                html.Button(
                    "Download STP",
                    title="Click to dowload the reactor CAD in STP file format",
                    id="download_flf_stp_button",
                    style={'margin': '5px'}
                ), 
                html.Button(
                    "Download HTML",
                    title="Click to dowload the reactor CAD in HTML file format",
                    id="download_flf_html_button",
                    style={'margin': '5px'}
                ),
                html.Button(
                    "Download DAGMC h5m",
                    title="Click to dowload the reactor CAD in h5m file format",
                    id="download_flf_h5m_button",
                    style={'margin': '5px'}
                ),
            ],
            style={"text-align": "center"}
        ),
    ],
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


flf_system_code_reactor_neutronics_parameters = html.Table(
    # Header
    [
        # html.Tr(
        #     [
        #         html.H2("\U0001f449 Specify neutronics settings")
        #     ]
        # ),
        html.Tr(
            [
                html.Td("batches"),
                html.Td(
                    dcc.Input(
                        id="simulation_flfsystemcodereactor_batches",
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
                        id="simulation_flfsystemcodereactor_particles",
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
                            {"label": "Tritium Breeding Ratio (TBR)", "value": "tbr"},
                            {"label": "blanket heating", "value": "heating"},
                            # {"label": "DPA - not implemented yet", "value": "dpa"},
                            # {"label": "dose maps - not implemented yet", "value": "dose_maps"},
                            # {"label": "dose vtk - not implemented yet", "value": "dose_vtk"},
                        ],
                        value=["tbr"],
                        multi=True,
                        id="results_flfsystemcodereactor_required",
                    )
                ),
            ]
        ),
        html.Br(),
        html.Button(
            "Simulate reactor",
            title="Click to start a neutronics simulation",
            id="simulate_flfsystemcodereactor_button",
            n_clicks=0
        ),
        html.Br(),
        html.Br(),
        html.A(
            "Link to simulation API",
            href="https://tgkubvki8f.execute-api.eu-west-2.amazonaws.com/flf_neutronics_api",
            target="_blank",
        ),
        dcc.Loading(
            id="simulate_flfsystemcodereactor_results",
            type="default",
        ),
    ]
)
