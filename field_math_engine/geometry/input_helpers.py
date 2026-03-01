def get_object_measurement(prompt):
    value = float(input(f"{prompt}: ").strip())
    unit = input("Unit (inches or feet): ").strip()
    return value, unit