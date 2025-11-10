#=====================================================
# Main Exemple LCD I2C:
# - Affiche un message simple sur l'ecran LCD
#=====================================================
from machine import Pin, I2C
from time import sleep
from machine_i2c_lcd import I2cLcd

#Board Setting
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)
#Philippe
#i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)

addr = i2c.scan()[0]
print(hex(addr))

lcd = I2cLcd(i2c, addr, 2, 16)


while True:
    lcd.putstr("  Joyeux Noel!  \n")
    lcd.putstr(" MJC Raspi 2024")
    sleep(1)
    lcd.clear()

