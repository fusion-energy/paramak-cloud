from paramak import BallReactor, FlfSystemCodeReactor

def make_flfsystemcodereactor_paramak_object(
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
    my_reactor = FlfSystemCodeReactor(
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

    return my_reactor


def make_ballreactor_paramak_object(
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
    rotation_angle):

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
    
    if number_of_tf_coils == 0:
        number_of_tf_coils = None

    my_reactor = BallReactor(
        inner_bore_radial_thickness=inner_bore_radial_thickness,
        inboard_tf_leg_radial_thickness=inboard_tf_leg_radial_thickness,
        center_column_shield_radial_thickness=center_column_shield_radial_thickness,
        divertor_radial_thickness=divertor_radial_thickness,
        inner_plasma_gap_radial_thickness=inner_plasma_gap_radial_thickness,
        plasma_radial_thickness=plasma_radial_thickness,
        outer_plasma_gap_radial_thickness=outer_plasma_gap_radial_thickness,
        blanket_radial_thickness=blanket_radial_thickness,
        blanket_rear_wall_radial_thickness=blanket_rear_wall_radial_thickness,
        plasma_gap_vertical_thickness=plasma_gap_vertical_thickness,
        elongation=elongation,
        triangularity=triangularity,
        firstwall_radial_thickness=firstwall_radial_thickness,
        divertor_to_tf_gap_vertical_thickness=divertor_to_tf_gap_vertical_thickness,
        number_of_tf_coils=number_of_tf_coils,
        rear_blanket_to_tf_gap=rear_blanket_to_tf_gap,
        outboard_tf_coil_radial_thickness=outboard_tf_coil_radial_thickness,
        outboard_tf_coil_poloidal_thickness=outboard_tf_coil_poloidal_thickness,
        rotation_angle=rotation_angle,
        divertor_position=divertor_position,
        pf_coil_radial_thicknesses=pf_coil_radial_thicknesses,
        pf_coil_vertical_thicknesses=pf_coil_vertical_thicknesses,
        pf_coil_radial_position=pf_coil_radial_position,
        pf_coil_vertical_position=pf_coil_vertical_position,
        pf_coil_case_thicknesses=pf_coil_case_thicknesses,
    )

    return my_reactor
