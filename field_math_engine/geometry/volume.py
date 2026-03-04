import math
import sys
from ..constants import DIAMETER_CUBED_DIVISOR,DIAMETER_SQUARED_DIVISOR, FEET_CUBED, INCHES_CUBED
from field_math_engine.geometry.input_helpers import get_object_measurement
from field_math_engine.geometry.area import area_circle, area_annulus
from field_math_engine.unit_helpers import (
    inches_to_feet,
    final_calc_value,
    convert_inches_cubed,

)

def volume_cube():
    length, length_unit = get_object_measurement("Length")
    length_ft = inches_to_feet(length, length_unit)
    volume_cu_ft = length_ft ** 3
    return volume_cu_ft

def volume_rectangle_prism():
    length, length_unit = get_object_measurement("Length")
    height, height_unit = get_object_measurement("Height")
    width, width_unit = get_object_measurement("Width")
    length_ft = inches_to_feet(length, length_unit)
    height_ft = inches_to_feet(height, height_unit)
    width_ft = inches_to_feet(width, width_unit)
    volume_cu_ft = length_ft * height_ft * width_ft
    return volume_cu_ft

def volume_sphere():
    diameter, diameter_unit =  get_object_measurement("Diameter")
    diameter_ft = inches_to_feet(diameter, diameter_unit)
    volume_cb_ft =  (math.pi / DIAMETER_CUBED_DIVISOR) * diameter_ft ** 3
    return volume_cb_ft

def volume_hemisphere():
    return volume_sphere() / 2

def volume_cylinder():
    height, height_unit = get_object_measurement("Height")
    height_ft = inches_to_feet(height, height_unit)
    volume_cb_ft = area_circle() * height_ft
    return volume_cb_ft

def volume_annulus():
    outside_diameter, outside_diameter_unit = get_object_measurement("Outside Diameter")
    inside_diameter, inside_diameter_unit = get_object_measurement("Inside Diameter")
    outside_diameter_ft =inches_to_feet(outside_diameter, outside_diameter_unit)
    inside_diameter_ft = inches_to_feet(inside_diameter, inside_diameter_unit)
    if outside_diameter_ft < inside_diameter_ft:
        raise ValueError("Outside diameter cannot be less than inside diameter.")

    else:
        height, height_unit = get_object_measurement("Height")
        height_ft = inches_to_feet(height, height_unit)
        volume_cb_ft = (
            (math.pi/ DIAMETER_SQUARED_DIVISOR)
            * (outside_diameter_ft ** 2 -inside_diameter_ft ** 2)
            * height_ft
        )
    return volume_cb_ft


def volume_unit_choice():
    unit = input("Output units [1=ft³, 2=in³]: ").strip()
    if unit == "1":
        return FEET_CUBED
    elif unit == "2":
        return INCHES_CUBED
    else:
        raise ValueError("Invalid unit")

def volume_formula_choice():  # Handle volume formula selection
    formula = int(input("Volume Calculation type [1=Rectangle, 2=Cube, 3=Sphere, 4=Hemisphere, 5=Cylinder, 6=Annular(Pipe)]: ").strip())
    if formula in EQUATIONS:
        return EQUATIONS[formula]()
    else:
        raise ValueError("Invalid formula choice")

def run_volume_calc():
    volume_cb_ft = volume_formula_choice()
    unit = volume_unit_choice()
    final_volume = convert_inches_cubed(unit, volume_cb_ft)
    final_calc_value(final_volume, unit)


EQUATIONS = {

1: volume_rectangle_prism,
2: volume_cube,
3: volume_sphere,
4: volume_hemisphere,
5: volume_cylinder,
6: volume_annulus,
    }

