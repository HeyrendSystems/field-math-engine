import math
from ..constants import DIAMETER_CUBED_DIVISOR,DIAMETER_SQUARED_DIVISOR
from field_math_engine.geometry.area import area_circle

def volume_cube(length_ft):
    volume_cu_ft = length_ft ** 3
    return volume_cu_ft

def volume_rectangle_prism(length_ft, height_ft, width_ft):
    volume_cu_ft = length_ft * height_ft * width_ft
    return volume_cu_ft

def volume_sphere(diameter_ft):
    volume_cb_ft =  (math.pi / DIAMETER_CUBED_DIVISOR) * diameter_ft ** 3
    return volume_cb_ft

def volume_hemisphere(diameter_ft):
    return volume_sphere(diameter_ft) / 2

def volume_cylinder(diameter_ft, height_ft):
    area_sq_ft = area_circle(diameter_ft,)
    volume_cb_ft = area_sq_ft * height_ft
    return volume_cb_ft

def volume_annulus(outside_diameter_ft, inside_diameter_ft, height_ft):
    volume_cb_ft = (
        (math.pi/ DIAMETER_SQUARED_DIVISOR)
        * (outside_diameter_ft ** 2 - inside_diameter_ft ** 2)
        * height_ft
    )
    return volume_cb_ft

VOLUME_EQUATIONS = {

1: volume_rectangle_prism,
2: volume_cube,
3: volume_sphere,
4: volume_hemisphere,
5: volume_cylinder,
6: volume_annulus,
    }


