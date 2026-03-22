from pico_calc.oled_display import OLEDDisplay
from pico_calc.keypad_input import KeypadInput
from pico_calc.pico_area import RectangleArea
display = OLEDDisplay(sda_pin=0, scl_pin=1)

area = RectangleArea()
oled= OLEDDisplay(sda_pin=0, scl_pin=1)

class MainMenu:
    def __init__(self, display):
        self.display = display
        self.menu_items = ["1.Area", "2.Volume"]
        self.index = 0
        self.state = "MENU"
               
    def handle_menu_keypress(self, key, keypad):
        if self.state == "MENU":
            self.hanlde_menu_navigation(key,keypad)
    
    def hanlde_menu_navigation(self, key, keypad):
        if key == "A":
            self.index = (self.index - 1) % len(self.menu_items)
            self.refresh_display()
        elif key == "B":
            self.index = (self.index + 1) % len(self.menu_items)
            self.refresh_display()
        if key == "#":
            keypad.confirmed = True
            return 

    def refresh_display(self,title="Field Calc v1.0"):
        self.display.oled.fill(0)
        self.display.oled.text(str(title), 0, 0)
        self.display.oled.hline(0, 10, 128, 1)
        self.display.oled.write_list(self.menu_items, selected_index=self.index)
        self.display.oled.show()
            
    def main_menu(self, key, keypad, oled):
        self.refresh_display()
        self.handle_menu_keypress(key, keypad)
        print(self.index)
        if key == "#" and keypad.confirmed and self.index == 0:
                self.state = "AREA"
                keypad.confirmed = False
        elif key == "#" and keypad.confirmed and self.index == 1:
            self.state = "VOLUME"
            keypad.confirmed = False
            
        
        
        
   
