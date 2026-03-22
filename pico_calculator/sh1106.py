# sh1106.py - Minimal driver for 1.3" OLED
from micropython import const
import framebuf

class SH1106(framebuf.FrameBuffer): 
    def __init__(self, width, height, external_vcc):
        self.width = width
        self.height = height
        self.external_vcc = external_vcc
        self.pages = self.height // 8
        self.buffer = bytearray(self.pages * self.width)
        super().__init__(self.buffer, self.width, self.height, framebuf.MONO_VLSB)
        self.init_display()

    def init_display(self):
        for cmd in (
            0xAE, 0x02, 0x10, 0x40, 0x81, 0xCF, 0xA1, 0xC8, 0xA6, 0xA8, 
            0x3F, 0xD3, 0x00, 0xD5, 0x80, 0xD9, 0xF1, 0xDA, 0x12, 0xDB, 
            0x40, 0xAF, 0x20, 0x02
        ):
            self.write_cmd(cmd)

    def show(self):
        for page in range(self.pages):
            self.write_cmd(0xB0 + page)
            self.write_cmd(0x02)
            self.write_cmd(0x10)
            self.write_data(self.buffer[page * self.width : (page + 1) * self.width])
            
    def poweroff(self):
        self.write_cmd(0xAE)

    def poweron(self):
        self.write_cmd(0xAF)

    def sleep(self, value):
        if value:
            self.write_cmd(0xAE) #Sleep
        else:
            self.write_cmd(0xAF) # Wake

class SH1106_I2C(SH1106):  
    def __init__(self, width, height, i2c, addr=0x3C, external_vcc=False):
        self.i2c = i2c
        self.addr = addr
        super().__init__(width, height, external_vcc)

    def write_cmd(self, cmd):
        self.i2c.writeto(self.addr, bytearray([0x00, cmd]))

    def write_data(self, buf):
        self.i2c.writeto(self.addr, b'\x40' + buf)
        
    def write_list(self, items, x=0, start_y=15, spacing=12, selected_index=0):
        for i, item in enumerate(items):
            y = start_y + (i * spacing)
            prefix = "> " if i == selected_index else "  "
            if y < 64:
                self.text(prefix + str(item), x, y)
        self.show()
