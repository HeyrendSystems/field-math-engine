from field_math_engine.geometry.area import AREA_EQUATIONS
from field_math_engine.geometry.volume import VOLUME_EQUATIONS
from field_math_engine.geometry.input_helpers import get_object_measurement, get_psi_measurement, pressure_head
from field_math_engine.hydraulics.flow import flow_rate
from field_math_engine.hydraulics.veloctiy import velocity_rate
from field_math_engine.hydraulics.tdh import friction_head_loss, total_dynamic_head_calc
from field_math_engine.unit_helpers import (
    inches_to_feet,
    convert_inches_squared,
    final_calc_value,
    get_number_format,
    convert_inches_cubed,
    feet_to_inches,
)
from field_math_engine.constants import (
    FEET_SQUARED,
    FEET_CUBED,
    FOOT_TO_METER,
    CFS_TO_GPD,
    CFS_TO_GPH,
    CFS_TO_GPM,
    CFS_TO_GPS,
    INCHES_CUBED,
    INCHES_SQUARED,
    ONE_FOOT,
    SECONDS_IN_MINUTES,
    MINUTES_IN_DAY,
    MINUTES_IN_HOUR,
    PSI_TO_FT_HEAD,
)


# AREA CLI HELPERS

def area_formula_choice():  # Handle area formula selection
    formula = int(input("Area Calculation type [1=Rectangle, 2=Circle, 3 = Trapizoid, 4 = Trianlge, 5 = Eclipse, 6=Annulus]: ").strip())
    if formula in AREA_INPUTS:
        return AREA_EQUATIONS[formula](*AREA_INPUTS[formula]()) # unpack function if needed
    else:
        raise ValueError("Invalid formula choice")

def area_unit_choice():
    unit = input("Output units [1=ft², 2=in²]: ").strip()
    if unit == "1":
        return FEET_SQUARED
    elif unit == "2":
        return INCHES_SQUARED
    else:
        raise ValueError("Invalid unit")

def area_rectangle_input():
    length, length_unit = get_object_measurement("Length")
    width, width_unit = get_object_measurement("Width")
    length_ft = inches_to_feet(length, length_unit)
    width_ft = inches_to_feet(width, width_unit)
    return length_ft, width_ft

def area_circle_input():
    diameter, diameter_unit = get_object_measurement("Diameter")
    diameter_ft = inches_to_feet(diameter, diameter_unit)
    return diameter_ft,

def area_trapeziod_input():
    base_one, base_one_unit = get_object_measurement("base one length")
    base_two, base_two_unit = get_object_measurement("base two length")
    height, height_unit = get_object_measurement("Height")
    base_one_ft = inches_to_feet(base_one, base_one_unit)
    base_two_ft = inches_to_feet(base_two, base_two_unit)
    height_ft = inches_to_feet(height,height_unit)
    return base_one_ft, base_two_ft, height_ft

def area_triangle_input():
    base, base_unit = get_object_measurement("Base")
    height, height_unit = get_object_measurement("Height")
    base_ft = inches_to_feet(base, base_unit)
    height_ft = inches_to_feet(height, height_unit)
    return base_ft, height_ft

def area_ellipse_input():
    semi_major_axis, semi_major_axis_unit = get_object_measurement("Semi major axis")
    semi_minor_axis, semi_minor_axis_unit = get_object_measurement("Semi major axis")
    semi_major_axis_ft = inches_to_feet(semi_major_axis, semi_major_axis_unit)
    semi_minor_axis_ft = inches_to_feet(semi_minor_axis, semi_minor_axis_unit)
    return semi_major_axis_ft, semi_minor_axis_ft

def area_annulus_input():
    outside_diameter, outside_diameter_unit = get_object_measurement("Outside Diameter")
    inside_diameter, inside_diameter_unit = get_object_measurement("Inside Diameter")
    outside_diameter_ft =inches_to_feet(outside_diameter, outside_diameter_unit)
    inside_diameter_ft = inches_to_feet(inside_diameter, inside_diameter_unit)
    return outside_diameter_ft, inside_diameter_ft

# area INPUTS
AREA_INPUTS = {
    1: area_rectangle_input,
    2: area_circle_input,
    3: area_trapeziod_input,
    4: area_triangle_input,
    5: area_ellipse_input,
    6: area_annulus_input,
    }

# Run area calc
def run_area_calculator():
    area_ft_sq = area_formula_choice()
    unit = area_unit_choice()
    final_area = convert_inches_squared(unit, area_ft_sq)
    final_calc_value(final_area, unit)

# Volume CLI helpers
def volume_formula_choice():  # Handle area formula selection
    formula = int(input("Volume Calculation type [1=Rectangle, 2=Cube, 3=Sphere, 4=Hemisphere, 5=Cylinder, 6=Annular(Pipe)]: ").strip())
    if formula in VOLUME_INPUTS:
        return VOLUME_EQUATIONS[formula](*VOLUME_INPUTS[formula]()) # unpack function if needed
    else:
        raise ValueError("Invalid formula choice")

def volume_unit_choice():
    unit = input("Output units [1=ft³, 2=in³]: ").strip()
    if unit == "1":
        return FEET_CUBED
    elif unit == "2":
        return INCHES_CUBED
    else:
        raise ValueError("Invalid unit")

def volume_rectangle_prism_input():
    length, length_unit = get_object_measurement("Length")
    height, height_unit = get_object_measurement("Height")
    width, width_unit = get_object_measurement("Width")
    length_ft = inches_to_feet(length, length_unit)
    height_ft = inches_to_feet(height, height_unit)
    width_ft = inches_to_feet(width, width_unit)
    return length_ft, height_ft, width_ft

def volume_cube_input():
    length, length_unit = get_object_measurement("Length")
    length_ft = inches_to_feet(length, length_unit)
    return length_ft,

def volume_sphere_input():
    diameter, diameter_unit =  get_object_measurement("Diameter")
    diameter_ft = inches_to_feet(diameter, diameter_unit)
    return diameter_ft,

def volume_hemisphere_input():
    return volume_sphere_input()


def volume_cylinder_input():
    diameter_ft, = area_circle_input()
    height, height_unit = get_object_measurement("Height")
    height_ft = inches_to_feet(height, height_unit)
    return diameter_ft, height_ft

def volume_annulus_input():
    outside_diameter, outside_diameter_unit = get_object_measurement("Outside Diameter")
    inside_diameter, inside_diameter_unit = get_object_measurement("Inside Diameter")
    outside_diameter_ft =inches_to_feet(outside_diameter, outside_diameter_unit)
    inside_diameter_ft = inches_to_feet(inside_diameter, inside_diameter_unit)
    if outside_diameter_ft < inside_diameter_ft:
        raise ValueError("Outside diameter cannot be less than inside diameter.")
    else:
        height, height_unit = get_object_measurement("Height")
        height_ft = inches_to_feet(height, height_unit)

    return outside_diameter_ft, inside_diameter_ft, height_ft

def run_volume_calc():
    volume_cb_ft = volume_formula_choice()
    unit = volume_unit_choice()
    final_volume = convert_inches_cubed(unit, volume_cb_ft)
    final_calc_value(final_volume, unit)


VOLUME_INPUTS = {

1: volume_rectangle_prism_input,
2: volume_cube_input,
3: volume_sphere_input,
4: volume_hemisphere_input,
5: volume_cylinder_input,
6: volume_annulus_input,
    }


# FLOW CLI helpers
def get_velocity(prompt):
    value = float(input(f"{prompt}: ").strip())
    return value

def flow_unit_choice(flow):
    command = input("Final units for flow [1=ft³/s, 2=GPS, 3=GPM, 4=GPH, 5=GPD]: ").strip().lower()
    match command:
        case "1":
            unit = "ft³/s"
            value = flow
        case "2":
            unit = "GPS"
            value = flow * CFS_TO_GPS
        case "3":
            unit = "GPM"
            value = flow * CFS_TO_GPM
        case "4":
            unit = "GPH"
            value = flow * CFS_TO_GPH
        case "5":
            unit = "GPD"
            value = flow * CFS_TO_GPD
    return value, unit

def print_flow(value, unit):
    print(f"This is the flow {value} {unit}")

# Run flow calc
def run_flow_calculator():
    area_of_shape = area_formula_choice()
    velocity = get_velocity("Velocity")
    flow = flow_rate(area_of_shape, velocity)
    value, unit = flow_unit_choice(flow)
    value = get_number_format(value)
    print_flow(value, unit)

# Velocity CLI helpers
def get_flow(prompt):
    value = float(input(f"{prompt}: ").strip())
    return value

def convert_flow_to_cfs():
    command = input("Flow units [1=ft³/s, 2=GPS, 3=GPM, 4=GPH, 5=GPD]: ")
    match command:
        case "1":
            flow = get_flow("Flow ft³/s")
        case "2":
            flow = get_flow("Flow GPS")
            flow = flow / CFS_TO_GPS
        case "3":
            flow = get_flow("Flow GPM")
            flow = flow / CFS_TO_GPM
        case "4":
            flow = get_flow("Flow GPH")
            flow = flow / CFS_TO_GPH
        case "5":
            flow = get_flow("Flow GPD")
            flow = flow / CFS_TO_GPD
    return flow

def final_velocity_unit(velocity):
    command = input("Final units for velocity [1=in/s, 2=ft/s, 3=m/s: ").strip().lower()
    match command:
        case "1":
            unit = "in/s"
            velocity = velocity * ONE_FOOT
        case "2":
            unit = "ft/s"
        case "3":
            unit = "m/s"
            velocity = velocity * FOOT_TO_METER
    return velocity, unit

# Run veolcity calc
def run_velocity_calculator():
    area_of_shape = area_formula_choice()
    flow =  convert_flow_to_cfs()
    velocity = velocity_rate(flow, area_of_shape)
    velocity, unit = final_velocity_unit(velocity)
    velocity = get_number_format(velocity)
    print(velocity,unit)

# Total Dynamic Head Helpers
def convert_flow_to_gpm():
    command = input("Flow units [1=ft³/s, 2=GPS, 3=GPM, 4=GPH, 5=GPD]: ")
    match command:
        case "1":
            flow = get_flow("Flow ft³/s")
            flow = flow * CFS_TO_GPM
        case "2":
            flow = get_flow("Flow GPS")
            flow = flow * SECONDS_IN_MINUTES
        case "3":
            flow = get_flow("Flow GPM")
            flow = flow
        case "4":
            flow = get_flow("Flow GPH")
            flow = flow / MINUTES_IN_HOUR
        case "5":
            flow = get_flow("Flow GPD")
            flow = flow / MINUTES_IN_DAY
    return flow

def get_friction_measurements_inputs():
    pipe_length, pipe_length_unit = get_object_measurement("Pipe Length")
    pipe_length_ft = inches_to_feet(pipe_length, pipe_length_unit)
    flow_rate_measurement = convert_flow_to_gpm()
    pipe_roughness = float(input("Pipe roughness: "))
    inside_diameter, inside_diameter_unit = get_object_measurement("Inside_diameter")
    inside_diameter_inches = feet_to_inches(inside_diameter, inside_diameter_unit)
    return pipe_length_ft, flow_rate_measurement, pipe_roughness, inside_diameter_inches

def get_static_water_level_inputsl():
    static_water_level, static_water_level_unit = get_object_measurement("Static water level")
    static_water_level_ft = inches_to_feet(static_water_level, static_water_level_unit)
    return static_water_level_ft

def get_hydraulic_grade_line_inputs():
    destination_elevation, destination_elevation_unit = get_object_measurement("Destination elevation")
    destination_elevation_ft = inches_to_feet(destination_elevation, destination_elevation_unit)
    required_psi = get_psi_measurement("Required PSI")
    pressure_head_ft = pressure_head(required_psi)
    return destination_elevation_ft, pressure_head_ft



# Run TDH calc
def run_tdh_calculator():
    pipe_length_ft, flow_rate_measurement, pipe_roughness, inside_diameter = get_friction_measurements_inputs()
    friction_loss_ft = friction_head_loss(pipe_length_ft, flow_rate_measurement, pipe_roughness, inside_diameter)
    friction_psi = friction_loss_ft / PSI_TO_FT_HEAD
    print(f"Friction head loss: {friction_loss_ft}")
    print(f"Pressure loss: {friction_psi}")
    static_water_level_ft = get_static_water_level_inputsl()
    destination_elevation_ft, pressure_head_ft = get_hydraulic_grade_line_inputs()
    print(pressure_head_ft)
    tdh = total_dynamic_head_calc(static_water_level_ft, destination_elevation_ft, pressure_head_ft, friction_loss_ft)
    return tdh





# Calculator choice
def calculator_choice():
    command = input("Calculator [type: area, volume, flow, velocity, TDH]: ").lower().strip()
    match command:
        case "area":
            run_area_calculator()
        case "volume":
            run_volume_calc()
        case "flow":
            run_flow_calculator()
        case "velocity":
            run_velocity_calculator()
        case "tdh":
            run_tdh_calculator()
        case _:
            print("Invalid option")