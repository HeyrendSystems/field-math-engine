
from field_math_engine.unit_helpers import get_number_format
from field_math_engine.constants import (
    FOOT_TO_METER,
    GALLON_PER_DAY,
    GALLON_PER_MIN,
    GALLON_PER_SEC,
    GALLON_PER_HOUR,
    ONE_FOOT,
)
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
            flow = flow / GALLON_PER_SEC
        case "3":
            flow = get_flow("Flow GPM")
            flow = flow / GALLON_PER_MIN
        case "4":
            flow = get_flow("Flow GPH")
            flow = flow / GALLON_PER_HOUR
        case "5":
            flow = get_flow("Flow GPD")
            flow = flow / GALLON_PER_DAY
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

def velocity_rate():
    area_of_shape = area_formula_choice()
    flow =  convert_flow_to_cfs()
    velocity = (flow / area_of_shape)
    return velocity



def run_velocity_calculator():
    velocity = velocity_rate()
    velocity, unit = final_velocity_unit(velocity)
    velocity = get_number_format(velocity)
    print(velocity,unit)