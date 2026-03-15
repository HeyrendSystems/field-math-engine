from field_math_engine.constants import PSI_TO_FT_HEAD
def friction_head_loss(pipe_length_ft, flow_rate_measurement, pipe_roughness, inside_diameter_inches):
    hazen_williams_friction_calc = (
        0.002083 * pipe_length_ft * ((100 / pipe_roughness) ** 1.852)
    * ((flow_rate_measurement ** 1.852) / (inside_diameter_inches ** 4.8655))
    )
    friction_loss_ft = hazen_williams_friction_calc
    return friction_loss_ft

def total_dynamic_head_calc(static_water_level_ft, destination_elevation_ft, pressure_head_ft, friction_loss_ft):
    hydraulic_grade_line = destination_elevation_ft + pressure_head_ft
    total_dynamic_head =  hydraulic_grade_line - static_water_level_ft + friction_loss_ft
    friction_psi = friction_loss_ft / PSI_TO_FT_HEAD

    return total_dynamic_head, friction_loss_ft, friction_psi