from pico_calc.pico_hardware.oled_display import OLEDDisplay
from pico_calc.pico_hardware.keypad_input import KeypadInput
from pico_calc.geometry.pico_area import RectangleArea
display = OLEDDisplay(sda_pin=0, scl_pin=1)

area = RectangleArea()
oled= OLEDDisplay(sda_pin=0, scl_pin=1)

class MainMenu:
    def __init__(self, display):
        self.display = display
        self.menu_items = []
        self.index = 0
        self.state = "MENU"
        self.title = ""
        self.refresh_check = False
        
    def state_check(self):
        if self.state == "MENU":
            self.title = "Field Calc v1.0"
            self.menu_items = ["1.Area", "2.Volume"]
        elif self.state == "AREA":
            self.title = "Area Calc Menu"
            self.menu_items = ["1.Rectangle", "2.Circle"]
                       
    def handle_menu_keypress(self, key, keypad):
            self.handle_menu_navigation(key,keypad)
    
    def handle_menu_navigation(self, key, keypad):
        if key == "2":
            self.index = (self.index - 1) % len(self.menu_items)
            self.refresh_display()
        elif key == "8":
            self.index = (self.index + 1) % len(self.menu_items)
            self.refresh_display()
        if key == "#":
            keypad.confirmed = True
            return 

    def refresh_display(self):
        self.display.oled.fill(0)
        self.display.oled.text(str(self.title), 0, 0)
        self.display.oled.hline(0, 10, 128, 1)
        self.display.oled.write_list(self.menu_items, selected_index=self.index)
        self.display.oled.show()
            
    def main_menu(self, key, keypad, oled):
        if not self.refresh_check:
            self.state_check()
            self.refresh_display()
            self.refresh_check = True
            
        self.handle_menu_keypress(key, keypad)
        
        if key == "#" and keypad.confirmed and self.index == 0:
            keypad.confirmed = False
            self.refresh_check = False
            self.state = "AREA"
                
        elif key == "#" and keypad.confirmed and self.index == 1:
            keypad.confirmed = False
            self.refresh_check = False
            self.state = "VOLUME"
            
    def area_menu(self, key, keypad, oled):
        if not self.refresh_check:
            self.state_check()
            self.refresh_display()
            self.refresh_check = True
            
        self.handle_menu_keypress(key, keypad)
        
        if key == "#" and keypad.confirmed and self.index == 0:
            keypad.confirmed = False
            self.refresh_check = False
            self.state = "RECTANGLE"

                
        elif key == "#" and keypad.confirmed and self.index == 1:
            keypad.confirmed = False
            self.refresh_check = False
            self.state = "CIRCLE"
        
        
        
        
   
