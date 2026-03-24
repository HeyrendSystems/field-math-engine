from machine import Pin, I2C
from pico_calc.geometry.pico_area import Area
from pico_calc.pico_hardware.keypad_input import KeypadInput
from pico_calc.pico_hardware.oled_display import OLEDDisplay
from pico_calc.main_menu import MainMenu
import gc
import time
import sys
import uselect

spoll = uselect.poll()
spoll.register(sys.stdin, uselect.POLLIN)

keypad = KeypadInput()
area = Area()
oled = OLEDDisplay()
menu = MainMenu(oled)
last_state = None

while True:
    
    if spoll.poll(0):
        key = sys.stdin.read(1)
    else:
        key = keypad.key_pad_scan()
        
    if key == "A":
        oled.shutdown_sequence()
        
    if menu.state != last_state:
        gc.collect()
        last_state = menu.state
        print(f"State changed to {menu.state}, memory cleaned!")
        
    if menu.state == "MENU":
        menu.main_menu(key, keypad, oled)
        
    elif menu.state == "AREA":
        menu.area_menu(key, keypad, oled, area)
        
    elif menu.state == "RECTANGLE":
        area.run_rectangle_area( key, keypad, oled, menu)
        
    elif menu.state == "CIRCLE":
        area.run_circle_area(key, keypad, oled, menu)
        
    elif menu.state == "VOLUME":
        print("Coming soon!")
 
    
                
        
        
    
   
