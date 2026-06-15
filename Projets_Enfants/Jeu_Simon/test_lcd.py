from machine import Pin, I2C
from machine_i2c_lcd import I2cLcd
import time

# Declaration de l'ecran LCD
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
addr = i2c.scan()[0]
#print(hex(addr))
lcd = I2cLcd(i2c, addr, 2, 16)


while True:
    lcd.clear()
    lcd.putstr(" Hello Raspi ! \n")
    lcd.putstr(" MJC 2025-2026 \n")
    time.sleep(1)

