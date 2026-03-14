from field_math_engine.geometry.area import EQUATIONS
from field_math_engine.geometry.volume import run_volume_calc
from field_math_engine.hydraulics.flow import run_flow_calculator
from field_math_engine.hydraulics.veloctiy import run_velocity_calculator
from field_math_engine.geometry.input_helpers import get_object_measurement
from field_math_engine.constants import FEET_SQUARED, INCHES_SQUARED
from field_math_engine.unit_helpers import inches_to_feet, convert_inches_squared, final_calc_value

# AREA CLI HELPERS

def area_formula_choice():  # Handle area formula selection
    formula = int(input("Area Calculation type [1=Rectangle, 2=Circle, 3 = Trapizoid, 4 = Trianlge, 5 = Eclipse, 6=Annulus]: ").strip())
    if formula in INPUTS:
        return EQUATIONS[formula](*INPUTS[formula]()) # unpack function if needed
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

def run_area_calculator():
    area_ft_sq = area_formula_choice()
    unit = area_unit_choice()
    final_area = convert_inches_squared(unit, area_ft_sq)
    final_calc_value(final_area, unit)

def calculator_choice():
    command = input("Calculator [type: area, volume, flow, or velocity]: ").lower().strip()
    match command:
        case "area":
            run_area_calculator()
        case "volume":
            run_volume_calc()
        case "flow":
            run_flow_calculator()
        case "velocity":
            run_velocity_calculator()
        case _:
            print("Invalid option")

# area INPUTS
INPUTS = {
    1: area_rectangle_input,
    2: area_circle_input,
    3: area_trapeziod_input,
    4: area_triangle_input,
    5: area_ellipse_input,
    6: area_annulus_input,
    }