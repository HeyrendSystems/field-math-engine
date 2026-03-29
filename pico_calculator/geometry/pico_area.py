from pico_calc.pico_hardware.oled_display import OLEDDisplay
import time
import math


class Area:
    def __init__(self):
        self.reset()

    def reset(self):
        self.calc_type = "Area"
        self.label_one = None
        self.label_two = None
        self.label_three = None
        self.shape = None
        self.state = None
        self.length = None
        self.width = None
        self.diameter = None
        self.base_one = None
        self.base_two = None
        self.height = None
        self.semi_major_axis = None
        self.semi_minor_axis = None
        self.outside_diameter = None
        self.inside_diameter = None
        self.area_ft_sq = None
        self.area_in_sq = None
        self.length_ft_label = None
        self.width_ft_label = None
        self.diameter_ft_label = None
        self.base_one_ft_label = None
        self.base_two_ft_label = None
        self.height_ft_label = None
        self.semi_major_axis_ft_label = None
        self.semi_minor_axis_ft_label = None
        self.inside_diameter_ft_label = None
        self.outside_diameter_ft_label = None
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
                self.length_ft_label = f"L: {self.length:,.5g} {unit_choice[1]}"
                print(f"Length: {self.length:,.5g} {unit_choice[1]}")

            elif key == "2":
                self.unit_check = True
                self.length_ft_label = f"L: {self.length:,.5g} {unit_choice[1]}"
                print(f"Length: {self.length:,.5g} {unit_choice[1]}")

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
            oled.update_input_three_label(title, label_one, lable_two, buffer)
            keypad.update_screen(key)
            print("Width: {buffer}")

        if key is not None and not keypad.confirmed:
            if key.isdigit():
                self.buffer_check = True
                title = f"{self.calc_type} {self.shape}"
                label_one =f"{self.length_ft_label}"
                lable_two = "ENTER Width"
                buffer = keypad.buffer
                oled.update_input_three_label(title, label_one, lable_two, buffer)
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
                self.width_ft_label = f"W: {self.width:,.5g} {unit_choice[1]}"
                print(f"Width: {self.width:,.5g} {unit_choice[1]}")

            elif key == "2":
                self.unit_check = True
                self.width_ft_label = f"W: {self.width:,.5g} {unit_choice[1]}"
                print(f"Width: {self.width:,.5g} {unit_choice[1]}")

        elif self.unit_check:
            keypad.buffer = ""
            keypad.confirmed = False
            self.unit_prompt_shown = False
            self.unit_check = False
            self.buffer_check = False
            self.state = (f"GET RECTANGLE AREA")
            print("Width Complete")

    def handle_diameter(self, key, keypad, oled):
        if not keypad.confirmed:
            title = f"{self.calc_type} {self.shape}"
            label = "ENTER Diameter"
            buffer = keypad.buffer
            oled.update_input(title,label, buffer)
            keypad.update_screen(key)
            print(f"Diameter: {buffer}")
        if key is not None and not keypad.confirmed and not keypad.exit:
            if key.isdigit():
                self.buffer_check = True
                title = f"{self.calc_type} {self.shape}"
                label = "ENTER Diamter"
                buffer = keypad.buffer
                oled.update_input(title,label, buffer)
                self.diameter = float(keypad.buffer)
                print(f"Diameter: {buffer}")

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
                self.diameter_ft_label = f"D: {self.diameter:,.5g} {unit_choice[1]}"
                print(f"Diameter: {self.diameter:,.5g} {unit_choice[1]}")

            elif key == "2":
                self.unit_check = True
                self.diameter_ft_label = f"D: {self.diameter:,.5g} {unit_choice[1]}"
                print(f"Diameter: {self.diameter:,.5g} {unit_choice[1]}")

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

    def handle_base_one(self, key, keypad, oled):
        if not keypad.confirmed:
            title = f"{self.calc_type} {self.shape}"
            label = "ENTER Base"
            buffer = keypad.buffer
            oled.update_input(title,label, buffer)
            keypad.update_screen(key)
            print(f"base_one: {buffer}")
        if key is not None and not keypad.confirmed and not keypad.exit:
            if key.isdigit():
                self.buffer_check = True
                title = f"{self.calc_type} {self.shape}"
                label = "ENTER Base"
                buffer = keypad.buffer
                oled.update_input(title,label, buffer)
                self.base_one = float(keypad.buffer)
                print(f"Base: {buffer}")

        if not self.buffer_check and keypad.confirmed:
            keypad.confirmed = False

        elif keypad.confirmed and not self.unit_prompt_shown and self.buffer_check:
            title = "Base UNIT"
            label = f"[1=in, 2=ft]"
            buffer = keypad.buffer
            oled.update_input(title,label, buffer)
            self.unit_prompt_shown = True
            print("Get  unit check")

        elif keypad.confirmed and not self.unit_check:
            unit_choice = ["in", "ft"]
            if key == "1":
                self.base_one = float(self.inches_to_feet(self.base_one))
                self.unit_check = True
                self.base_one_ft_label = f"B1: {self.base_one:,.5g} {unit_choice[1]}"
                print(f"Base: {self.base_one:,.5g} {unit_choice[1]}")

            elif key == "2":
                self.unit_check = True
                self.diameter_ft_label = f"B1: {self.base_one:,.5g} {unit_choice[1]}"
                print(f"Base: {self.base_one:,.5g} {unit_choice[1]}")

        elif self.unit_check:
            if self.shape == "Trapezoid":
                self.state = f"GET {self.shape} BASE TWO"

            elif self.shape == "Triangle":
                self.state = f"GET {self.shape} HEIGHT"
                print(f"{self.shape} base complete")

            keypad.buffer = ""
            keypad.confirmed = False
            self.unit_check = False
            self.unit_prompt_shown = False
            self.initialize = False
            self.buffer_check = False
            print(self.state)
            return

    def handle_base_two(self, key, keypad, oled):
        if not keypad.confirmed:
            title = f"{self.calc_type} {self.shape}"
            label = "ENTER Base Two"
            buffer = keypad.buffer
            oled.update_input(title,label, buffer)
            keypad.update_screen(key)
            print(f"Base Two: {buffer}")
        if key is not None and not keypad.confirmed and not keypad.exit:
            if key.isdigit():
                self.buffer_check = True
                title = f"{self.calc_type} {self.shape}"
                label = "ENTER Base Two"
                buffer = keypad.buffer
                oled.update_input(title,label, buffer)
                self.base_two = float(keypad.buffer)
                print(f"Base two: {buffer}")

        if not self.buffer_check and keypad.confirmed:
            keypad.confirmed = False

        elif keypad.confirmed and not self.unit_prompt_shown and self.buffer_check:
            title = "Base two UNIT"
            label = f"[1=in, 2=ft]"
            buffer = keypad.buffer
            oled.update_input(title,label, buffer)
            self.unit_prompt_shown = True
            print("Get base two unit check")

        elif keypad.confirmed and not self.unit_check:
            unit_choice = ["in", "ft"]
            if key == "1":
                self.base_two = float(self.inches_to_feet(self.base_two))
                self.unit_check = True
                self.base_two_ft_label = f"B2: {self.base_two:,.5g} {unit_choice[1]}"
                print(f"B2: {self.base_two:,.5g} {unit_choice[1]}")

            elif key == "2":
                self.unit_check = True
                self.base_two_ft_label = f"Base two: {self.base_two:,.5g} {unit_choice[1]}"
                print(f"Base two: {self.base_two:,.5g} {unit_choice[1]}")

        elif self.unit_check:
            keypad.buffer = ""
            keypad.confirmed = False
            self.unit_check = False
            self.unit_prompt_shown = False
            self.initialize = False
            self.buffer_check = False
            self.state = f"GET {self.shape} HEIGHT"
            print("Base Two complete")
            return

    def handle_height(self, key, keypad, oled):
        if not keypad.confirmed:
            title = f"{self.calc_type} {self.shape}"
            label = "ENTER Height"
            buffer = keypad.buffer
            oled.update_input(title,label, buffer)
            keypad.update_screen(key)
            print(f"Height: {buffer}")
        if key is not None and not keypad.confirmed and not keypad.exit:
            if key.isdigit():
                self.buffer_check = True
                title = f"{self.calc_type} {self.shape}"
                label = "ENTER Height"
                buffer = keypad.buffer
                oled.update_input(title,label, buffer)
                self.height = float(keypad.buffer)
                print(f"Height: {buffer}")

        if not self.buffer_check and keypad.confirmed:
            keypad.confirmed = False

        elif keypad.confirmed and not self.unit_prompt_shown and self.buffer_check:
            title = "Height UNIT"
            label = f"[1=in, 2=ft]"
            buffer = keypad.buffer
            oled.update_input(title,label, buffer)
            self.unit_prompt_shown = True
            print("Get base unit check")

        elif keypad.confirmed and not self.unit_check:
            unit_choice = ["in", "ft"]
            if key == "1":
                self.height = float(self.inches_to_feet(self.height))
                self.unit_check = True
                self.height_ft_label = f"H: {self.height:,.5g} {unit_choice[1]}"
                print(f"Height: {self.height:,.5g} {unit_choice[1]}")

            elif key == "2":
                self.unit_check = True
                self.height_ft_label = f"H: {self.height:,.5g} {unit_choice[1]}"
                print(f"Height: {self.height:,.5g} {unit_choice[1]}")

        elif self.unit_check:
            keypad.buffer = ""
            keypad.confirmed = False
            self.unit_check = False
            self.unit_prompt_shown = False
            self.initialize = False
            self.buffer_check = False
            self.state = f"GET {self.shape} AREA"
            print(f"Height {self.shape} complete")
            print(self.state)
            return

    def handle_semi_major_axis(self, key, keypad, oled):
        if not keypad.confirmed:
            title = f"{self.calc_type} {self.shape}"
            label = "ENTER Semi Major Axis"
            buffer = keypad.buffer
            oled.update_input(title,label, buffer)
            keypad.update_screen(key)
            print(f"Semi Major Axis: {buffer}")
        if key is not None and not keypad.confirmed and not keypad.exit:
            if key.isdigit():
                self.buffer_check = True
                title = f"{self.calc_type} {self.shape}"
                label = "ENTER Semi Major Axis"
                buffer = keypad.buffer
                oled.update_input(title,label, buffer)
                self.semi_major_axis = float(keypad.buffer)
                print(f"Semi Major Axis: {buffer}")

        if not self.buffer_check and keypad.confirmed:
            keypad.confirmed = False

        elif keypad.confirmed and not self.unit_prompt_shown and self.buffer_check:
            title = "Semi Major Axis UNIT"
            label = f"[1=in, 2=ft]"
            buffer = keypad.buffer
            oled.update_input(title,label, buffer)
            self.unit_prompt_shown = True
            print("Get base unit check")

        elif keypad.confirmed and not self.unit_check:
            unit_choice = ["in", "ft"]
            if key == "1":
                self.semi_major_axis = float(self.inches_to_feet(self.semi_major_axis))
                self.unit_check = True
                self.semi_major_axis_ft_label = f"Maj: {self.semi_major_axis:,.5g} {unit_choice[1]}"
                print(f"Semi Major Axis: {self.semi_major_axis:,.5g} {unit_choice[1]}")

            elif key == "2":
                self.unit_check = True
                self.semi_major_axis_ft_label = f"Maj: {self.semi_major_axis:,.5g} {unit_choice[1]}"
                print(f"Semi Major Axis: {self.semi_major_axis:,.5g} {unit_choice[1]}")

        elif self.unit_check:
            keypad.buffer = ""
            keypad.confirmed = False
            self.unit_check = False
            self.unit_prompt_shown = False
            self.initialize = False
            self.buffer_check = False
            self.state = f"GET {self.shape} SEMI MINOR AXIS"
            print(f"Semi Major Axis {self.shape} complete")
            print(self.state)
            return

    def handle_semi_minor_axis(self, key, keypad, oled):
        if not keypad.confirmed:
            title = f"{self.calc_type} {self.shape}"
            label = "ENTER Semi Minor Axis"
            buffer = keypad.buffer
            oled.update_input(title,label, buffer)
            keypad.update_screen(key)
            print(f"Semi Minor Axis: {buffer}")
        if key is not None and not keypad.confirmed and not keypad.exit:
            if key.isdigit():
                self.buffer_check = True
                title = f"{self.calc_type} {self.shape}"
                label = "ENTER Semi Minor Axis"
                buffer = keypad.buffer
                oled.update_input(title,label, buffer)
                self.semi_minor_axis = float(keypad.buffer)
                print(f"Semi Minor Axis: {buffer}")

        if not self.buffer_check and keypad.confirmed:
            keypad.confirmed = False

        elif keypad.confirmed and not self.unit_prompt_shown and self.buffer_check:
            title = "Semi Minor Axis UNIT"
            label = f"[1=in, 2=ft]"
            buffer = keypad.buffer
            oled.update_input(title,label, buffer)
            self.unit_prompt_shown = True
            print("Get base unit check")

        elif keypad.confirmed and not self.unit_check:
            unit_choice = ["in", "ft"]
            if key == "1":
                self.semi_minor_axis = float(self.inches_to_feet(self.semi_minor_axis))
                self.unit_check = True
                self.semi_minor_axis_ft_label = f"Min: {self.semi_minor_axis:,.5g} {unit_choice[1]}"
                print(f"Semi Minor Axis: {self.semi_minor_axis:,.5g} {unit_choice[1]}")

            elif key == "2":
                self.unit_check = True
                self.semi_minor_axis_ft_label = f"Min: {self.semi_minor_axis:,.5g} {unit_choice[1]}"
                print(f"Semi Minor Axis: {self.semi_minor_axis:,.5g} {unit_choice[1]}")

        elif self.unit_check:
            keypad.buffer = ""
            keypad.confirmed = False
            self.unit_check = False
            self.unit_prompt_shown = False
            self.initialize = False
            self.buffer_check = False
            self.state = f"GET {self.shape} AREA"
            print(f"Semi Minor Axis {self.shape} complete")
            return

    def handle_outside_diameter(self, key, keypad, oled):
        if not keypad.confirmed:
            title = f"{self.calc_type} {self.shape}"
            label = "ENTER Outside Diameter"
            buffer = keypad.buffer
            oled.update_input(title,label, buffer)
            keypad.update_screen(key)
            print(f"Outside Diameter: {buffer}")
        if key is not None and not keypad.confirmed and not keypad.exit:
            if key.isdigit():
                self.buffer_check = True
                title = f"{self.calc_type} {self.shape}"
                label = "ENTER Outside Diameter"
                buffer = keypad.buffer
                oled.update_input(title,label, buffer)
                self.outside_diameter = float(keypad.buffer)
                print(f"Outside Diameter: {buffer}")

        if not self.buffer_check and keypad.confirmed:
            keypad.confirmed = False

        elif keypad.confirmed and not self.unit_prompt_shown and self.buffer_check:
            title = "Outside Diameter UNIT"
            label = f"[1=in, 2=ft]"
            buffer = keypad.buffer
            oled.update_input(title,label, buffer)
            self.unit_prompt_shown = True
            print("Get base unit check")

        elif keypad.confirmed and not self.unit_check:
            unit_choice = ["in", "ft"]
            if key == "1":
                self.outside_diameter = float(self.inches_to_feet(self.outside_diameter))
                self.unit_check = True
                self.outside_diameter_ft_label = f"Outside Diameter: {self.outside_diameter:,.3g} {unit_choice[1]}"
                print(f"Outside Diameter: {self.outside_diameter:,.3g} {unit_choice[1]}")

            elif key == "2":
                self.unit_check = True
                self.outside_diameter_ft_label = f"Outside Diameter: {self.outside_diameter:,.3g} {unit_choice[1]}"
                print(f"Outside Diameter: {self.outside_diameter:,.3g} {unit_choice[1]}")

        elif self.unit_check:
            keypad.buffer = ""
            keypad.confirmed = False
            self.unit_check = False
            self.unit_prompt_shown = False
            self.initialize = False
            self.buffer_check = False
            self.state = f"GET INSIDE DIAMETER"
            print(f"Outside Diameter {self.shape} complete")
            print(self.state)
            return
    def handle_inside_diameter(self, key, keypad, oled):
        if not keypad.confirmed:
            title = f"{self.calc_type} {self.shape}"
            label = "ENTER Inside Diameter"
            buffer = keypad.buffer
            oled.update_input(title,label, buffer)
            keypad.update_screen(key)
            print(f"Inside Diameter: {buffer}")
        if key is not None and not keypad.confirmed and not keypad.exit:
            if key.isdigit():
                self.buffer_check = True
                title = f"{self.calc_type} {self.shape}"
                label = "ENTER Inside Diameter"
                buffer = keypad.buffer
                oled.update_input(title,label, buffer)
                self.inside_diameter = float(keypad.buffer)
                print(f"Inside Diameter: {buffer}")

        if not self.buffer_check and keypad.confirmed:
            keypad.confirmed = False

        elif keypad.confirmed and not self.unit_prompt_shown and self.buffer_check:
            title = "Inside Diameter UNIT"
            label = f"[1=in, 2=ft]"
            buffer = keypad.buffer
            oled.update_input(title,label, buffer)
            self.unit_prompt_shown = True
            print("Get base unit check")

        elif keypad.confirmed and not self.unit_check:
            unit_choice = ["in", "ft"]
            if key == "1":
                self.inside_diameter = float(self.inches_to_feet(self.inside_diameter))
                self.unit_check = True
                self.inside_diameter_ft_label = f"Inside Diameter: {self.inside_diameter:,.3g} {unit_choice[1]}"
                print(f"Inside Diameter: {self.inside_diameter:,.3g} {unit_choice[1]}")

            elif key == "2":
                self.unit_check = True
                self.inside_diameter_ft_label = f"Inside Diameter: {self.inside_diameter:,.3g} {unit_choice[1]}"
                print(f"Inside Diameter: {self.inside_diameter:,.3g} {unit_choice[1]}")

        elif self.unit_check:
            keypad.buffer = ""
            keypad.confirmed = False
            self.unit_check = False
            self.unit_prompt_shown = False
            self.initialize = False
            self.buffer_check = False
            self.state = f"GET {self.shape} AREA"
            print(f"Inside Diameter {self.shape} complete")
            print(self.state)
            return

    def handle_rectangle_area(self):
        self.area_ft_sq = self.length * self.width
        self.state = (f"GET FINAL UNITS")
        return

    def handle_circle_area(self):
        self.area_ft_sq = (math.pi / 4) * self.diameter ** 2
        self.state = (f"GET FINAL UNITS")
        return

    def handle_trapezoid_area(self):
        self.area_ft_sq = ((self.base_one + self.base_two) * self.height ) / 2
        self.state = (f"GET FINAL UNITS")
        return

    def handle_triangle_area(self):
        self.area_ft_sq = (self.base_one * self.height) * 0.5
        self.state = (f"GET FINAL UNITS")
        return
    def handle_ellipse_area(self):
        self.area_ft_sq = (math.pi * self.semi_major_axis * self.semi_minor_axis)
        self.state = (f"GET FINAL UNITS")
        return self.area_ft_sq

    def handle_annulus_area(self):
        self.area_ft_sq = (
            (math.pi/ 4)
            * (self.outside_diameter ** 2 - self.inside_diameter ** 2)
            )
        self.state = (f"GET FINAL UNITS")
        return self.area_ft_sq

    def handle_final_units(self, key, keypad, menu, oled):
        unit_dict = { "1":"ft sq", "2": "in sq"}
        print(self.shape)
        if self.shape == "Rectangle" and not self.unit_prompt_shown:
            title = f"Final Area Units"
            label_one = f"[1=ft sq, 2=in sq]"
            label_two = f"{self.length_ft_label}"
            label_three = f"{self.width_ft_label}"
            oled.update_input_three_label(title, label_one, label_two, label_three)
            self.unit_prompt_shown = True
        elif self.shape == "Circle" and not self.unit_prompt_shown:
            title = f"Final Area Units"
            label_one = f"[1=ft sq, 2=in sq]"
            label_two = f"{self.diameter_ft_label}"
            label_three = ""
            oled.update_input_three_label(title, label_one, label_two, label_three)
            self.unit_prompt_shown = True
        elif self.shape == "Trapezoid" and not self.unit_prompt_shown:
            title = f"Final Area Units"
            label_one = f"[1=ft sq, 2=in sq]"
            label_two = f"{self.base_one_ft_label}"
            label_three = f"{self.base_two_ft_label}"
            label_four = f"{self.height_ft_label}"
            oled.update_input_four_labels(title, label_one, label_two, label_three, label_four)
            self.unit_prompt_shown = True
        elif self.shape == "Triangle" and not self.unit_prompt_shown:
            title = f"Final Area Units"
            label_one = f"[1=ft sq, 2=in sq]"
            label_two = f"{self.base_one_ft_label}"
            label_three = f"{self.height_ft_label}"
            oled.update_input_three_label(title, label_one, label_two, label_three)
            self.unit_prompt_shown = True

        elif self.shape == "Ellipse" and not self.unit_prompt_shown:
            title = f"Final Area Units"
            label_one = f"[1=ft sq, 2=in sq]"
            label_two = f"{self.semi_major_axis_ft_label}"
            label_three = f"{self.semi_minor_axis_ft_label}"
            oled.update_input_three_label(title, label_one, label_two, label_three)
            self.unit_prompt_shown = True

        elif self.shape == "Annulus" and not self.unit_prompt_shown:
            title = f"Final Area Units"
            label_one = f"[1=ft sq, 2=in sq]"
            label_two = f"{self.outside_diameter_ft_label}"
            label_three = f"{self.inside_diameter_ft_label}"
            oled.update_input_three_label(title, label_one, label_two, label_three)
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
            self.handle_circle_area()

        elif self.state == "GET FINAL UNITS":
            self.handle_final_units(key, keypad, menu, oled)

        elif self.state == "EXIT CALCULATOR":
            if key == "A":
                oled.shutdown_sequence()


    def run_trapezoid_area(self, key, keypad, oled, menu):
        if self.state == "GET BASE ONE":
            self.handle_base_one(key, keypad, oled)

        elif self.state == "GET Trapezoid BASE TWO":
            self.handle_base_two(key, keypad, oled)

        elif self.state == "GET Trapezoid HEIGHT":
            self.handle_height(key, keypad, oled)

        elif self.state == "GET Trapezoid AREA":
            self.handle_trapezoid_area()

        elif self.state == "GET FINAL UNITS":
            self.handle_final_units(key, keypad, menu, oled)

        elif self.state == "EXIT CALCULATOR":
            if key == "A":
                oled.shutdown_sequence()

    def run_triangle_area(self, key, keypad, oled, menu):
        if self.state == "GET BASE ONE":
            self.handle_base_one(key, keypad, oled)

        elif self.state == "GET Triangle HEIGHT":
            self.handle_height(key, keypad, oled)

        elif self.state == "GET Triangle AREA":
            self.handle_triangle_area()

        elif self.state == "GET FINAL UNITS":
            self.handle_final_units(key, keypad, menu, oled)

        elif self.state == "EXIT CALCULATOR":
            if key == "A":
                oled.shutdown_sequence()

    def run_ellipse_area(self, key, keypad, oled, menu):
        if self.state == f"GET SEMI MAJOR AXIS":
            self.handle_semi_major_axis(key, keypad, oled)

        elif self.state == f"GET SEMI MINOR AXIS":
            self.handle_semi_minor_axis(key, keypad, oled)

        elif self.state == "GET Ellipse AREA":
            self.handle_ellipse_area()

        elif self.state == "GET FINAL UNITS":
            self.handle_final_units(key, keypad, menu, oled)

        elif self.state == "EXIT CALCULATOR":
            if key == "A":
                oled.shutdown_sequence()

    def run_annulus_area(self, key, keypad, oled, menu):
        if self.state == "GET OUTSIDE DIAMETER":
            self.handle_outside_diameter(key, keypad, oled)

        elif self.state == f"GET INSIDE DIAMETER":
            self.handle_inside_diameter(key, keypad, oled)

        elif self.state == "GET Annulus AREA":
            if self.outside_diameter < self.inside_diameter:
                raise ValueError("Outside diameter cannot be less than inside diameter.")
            else:
                self.handle_annulus_area()

        elif self.state == "GET FINAL UNITS":
            self.handle_final_units(key, keypad, menu, oled)

        elif self.state == "EXIT CALCULATOR":
            if key == "A":
                oled.shutdown_sequence()