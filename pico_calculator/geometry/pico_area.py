from pico_calc.pico_hardware.oled_display import OLEDDisplay
import time

oled_screen = OLEDDisplay(sda_pin=0, scl_pin=1)

class RectangleArea:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.calc_type = "Area"
        self.shape = "Rectangle"
        self.state = "GET LENGTH"
        self.length = None
        self.width = None
        self.length_ft = None
        self.width_ft = None
        self.area_ft_sq = None
        self.area_in_sq = None
        self.length_ft_label = None
        self.width_ft_label = None
        self.choice = ""
        self.unit_check = False
        self.unit_prompt_shown = False
        self.unit = "ft"
    
    def inches_to_feet(self, value):
        return value / 12

    def handle_length(self, key, keypad):
        if not keypad.confirmed:
            title = f"{self.calc_type} {self.shape}"
            label = "ENTER Length"
            buffer = keypad.buffer
            oled_screen.update_input(title,label, buffer)
            keypad.update_screen(key)
            print(f"Length: {buffer}")

        if key is not None and not keypad.confirmed and not keypad.exit:
            if key.isdigit():
                title = f"{self.calc_type} {self.shape}"
                label = "ENTER Length"
                buffer = keypad.buffer
                oled_screen.update_input(title,label, buffer)
                self.length = float(keypad.buffer)
                print(f"Length: {buffer}")
            
        elif keypad.confirmed and not self.unit_prompt_shown:
            title = "LENGTH UNIT"
            label = f"[1=in, 2=ft]"
            buffer = keypad.buffer
            oled_screen.update_input(title,label, buffer)
            self.unit_prompt_shown = True
            print("Get length unit check")
        
        elif keypad.confirmed and not self.unit_check:
            unit_choice = ["in", "ft"]
            print(key)
            if key == "1":
                self.length_ft = float(self.inches_to_feet(self.length))
                self.unit_check = True
                self.length_ft_label = f"Len: {self.length_ft:,.3g} {unit_choice[1]}"
                print(f"Length: {self.length_ft:,.3g} {unit_choice[1]}")

            elif key == "2":
                self.length_ft = self.length
                self.unit_check = True
                self.length_ft_label = f"Len: {self.length_ft:,.3g} {unit_choice[1]}"
                print(f"Length: {self.length_ft:,.3g} {unit_choice[1]}")
            
        elif self.unit_check:
            keypad.buffer = ""
            keypad.confirmed = False
            self.unit_check = False
            self.unit_prompt_shown = False
            self.initialize = False
            self.state = "GET WIDTH"
            print("Length complete")
            return
            
    def handle_width(self, key, keypad):   
        if not keypad.confirmed:
            title = f"{self.calc_type} {self.shape}"
            label_one =f"{self.length_ft_label}"
            lable_two = "ENTER Width"
            buffer = keypad.buffer
            oled_screen.update_input_double_label(title, label_one, lable_two, buffer)
            keypad.update_screen(key)
            print("Width: {buffer}")
            
        if key is not None and not keypad.confirmed:
            if key.isdigit():
                title = f"{self.calc_type} {self.shape}"
                label_one =f"{self.length_ft_label}"
                lable_two = "ENTER Width"
                buffer = keypad.buffer
                oled_screen.update_input_double_label(title, label_one, lable_two, buffer)
                self.width = float(keypad.buffer)
                print("Width: {buffer}")
            
        elif keypad.confirmed and not self.unit_prompt_shown:
            title = "WIDTH UNIT"
            label = "[1=in, 2=ft]"
            buffer = keypad.buffer
            oled_screen.update_input(title, label, buffer)
            self.unit_prompt_shown = True
            print("Get width units")
            return
        
        elif keypad.confirmed and not self.unit_check:
            unit_choice = ["in", "ft"]
            if key == "1":
                self.width_ft = float(self.inches_to_feet(self.width))
                self.unit_check = True
                self.width_ft_label = f"W: {self.width_ft:,.3g} {unit_choice[1]}"
                print(f"Width: {self.length_ft:,.3g} {unit_choice[1]}")

            elif key == "2":
                self.width_ft = self.width
                self.unit_check = True
                self.width_ft_label = f"W: {self.width_ft:,.3g} {unit_choice[1]}"
                print(f"Width: {self.length_ft:,.3g} {unit_choice[1]}")
                
        elif self.unit_check:
            keypad.buffer = ""
            keypad.confirmed = False
            self.unit_prompt_shown = False
            self.unit_check = False
            self.state = (f"GET RECTANGLE AREA")
            print("Width Complete")
            
    def handle_rectangle_area(self):
        self.area_ft_sq = self.length_ft * self.width_ft
        self.state = (f"GET FINAL UNITS")
        return
    
    def handle_final_units(self, key, keypad, menu):
        unit_dict = { "1":"ft sq", "2": "in sq"}
        if not self.unit_prompt_shown:
            title = f"Final Area Units"
            label_one =f"[1=ft sq, 2=in sq]"
            lable_two = f"{self.length_ft_label}"
            label_three = f"{self.width_ft_label}"
            oled_screen.update_input_double_label(title, label_one, lable_two, label_three)
            self.unit_prompt_shown = True
            
        if not self.unit_check:
            if key == "1":
                self.choice = "1"
                self.unit_check = True
            elif key == "2":
                self.area_in_sq = float(self.area_ft_sq * 144)
                self.choice = "2"
                self.unit_check = True
                
        elif self.unit_check and self.choice == "1":
                title = "Area Results"
                label =f"{self.area_ft_sq:.5g} {unit_dict[self.choice]}"
                label_two = "[A=EXIT B=CONT.]"
                oled_screen.update_input(title, label, label_two)
                if key == "A":
                    self.state = "EXIT CALCULATOR"
                elif key == "B":
                    self.reset()
                    menu.state = "MENU"
                
        elif self.unit_check and self.choice == "2":
                title = "Area Results"
                label = f"{self.area_in_sq:.5g} {unit_dict[self.choice]}"
                label_two = "[A=EXIT B=CONT.]"
                oled_screen.update_input(title, label, label_two)
                if key == "A":
                    self.state = "EXIT CALCULATOR"
                elif key == "B":
                    self.reset()
                    menu.state = "MENU"
                
                
    def run_rectangle_area(self, key, keypad, oled, menu):
        if self.state == "GET LENGTH":
            if key == "A":
                oled.shutdown_sequence()
            self.handle_length(key, keypad)
            
        elif self.state == "GET WIDTH":
            if key == "A":
                oled.shutdown_sequence()
            self.handle_width(key, keypad)
            
        elif self.state == "GET RECTANGLE AREA":
            if key == "A":
                oled.shutdown_sequence()
            self.handle_rectangle_area()
            
        elif self.state == "GET FINAL UNITS":
            if key == "A":
                oled.shutdown_sequence()
            self.handle_final_units(key,keypad,menu)
            
        elif self.state == "EXIT CALCULATOR":
            if key == "A":
                oled.shutdown_sequence()
        
                
                                         
        
        
        
        

            