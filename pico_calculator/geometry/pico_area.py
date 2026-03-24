from pico_calc.pico_hardware.oled_display import OLEDDisplay
import time
import math


class Area:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.calc_type = "Area"
        self.shape = None
        self.state = None
        self.length = None
        self.width = None
        self.diameter = None
        self.base = None
        self.area_ft_sq = None
        self.area_in_sq = None
        self.length_ft_label = None
        self.width_ft_label = None
        self.diameter_ft_label = None
        self.base_ft_label = None
        self.choice = None
        self.unit_check = False
        self.unit_prompt_shown = False
        self.unit = "ft"
        self.buffer_check = False
    
    def inches_to_feet(self, value):
        return value / 12

    def handle_length(self, key, keypad, oled):
        if not keypad.confirmed:
            title = f"{self.calc_type} {self.shape}"
            label = "ENTER Length"
            buffer = keypad.buffer
            oled.update_input(title,label, buffer)
            keypad.update_screen(key)
            print(f"Length: {buffer}")

        if key is not None and not keypad.confirmed and not keypad.exit:
            if key.isdigit():
                self.buffer_check = True
                title = f"{self.calc_type} {self.shape}"
                label = "ENTER Length"
                buffer = keypad.buffer
                oled.update_input(title,label, buffer)
                self.length = float(keypad.buffer)
                print(f"Length: {buffer}")
        if not self.buffer_check and keypad.confirmed:
            keypad.confirmed = False
            
        elif keypad.confirmed and not self.unit_prompt_shown and self.buffer_check:
            title = "LENGTH UNIT"
            label = f"[1=in, 2=ft]"
            buffer = keypad.buffer
            oled.update_input(title,label, buffer)
            self.unit_prompt_shown = True
            print("Get length unit check")
            
        elif keypad.confirmed and not self.unit_check:
            unit_choice = ["in", "ft"]
            if key == "1":
                self.length = float(self.inches_to_feet(self.length))
                self.unit_check = True
                self.length_ft_label = f"Len: {self.length:,.3g} {unit_choice[1]}"
                print(f"Length: {self.length:,.3g} {unit_choice[1]}")

            elif key == "2":
                self.unit_check = True
                self.length_ft_label = f"Len: {self.length:,.3g} {unit_choice[1]}"
                print(f"Length: {self.length:,.3g} {unit_choice[1]}")
                
        elif self.unit_check:
            keypad.buffer = ""
            keypad.confirmed = False
            self.unit_check = False
            self.unit_prompt_shown = False
            self.initialize = False
            self.buffer_check = False
            self.state = "GET WIDTH"
            print("Length complete")
            return
            
    def handle_width(self, key, keypad, oled):   
        if not keypad.confirmed:
            title = f"{self.calc_type} {self.shape}"
            label_one =f"{self.length_ft_label}"
            lable_two = "ENTER Width"
            buffer = keypad.buffer
            oled.update_input_double_label(title, label_one, lable_two, buffer)
            keypad.update_screen(key)
            print("Width: {buffer}")
            
        if key is not None and not keypad.confirmed:
            if key.isdigit():
                self.buffer_check = True
                title = f"{self.calc_type} {self.shape}"
                label_one =f"{self.length_ft_label}"
                lable_two = "ENTER Width"
                buffer = keypad.buffer
                oled.update_input_double_label(title, label_one, lable_two, buffer)
                self.width = float(keypad.buffer)
                print("Width: {buffer}")
        if not self.buffer_check and keypad.confirmed:
            keypad.confirmed = False
            
        elif keypad.confirmed and not self.unit_prompt_shown:
            title = "WIDTH UNIT"
            label = "[1=in, 2=ft]"
            buffer = keypad.buffer
            oled.update_input(title, label, buffer)
            self.unit_prompt_shown = True
            print("Get width units")
            return
        
        elif keypad.confirmed and not self.unit_check:
            unit_choice = ["in", "ft"]
            if key == "1":
                self.width = float(self.inches_to_feet(self.width))
                self.unit_check = True
                self.width_ft_label = f"W: {self.width:,.3g} {unit_choice[1]}"
                print(f"Width: {self.width:,.3g} {unit_choice[1]}")

            elif key == "2":
                self.unit_check = True
                self.width_ft_label = f"W: {self.width:,.3g} {unit_choice[1]}"
                print(f"Width: {self.width:,.3g} {unit_choice[1]}")
                
        elif self.unit_check:
            keypad.buffer = ""
            keypad.confirmed = False
            self.unit_prompt_shown = False
            self.unit_check = False
            self.buffer_check = False
            self.state = (f"GET RECTANGLE AREA")
            print("Width Complete")
            
    def handle_rectangle_area(self):
        self.area_ft_sq = self.length * self.width
        self.state = (f"GET FINAL UNITS")
        return
    
    def handle_area_circle(self):
        self.area_ft_sq = (math.pi / 4) * self.diameter ** 2
        self.state = (f"GET FINAL UNITS")
        return

    
    def handle_final_units(self, key, keypad, menu, oled):
        unit_dict = { "1":"ft sq", "2": "in sq"}
        if self.shape == "Rectangle":
            lable_two = f"{self.length_ft_label}"
            label_three = f"{self.width_ft_label}"
        elif self.shape == "Circle":
            lable_two = f"{self.diameter_ft_label}"
            label_three = ""
            
        if not self.unit_prompt_shown:
            title = f"Final Area Units"
            label_one =f"[1=ft sq, 2=in sq]"
            oled.update_input_double_label(title, label_one, lable_two, label_three)
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
                oled.update_input(title, label, label_two)
                if key == "A":
                    self.state = "EXIT CALCULATOR"
                elif key == "B":
                    self.reset()
                    menu.state = "MENU"
                
        elif self.unit_check and self.choice == "2":
                title = "Area Results"
                label = f"{self.area_in_sq:.5g} {unit_dict[self.choice]}"
                label_two = "[A=EXIT B=CONT.]"
                oled.update_input(title, label, label_two)
                if key == "A":
                    self.state = "EXIT CALCULATOR"
                elif key == "B":
                    self.reset()
                    menu.state = "MENU"
                
    # RUN Rectanlge Calc           
    def run_rectangle_area(self, key, keypad, oled, menu):
        if self.state == "GET LENGTH":
            self.handle_length(key, keypad, oled)
            
        elif self.state == "GET WIDTH":
            self.handle_width(key, keypad, oled)
            
        elif self.state == "GET RECTANGLE AREA":
            self.handle_rectangle_area()
            
        elif self.state == "GET FINAL UNITS":
            self.handle_final_units(key, keypad, menu, oled)
            
        elif self.state == "EXIT CALCULATOR":
            if key == "A":
                oled.shutdown_sequence()
                
    def run_circle_area(self, key, keypad, oled, menu):
        
        if self.state == "GET DIAMETER":
            self.handle_diameter(key, keypad, oled)
            
        elif self.state == "GET CIRCLE AREA":
            self.handle_area_circle()
            
        elif self.state == "GET FINAL UNITS":
            self.handle_final_units(key, keypad, menu, oled)
            
        elif self.state == "EXIT CALCULATOR":
            if key == "A":
                oled.shutdown_sequence()
            
            
        
            
        
    
    
    def handle_diameter(self, key, keypad, oled):
        if not keypad.confirmed:
            title = f"{self.calc_type} {self.shape}"
            label = "ENTER Diameter"
            buffer = keypad.buffer
            oled.update_input(title,label, buffer)
            keypad.update_screen(key)
            print(f"Length: {buffer}")  
        if key is not None and not keypad.confirmed and not keypad.exit:
            if key.isdigit():
                self.buffer_check = True
                title = f"{self.calc_type} {self.shape}"
                label = "ENTER Diamter"
                buffer = keypad.buffer
                oled.update_input(title,label, buffer)
                self.diameter = float(keypad.buffer)
                print(f"Length: {buffer}")
        if not self.buffer_check and keypad.confirmed:
            keypad.confirmed = False
            
        elif keypad.confirmed and not self.unit_prompt_shown and self.buffer_check:
            title = "Diameter UNIT"
            label = f"[1=in, 2=ft]"
            buffer = keypad.buffer
            oled.update_input(title,label, buffer)
            self.unit_prompt_shown = True
            print("Get diameter unit check")
            
        elif keypad.confirmed and not self.unit_check:
            unit_choice = ["in", "ft"]
            if key == "1":
                self.diameter = float(self.inches_to_feet(self.diameter))
                self.unit_check = True
                self.diameter_ft_label = f"D: {self.diameter:,.3g} {unit_choice[1]}"
                print(f"Diameter: {self.diameter:,.3g} {unit_choice[1]}")

            elif key == "2":
                self.unit_check = True
                self.diameter_ft_label = f"D: {self.diameter:,.3g} {unit_choice[1]}"
                print(f"Diameter: {self.diameter:,.3g} {unit_choice[1]}")
            
        elif self.unit_check:
            keypad.buffer = ""
            keypad.confirmed = False
            self.unit_check = False
            self.unit_prompt_shown = False
            self.initialize = False
            self.buffer_check = False
            self.state = "GET CIRCLE AREA"
            print("Diameter complete")
            return

        
        
    
        

            