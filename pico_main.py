from machine import Pin, I2C
from pico_calc.geometry.pico_area import RectangleArea
from pico_calc.pico_hardware.keypad_input import KeypadInput
from pico_calc.pico_hardware.oled_display import OLEDDisplay
from pico_calc.main_menu import MainMenu
import time

keypad = KeypadInput()
area = RectangleArea()
oled = OLEDDisplay()
menu = MainMenu(oled)

while True:
    key = keypad.key_pad_scan()
    if menu.state == "MENU":
        menu.main_menu(key, keypad, oled)
    elif menu.state == "AREA":
        menu.area_menu(key, keypad, oled)
    elif menu.state == "RECTANGLE":
        area.run_rectangle_area( key, keypad, oled, menu)
    elif menu.state == "VOLUME":
        print("Coming soon!")
 
    
                
        
        
    
   
