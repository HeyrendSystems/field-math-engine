from machine import Pin, I2C
import time

class KeypadInput:
    def __init__(self):
        self.buffer = ""
        self.confirmed = False
        self.last_key = None
        self.exit = False
        
        self.keymap = [
            ["1", "2", "3", "A"],
            ["4", "5", "6", "B"],
            ["7", "8", "9", "C"],
            ["*", "0", "#", "D"]
        ]

        self.rows = [
            Pin(6, Pin.OUT),
            Pin(7, Pin.OUT),
            Pin(8, Pin.OUT),
            Pin(9, Pin.OUT)
        ]

        self.cols = [
            Pin(10, Pin.IN, Pin.PULL_DOWN),
            Pin(11, Pin.IN, Pin.PULL_DOWN),
            Pin(12, Pin.IN, Pin.PULL_DOWN),
            Pin(13, Pin.IN, Pin.PULL_DOWN)
        ]
        
        for row in self.rows:
            row.value(0)

    def update_screen(self, key):
        
        if key == "A":
            self.exit = True
            return

        if key is None:
            return

        if key.isdigit():
            self.buffer += key
            return

        if key == "*":
            self.buffer = self.buffer[:-1]
            return

        if key == "#":
            self.confirmed = True
            return
        
    def key_pad_scan(self):
        for row_idx, row in enumerate(self.rows):
            for r in self.rows:
                r.value(0)

            row.value(1)
            time.sleep_ms(1)

            for col_idx, col in enumerate(self.cols):
                if col.value():
                    key = self.keymap[row_idx][col_idx]

                    while col.value():
                        time.sleep_ms(10)
                
                    return key
