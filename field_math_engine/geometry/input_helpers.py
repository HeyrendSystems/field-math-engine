from field_math_engine.constants import PSI_TO_FT_HEAD

def get_object_measurement(prompt):
    value = float(input(f"{prompt}: ").strip())
    unit = input("Unit (inches or feet): ").strip()
    return value, unit

def get_psi_measurement(prompt):
    value = float(input(f"{prompt}: ").strip())
    return value

def pressure_head(psi_value):
    return psi_value * PSI_TO_FT_HEAD

