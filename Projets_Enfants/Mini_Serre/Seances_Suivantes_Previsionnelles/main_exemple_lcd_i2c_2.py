#=====================================================
# Main Exemple LCD I2C:
# - Affiche la temperature du CPU sur l'ecran LCD
#=====================================================
from machine import Pin, I2C, ADC
from time import sleep
from machine_i2c_lcd import I2cLcd

#Declaration ports I2C
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)

addr = i2c.scan()[0]
# print(hex(addr[0]))

lcd = I2cLcd(i2c, addr, 2, 16)

#Sensor inclus dans le pico (ADC caché #4)
sensor_temp = ADC(4)
conversion_factor = 3.3 / (65535)

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    lcd.putstr(" MJC Raspi 2024")
    lcd.putstr(" CPU Temp:%.2f" % temperature)
    sleep(1)
    lcd.clear()