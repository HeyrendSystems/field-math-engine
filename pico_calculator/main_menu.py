from machine import ADC
import time
from pico_calc.pico_hardware.oled_display import OLEDDisplay
from pico_calc.pico_hardware.keypad_input import KeypadInput
from pico_calc.geometry.pico_area import Area

class MainMenu:
    def __init__(self, oled):
        self.display = oled
        self.menu_items = []
        self.state = "MENU"
        self.title = ""
        self.refresh_check = False
        self.index = 0

    def state_check(self):
        if self.state == "MENU":
            self.title = "Field Calc v1.0"
            self.menu_items = ["1.Area", "2.Volume"]
        elif self.state == "AREA":
            self.title = "Area Calc Menu"
            self.menu_items = ["1.Rectangle", "2.Circle", "3.Trapeziod", "4.Triangle", "5.Ellipse","6.Annulus"]

    def handle_menu_keypress(self, key, keypad):
            self.handle_menu_navigation(key,keypad)

    def handle_menu_navigation(self, key, keypad):
        last_state = self.state
        pot = ADC(26)
        value = pot.read_u16()
        self.index = int(value * len(self.menu_items) / 65536)
        self.refresh_display()
        if self.index >= len(self.menu_items):
            self.index = len(self.menu_items) - 1
        if key == "2":
            self.index = (self.index - 1) % len(self.menu_items)
            self.refresh_display()
        elif key == "8":
            self.index = (self.index + 1) % len(self.menu_items)
            self.refresh_display()
        if key == "#":
            keypad.confirmed = True
            return
        print(f"value {value}")
        print(f"index {self.index}")
    def refresh_display(self):
        max_list_display = 4
        self.display.oled.fill(0)
        self.display.oled.text(str(self.title), 0, 0)
        self.display.oled.hline(0, 10, 128, 1)

        for index, item in enumerate(self.menu_items):

            if self.index < max_list_display:
                  self.display.oled.write_list(self.menu_items[0:max_list_display], selected_index=self.index)

            if self.index < max_list_display:
                self.display.oled.write_list(self.menu_items[0:max_list_display], selected_index=self.index)

            elif self.index >= max_list_display:

                self.display.oled.write_list(self.menu_items[max_list_display:], selected_index=self.index - max_list_display)




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

    def area_menu(self, key, keypad, oled, area):
        if not self.refresh_check:
            self.state_check()
            self.refresh_display()
            self.refresh_check = True

        self.handle_menu_keypress(key, keypad)

        if key == "#" and keypad.confirmed and self.index == 0:
            keypad.confirmed = False
            self.refresh_check = False
            area.state = "GET LENGTH"
            area.shape = "Rectangle"
            self.state = "RECTANGLE"


        elif key == "#" and keypad.confirmed and self.index == 1:
            keypad.confirmed = False
            self.refresh_check = False
            self.state = "CIRCLE"
            area.state = "GET DIAMETER"
            area.shape = "Circle"

        elif key == "#" and keypad.confirmed and self.index == 2:
            keypad.confirmed = False
            self.refresh_check = False
            self.state = "TRAPEZOID"
            area.state = "GET BASE ONE"
            area.shape = "Trapezoid"

        elif key == "#" and keypad.confirmed and self.index == 3:
            keypad.confirmed = False
            self.refresh_check = False
            self.state = "TRIANGLE"
            area.state = "GET BASE ONE"
            area.shape = "Triangle"

        elif key == "#" and keypad.confirmed and self.index == 4:
            keypad.confirmed = False
            self.refresh_check = False
            self.state = "ELLIPSE"
            area.state = "GET SEMI MAJOR AXIS"
            area.shape = "Ellipse"

        elif key == "#" and keypad.confirmed and self.index == 5:
            keypad.confirmed = False
            self.refresh_check = False
            self.state = "ANNULUS"
            area.state = "GET OUTSIDE DIAMETER"
            area.shape = "Annulus"