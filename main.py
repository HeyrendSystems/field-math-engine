from field_math_engine.cli import formula_choice
from field_math_engine.unit_helpers import convert_area_output
from field_math_engine.unit_helpers import final_calc_value, final_unit_choice
def run_area_calculator():
    area_ft_sq = formula_choice()
    unit = final_unit_choice()
    final_area = convert_area_output(unit, area_ft_sq)
    final_calc_value(final_area, unit)

if __name__ == "__main__":
    run_area_calculator()
