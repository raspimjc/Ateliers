from machine import Pin
import time
from neopixel import Neopixel
from lcd1602_i2c import*
from machine import I2C

LedV= Pin(2,Pin.OUT)
LedV.value(0)
LedB= Pin(3,Pin.OUT)
LedB.value()
LedR= Pin(4,Pin.OUT)
LedR.value(0)
LedJ= Pin(5,Pin.OUT)
LedJ.value(0)
time.sleep(2)
LedV.value(1)
LedB.value(1)
LedR.value(1)
LedJ.value(1)
# --- LCD ---
DEFAULT_I2C_ADDR = 0x27 
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
lcd.clear()

leds = Neopixel(8,0,13,"GRB")
leds.brightness(10)
leds.clear()
leds.show()
relais1 = Pin(6, Pin.OUT)
relais2 = Pin(7, Pin.OUT)
relais3 = Pin(8, Pin.OUT)
relais4 = Pin(9, Pin.OUT)
relais1.value(1)
relais2.value(1)
relais3.value(1)
relais4.value(1)