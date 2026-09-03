"""ILI9341 demo (bouncing boxes)."""
from machine import Pin, SPI  
from random import random, seed
from ili9341 import Display, color565
from utime import sleep_us, ticks_cpu, ticks_us, ticks_diff 
import time

#from constantes import *
TFT_SPI_ID = 0
PIN_TFT_SCK = 2
PIN_TFT_MOSI = 3
PIN_TFT_DC = 1
PIN_TFT_CS = 5
PIN_TFT_RST = 0

class Box(object):
    """Bouncing box."""

    def __init__(self, screen_width, screen_height, size, display, color):
        """Initialize box.

        Args:
            screen_width (int): Width of screen.
            screen_height (int): Width of height.
            size (int): Square side length.
            display (ILI9341): display object.
            color (int): RGB565 color value.
        """
        self.size = size
        self.w = screen_width
        self.h = screen_height
        self.display = display
        self.color = color
        # Generate non-zero random speeds between -5.0 and 5.0
        seed(ticks_cpu())
        r = random() * 10.0
        self.x_speed = 5.0 - r if r < 5.0 else r - 10.0
        r = random() * 10.0
        self.y_speed = 5.0 - r if r < 5.0 else r - 10.0

        self.x = self.w / 2.0
        self.y = self.h / 2.0
        self.prev_x = self.x
        self.prev_y = self.y

    def update_pos(self):
        """Update box position and speed."""
        x = self.x
        y = self.y
        size = self.size
        w = self.w
        h = self.h
        x_speed = abs(self.x_speed)
        y_speed = abs(self.y_speed)
        self.prev_x = x
        self.prev_y = y

        if x + size >= w - x_speed:
            self.x_speed = -x_speed
        elif x - size <= x_speed + 1:
            self.x_speed = x_speed

        if y + size >= h - y_speed:
            self.y_speed = -y_speed
        elif y - size <= y_speed + 1:
            self.y_speed = y_speed

        self.x = x + self.x_speed
        self.y = y + self.y_speed

    def draw(self):
        """Draw box."""
        x = int(self.x)
        y = int(self.y)
        size = self.size
        prev_x = int(self.prev_x)
        prev_y = int(self.prev_y)
        self.display.fill_hrect(prev_x - size,
                                prev_y - size,
                                size, size, 0)
        self.display.fill_hrect(x - size,
                                y - size,
                                size, size, self.color)


def test(display, time_debut, timeout):
    """Bouncing box."""
    try:
        display.clear()
        colors = [color565(255, 0, 0),
                  color565(0, 255, 0),
                  color565(0, 0, 255),
                  color565(255, 255, 0),
                  color565(0, 255, 255),
                  color565(255, 0, 255)]
        sizes = [12, 11, 10, 9, 8, 7]
        boxes = [Box(display.width, display.height, sizes[i], display,
                 colors[i]) for i in range(6)]

        while time.ticks_diff(time.ticks_ms(), time_debut) < timeout * 1000:
            timer = ticks_us()
            for b in boxes:
                b.update_pos()
                b.draw()
            # Attempt to set framerate to 30 FPS
            timer_dif = 33333 - ticks_diff(ticks_us(), timer)
            if timer_dif > 0:
                sleep_us(timer_dif)

    except KeyboardInterrupt:
        display.cleanup()

if __name__ == '__main__':
    spi = SPI(TFT_SPI_ID, baudrate=10000000, sck=Pin(PIN_TFT_SCK), mosi=Pin(PIN_TFT_MOSI))
    display = Display(spi, dc=Pin(PIN_TFT_DC), cs=Pin(PIN_TFT_CS), rst=Pin(PIN_TFT_RST), width=320, height=240, rotation=0)
    debut = time.ticks_ms()
    test(display,debut,5)
