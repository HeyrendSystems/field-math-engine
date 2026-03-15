from field_math_engine.constants import WATER_HP_CONSTANT

def pump_horsepower(flow, total_dynamic_head, pump_effcieny):
    pump_hp = (
        (flow * total_dynamic_head)
    / (WATER_HP_CONSTANT * pump_effcieny)
)
    return pump_hp