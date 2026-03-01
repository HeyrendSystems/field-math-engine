from field_math_engine.geometry import EQUATIONS

def formula_choice():  # Handle formula selection
    formula = int(input("Area Calculation type [1=Rectangle, 2=Circle, 3 = Trapizoid, 4 = Trianlge, 5 = Eclipse]: ").strip())
    if formula in EQUATIONS:
        return EQUATIONS[formula]()
    else:
        raise ValueError("Invalid formula choice")