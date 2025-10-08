from machine import Pin, I2C
from time import sleep
from machine_i2c_lcd import I2cLcd

i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)

addr = i2c.scan()[0]
#print(hex(addr))
LCD = I2cLcd(i2c, addr, 2, 16)

def test_lcd(lcd):
    lcd.putstr(" MJC Raspi 2025 \n")
    lcd.putstr("  Hello World ")
    sleep(1)
    lcd.clear()
    

if __name__ == '__main__':
    while True:
        test_lcd(LCD)
