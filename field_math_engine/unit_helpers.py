from field_math_engine.constants import (
    FEET_SQUARED,
    FOOT_SQUARED,
    INCHES_SQUARED,
    ONE_FOOT,
)

def convert_area_output(unit,area_ft_sq):
    if unit == FEET_SQUARED:
        return area_ft_sq
    elif unit == INCHES_SQUARED:
        area_ft_sq = area_ft_sq * FOOT_SQUARED
        return area_ft_sq
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

def final_unit_choice():
    unit = input("Output units [1=ft², 2=in²]: ").strip()
    if unit == "1":
        return FEET_SQUARED
    elif unit == "2":
        return INCHES_SQUARED
    else:
        raise ValueError("Invalid unit")

def final_calc_value(area_ft_sq, unit):  # Output final value in correct units
    print(f"{area_ft_sq:g} {unit}")