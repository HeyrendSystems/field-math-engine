import math
from ..constants import DIAMETER_SQUARED_DIVISOR, FEET_SQUARED, INCHES_SQUARED
from field_math_engine.geometry.input_helpers import get_object_measurement
from field_math_engine.unit_helpers import (
    inches_to_feet,
    final_calc_value,
    convert_inches_squared,
)

def area_rectangle():
    length, length_unit = get_object_measurement("Length")
    width, width_unit = get_object_measurement("Width")
    length_ft = inches_to_feet(length, length_unit)
    width_ft = inches_to_feet(width, width_unit)
    area_ft_sq = length_ft * width_ft
    return area_ft_sq

def area_circle():
    diameter, diameter_unit = get_object_measurement("Diameter")
    diameter_ft = inches_to_feet(diameter, diameter_unit)
    area_ft_sq = (math.pi / DIAMETER_SQUARED_DIVISOR) * diameter_ft ** 2
    return area_ft_sq

def area_trapezoid():
    base_one, base_one_unit = get_object_measurement("base one length")
    base_two, base_two_unit = get_object_measurement("base two length")
    height, height_unit = get_object_measurement("Height")
    base_one_ft = inches_to_feet(base_one, base_one_unit)
    base_two_ft = inches_to_feet(base_two, base_two_unit)
    height_ft = inches_to_feet(height,height_unit)
    area_ft_sq = ((base_one_ft + base_two_ft) * height_ft ) / 2
    return area_ft_sq

def area_triangle():
    base, base_unit = get_object_measurement("Base")
    height, height_unit = get_object_measurement("Height")
    base_ft = inches_to_feet(base, base_unit)
    height_ft = inches_to_feet(height, height_unit)
    area_ft_sq = (base_ft * height_ft) * 0.5
    return area_ft_sq

def area_eclipse():
    semi_major_axis, semi_major_axis_unit = get_object_measurement("Semi major axis")
    semi_minor_axis, semi_minor_axis_unit = get_object_measurement("Semi major axis")
    semi_major_axis_ft = inches_to_feet(semi_major_axis, semi_major_axis_unit)
    semi_minor_axis_ft = inches_to_feet(semi_minor_axis, semi_minor_axis_unit)
    area_ft_sq = (math.pi * semi_major_axis_ft * semi_minor_axis_ft)
    return area_ft_sq

def area_formula_choice():  # Handle area formula selection
    formula = int(input("Area Calculation type [1=Rectangle, 2=Circle, 3 = Trapizoid, 4 = Trianlge, 5 = Eclipse]: ").strip())
    if formula in EQUATIONS:
        return EQUATIONS[formula]()
    else:
        raise ValueError("Invalid formula choice")

def run_area_calculator():
    area_ft_sq = area_formula_choice()
    unit = area_unit_choice()
    final_area = convert_inches_squared(unit, area_ft_sq)
    final_calc_value(final_area, unit)

def area_unit_choice():
    unit = input("Output units [1=ft², 2=in²]: ").strip()
    if unit == "1":
        return FEET_SQUARED
    elif unit == "2":
        return INCHES_SQUARED
    else:
        raise ValueError("Invalid unit")


EQUATIONS = {
    1 : area_rectangle,
    2 : area_circle,
    3 : area_trapezoid,
    4: area_triangle,
    5: area_eclipse,
    }