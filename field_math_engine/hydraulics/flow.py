from field_math_engine.constants import (
    GALLON_PER_DAY,
    GALLON_PER_MIN,
    GALLON_PER_SEC,
    GALLON_PER_HOUR,
)

from field_math_engine.geometry.area import (
    area_formula_choice,
)
from field_math_engine.unit_helpers import get_number_format

def get_velocity(prompt):
    value = float(input(f"{prompt}: ").strip())
    return value

def flow_rate():
    area_of_shape = area_formula_choice()
    velocity =  get_velocity("Velocity ft/s")
    flow = area_of_shape * velocity
    return flow

def flow_unit_choice(flow):
    command = input("Final units for flow [1=ft³/s, 2=GPS, 3=GPM, 4=GPH, 5=GPD]: ").strip().lower()
    match command:
        case "1":
            unit = "ft³/s"
            value = flow
        case "2":
            unit = "GPS"
            value = flow * GALLON_PER_SEC
        case "3":
            unit = "GPM"
            value = flow * GALLON_PER_MIN
        case "4":
            unit = "GPH"
            value = flow * GALLON_PER_HOUR
        case "5":
            unit = "GPD"
            value = flow * GALLON_PER_DAY
    return value, unit

def print_flow(value, unit):
    print(f"This is the flow {value} {unit}")

def run_flow_calculator():
    flow = flow_rate()
    value, unit = flow_unit_choice(flow)
    value = get_number_format(value)
    print_flow(value, unit)

