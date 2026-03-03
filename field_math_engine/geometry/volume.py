import math
from ..constants import FEET_CUBED, INCHES_CUBED
from field_math_engine.geometry.input_helpers import get_object_measurement
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

def volume_unit_choice():
    unit = input("Output units [1=ft³, 2=in³]: ").strip()
    if unit == "1":
        return FEET_CUBED
    elif unit == "2":
        return INCHES_CUBED
    else:
        raise ValueError("Invalid unit")

def volume_formula_choice():  # Handle volume formula selection
    formula = int(input("Volume Calculation type [1=Cube, 2=Coming Soon]: ").strip())
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
1 : volume_cube,

    }

