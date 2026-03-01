import math
from field_math_engine.geometry.input_helpers import get_object_measurement
from field_math_engine.unit_helpers import inches_to_feet
from ..constants import (
    DIAMETER_SQUARED_DIVISOR,
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


