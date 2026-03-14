import math
from ..constants import DIAMETER_SQUARED_DIVISOR

def area_rectangle(length_ft, width_ft):
    area_ft_sq = length_ft * width_ft
    return area_ft_sq

def area_circle(diameter_ft,):
    area_ft_sq = (math.pi / DIAMETER_SQUARED_DIVISOR) * diameter_ft ** 2
    return area_ft_sq

def area_trapezoid(base_one_ft, base_two_ft, height_ft):
    area_ft_sq = ((base_one_ft + base_two_ft) * height_ft ) / 2
    return area_ft_sq

def area_triangle(base_ft, height_ft):
    area_ft_sq = (base_ft * height_ft) * 0.5
    return area_ft_sq

def area_ellipse(semi_major_axis_ft, semi_minor_axis_ft):
    area_ft_sq = (math.pi * semi_major_axis_ft * semi_minor_axis_ft)
    return area_ft_sq

def area_annulus(outside_diameter_ft, inside_diameter_ft):
    if outside_diameter_ft < inside_diameter_ft:
        raise ValueError("Outside diameter cannot be less than inside diameter.")
    else:
        area_ft_sq = (
            (math.pi/ DIAMETER_SQUARED_DIVISOR)
            * (outside_diameter_ft ** 2 - inside_diameter_ft ** 2)
            )
    return area_ft_sq



AREA_EQUATIONS = {
    1: area_rectangle,
    2: area_circle,
    3: area_trapezoid,
    4: area_triangle,
    5: area_ellipse,
    6: area_annulus
    }