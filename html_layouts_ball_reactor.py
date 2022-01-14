from dash import dcc, html
from dash_daq import NumericInput


ball_reactor_geometry_input_args_table = html.Table(
    [
        html.Tr(
            [
                html.Td("inner bore radial thickness (cm)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        id="inner_bore_radial_thickness",
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
                html.Td("inboard tf leg radial thickness (cm)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        id="inboard_tf_leg_radial_thickness",
                        value=30,
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
                html.Td("center column shield radial thickness (cm)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        id="center_column_shield_radial_thickness",
                        value=60,
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
                html.Td("divertor radial thickness (cm)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        id="divertor_radial_thickness",
                        value=150,
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
                html.Td("inner plasma gap radial thickness (cm)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        id="inner_plasma_gap_radial_thickness",
                        value=30,
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
                html.Td("plasma radial thickness (cm)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        id="plasma_radial_thickness",
                        value=300,
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
                html.Td("outer plasma gap radial thickness (cm)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        id="outer_plasma_gap_radial_thickness",
                        value=30,
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
                html.Td("plasma gap vertical thickness (cm)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        id="plasma_gap_vertical_thickness",
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
                html.Td("firstwall radial thickness (cm)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        id="firstwall_radial_thickness",
                        value=30,
                        type="number",
                        min=0.01,
                        max=1000,
                        size=10,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("blanket radial thickness (cm)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        id="blanket_radial_thickness",
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
                html.Td("blanket rear wall radial thickness (cm)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        id="blanket_rear_wall_radial_thickness",
                        value=30,
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
                html.Td("elongation", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        id="elongation",
                        value=2.0,
                        type="number",
                        min=0,
                        max=1000,
                        size=10,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("triangularity", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        id="triangularity",
                        value=0.55,
                        type="number",
                        min=-100,
                        max=100,
                        size=10,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("divertor to tf gap vertical thickness (cm)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        id="divertor_to_tf_gap_vertical_thickness",
                        value=0,
                        type="number",
                        min=0,
                        max=1000,
                        size=10,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("number of tf coils", style={'white-space': 'nowrap'}),
                html.Td( #  could be numericalinput which allows ints

                    NumericInput(
                        id="number_of_tf_coils",
                        value=0,
                        min=0,
                        max=100,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("rear blanket to tf gap (cm)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        id="rear_blanket_to_tf_gap",
                        value=50,
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("pf coil radial thicknesses (cm)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        id="pf_coil_radial_thicknesses",
                        value="20,50,50,20",
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("pf coil vertical thicknesses (cm)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        id="pf_coil_vertical_thicknesses",
                        value="20,50,50,20",
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("pf coil radial position (cm)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        type="text",
                        id="pf_coil_radial_position",
                        value="500,575,575,500",
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("pf coil vertical position (cm)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        type="text",
                        id="pf_coil_vertical_position",
                        value="300,100,-100,-300",
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("pf coil case thicknesses (cm)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        id="pf_coil_case_thicknesses",
                        value="10,10,10,10",
                    )
                ),
            ]
        ),
        html.Tr(
            [
                html.Td("outboard tf coil radial thickness (cm)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(  # note this can be None
                        id="outboard_tf_coil_radial_thickness",
                        value=100,
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
                html.Td("outboard tf coil poloidal thickness (cm)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(  # note this can be None
                        id="outboard_tf_coil_poloidal_thickness",
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
                html.Td("divertor position", style={'white-space': 'nowrap'}),
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
                html.Td("rotation angle (degrees)", style={'white-space': 'nowrap'}),
                html.Td(
                    dcc.Input(
                        id="rotation_angle",
                        value=180,
                        type="number",
                        min=1,
                        max=360,
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
                    id="download_ballreactor_stl_button",
                    style={'margin': '5px'}
                ),
                html.Button(
                    "Download STP",
                    title="Click to dowload the reactor CAD in STP file format",
                    id="download_ballreactor_stp_button",
                    style={'margin': '5px'}
                ), 
                html.Button(
                    "Download HTML",
                    title="Click to dowload the reactor CAD in HTML file format",
                    id="download_ballreactor_html_button",
                    style={'margin': '5px'}
                ),
            ],
            style={"text-align": "center"}
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


ballreactor_neutronics_parameters = html.Table(
    # Header
    [
        html.Tr(
            [
                # html.H2("\U0001f449 Specify neutronics settings"),
                html.H2("not implemented yet")
            ]
        ),
        # html.Tr(
        #     [
        #         html.Td("batches"),
        #         html.Td(
        #             dcc.Input(
        #                 id="simulation_batches",
        #                 value=10,
        #             )
        #         ),
        #     ]
        # ),
        # html.Tr(
        #     [
        #         html.Td("particles per batch"),
        #         html.Td(
        #             dcc.Input(
        #                 id="simulation_particles",
        #                 value=1000,
        #             )
        #         ),
        #     ]
        # ),
        # html.Tr(
        #     [
        #         html.Td("results required"),
        #         html.Td(
        #             dcc.Dropdown(
        #                 options=[
        #                     {"label": "TBR", "value": "tbr"},
        #                     {"label": "blanket heating", "value": "heating"},
        #                     {"label": "DPA - not implemented yet", "value": "dpa"},
        #                     {"label": "dose maps - not implemented yet", "value": "dose_maps"},
        #                     {"label": "dose vtk - not implemented yet", "value": "dose_vtk"},
        #                 ],
        #                 value=["tbr"],
        #                 multi=True,
        #                 id="results_required",
        #             )
        #         ),
        #     ]
        # ),
        # html.Br(),
        # html.Button(
        #     "Simulate reactor",
        #     title="Click to start a neutronics simulation",
        #     id="simulate_button",
        # ),
        # html.Br(),
        # html.Br(),
        # html.A(
        #     "Link to simulation API",
        #     href="https://tgkubvki8f.execute-api.eu-west-2.amazonaws.com/flf_neutronics_api",
        #     target="_blank",
        # ),
        # dcc.Loading(
        #     id="simulate_results",
        #     type="default",
        # ),
    ]
)

