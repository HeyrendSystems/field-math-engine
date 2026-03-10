from field_math_engine.geometry.area import run_area_calculator
from field_math_engine.geometry.volume import run_volume_calc
from field_math_engine.hydraulics.flow import run_flow_calculator
from field_math_engine.hydraulics.veloctiy import run_velocity_calculator

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