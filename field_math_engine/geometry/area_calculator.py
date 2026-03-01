import math

DIAMETER_SQUARED_DIVISOR = 4
FOOT_SQUARED = 144
ONE_FOOT = 12
FEET_SQUARED = "ft²"
INCHES_SQUARED = "in²"


def final_unit_choice():
    unit = input("Output units [1=ft², 2=in²]: ").strip()
    if unit == "1":
        return FEET_SQUARED
    elif unit == "2":
        return INCHES_SQUARED
    else:
        raise ValueError("Invalid unit")

def convert_area_output(unit,area_ft_sq):
    if unit == FEET_SQUARED:
        return area_ft_sq
    elif unit == INCHES_SQUARED:
        area_ft_sq = area_ft_sq * FOOT_SQUARED
        return area_ft_sq
    else:
        raise ValueError("Invalid unit")

def formula_choice():  # Handle formula selection
    formula = int(input("Calculation type [1=Rectangle, 2=Circle]: ").strip())
    if formula in EQUATIONS:
        return EQUATIONS[formula]()
    else:
        raise ValueError("Invalid formula choice")

def inches_to_feet(value, unit):
    unit = unit.strip().lower()
    if unit in ("inches", "inch" ,"in"):
        value = value / ONE_FOOT
        return value
    elif unit in ("feet", "foot" ,"ft"):
        return value
    else:
        raise ValueError("Invalid unit")

def get_object_measurement(prompt):
    value = float(input(f"{prompt}: ").strip())
    unit = input("Unit (inches or feet): ").strip()
    return value, unit


def area_rectangle():
    length, length_unit = get_object_measurement("Length")
    width, width_unit = get_object_measurement("Width")
    length_ft = inches_to_feet(length,length_unit)
    width_ft = inches_to_feet(width, width_unit)
    area_ft_sq = length_ft * width_ft
    return area_ft_sq

def area_circle():
    diameter, diameter_unit = get_object_measurement("Diameter")
    diameter_ft = inches_to_feet(diameter, diameter_unit)
    area_ft_sq = (math.pi / DIAMETER_SQUARED_DIVISOR) * diameter_ft ** 2
    return area_ft_sq

def final_calc_value(area_ft_sq, unit):  # Output final value in correct units
    print(f"{area_ft_sq:g} {unit}")

def run_area_calculator():
    area_ft_sq = formula_choice()
    unit = final_unit_choice()
    final_area = convert_area_output(unit, area_ft_sq)
    final_calc_value(final_area, unit)

EQUATIONS = {
    1 : area_rectangle,
    2 : area_circle,
    }