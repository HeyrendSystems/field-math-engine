from machine import Pin, I2C
import pico_calc.drivers.sh1106
import time
class OLEDDisplay:
    def __init__(self, sda_pin=0, scl_pin=1):
        self.i2c = I2C(0, sda=Pin(sda_pin), scl=Pin(scl_pin), freq=400000)
        self.oled = pico_calc.drivers.sh1106.SH1106_I2C(128, 64, self.i2c, addr=0x3c)
        time.sleep(2)
        
        try:
            self.oled.sleep(True)
            self.oled.sleep(False)
            self.oled.fill(0)
            self.oled.show()
           
        except Exception as e:
            print(f"OLED Hardware Error: {e}")

    def show_header(self, title):
        self.oled.text(title, 0, 0)
        self.oled.hline(0, 10, 128, 1)
    
    def update_input(self,title, label, value):
        self.oled.fill(0)
        self.oled.text(title, 0, 0)
        self.oled.hline(0, 10, 128, 1)
        self.oled.text(label + ":", 0, 25)
        self.oled.text(value, 0, 40)
        self.oled.show()
        
    def update_input_double_label(self,title, label_one, label_two, value):
        self.oled.fill(0)
        self.oled.text(title, 0, 0)
        self.oled.hline(0, 10, 128, 1)
        self.oled.text(label_one, 0, 20)
        self.oled.text(label_two, 0, 40)
        self.oled.text(value, 0, 55)
        self.oled.show()

    def show_ready(self, dots=0):
        self.oled.fill(0)
        self.oled.text("FIELD ENGINE", 0, 0)
        self.oled.hline(0, 10, 128, 1)
        dot_str = "." * dots
        self.oled.text("System Online", 0, 25)
        self.oled.text("Ready" + dot_str, 0, 45)
        self.oled.show()

    def shutdown_sequence(self):
        self.oled.fill(0)
        self.oled.text("EXITING...", 30, 28)
        self.oled.show()
        time.sleep(1.2)

        self.oled.fill(0)
        self.oled.show()
        self.oled.sleep(True)
        print("OLED is now in sleep mode.")