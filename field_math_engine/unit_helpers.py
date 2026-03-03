from field_math_engine.constants import (
    FEET_CUBED,
    FEET_SQUARED,
    FOOT_CUBED,
    FOOT_SQUARED,
    INCHES_CUBED,
    INCHES_SQUARED,
    ONE_FOOT,
)

def convert_inches_squared(unit, value):
    if unit == FEET_SQUARED:
        return value
    elif unit == INCHES_SQUARED:
        value = value * FOOT_SQUARED
        return value
    else:
        raise ValueError("Invalid unit")

def convert_inches_cubed(unit, value):
    if unit == FEET_CUBED:
        return value
    elif unit == INCHES_CUBED:
        value = value * FOOT_CUBED
        return value
    else:
        raise ValueError("Invalid unit")

def inches_to_feet(value, unit):
    unit = unit.strip().lower()
    if unit in ("inches", "inch" ,"in"):
        value = value / ONE_FOOT
        return value
    elif unit in ("feet", "foot" ,"ft"):
        return value
    else:
        raise ValueError("Invalid unit")

def final_unit_choice(unit):
    pass # currently final unit choice is choosen in calulator engines


def final_calc_value(value, unit):  # Output final value in correct units
    print(f"{value:g} {unit}")