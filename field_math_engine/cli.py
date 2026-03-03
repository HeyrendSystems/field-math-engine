from field_math_engine.geometry.area import run_area_calculator
from field_math_engine.geometry.volume import run_volume_calc

def calculator_choice():
    command = input("Calculator [type: area or volume]: ").lower().strip()
    match command:
        case "area":
            run_area_calculator()
        case "volume":
            run_volume_calc()
        case _:
            print("Invalid option")