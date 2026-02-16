from machine import Pin, I2C, ADC
from machine_i2c_lcd import I2cLcd
import dht
from time import sleep

#Declaration de l'ecran LCD
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
addr = i2c.scan()[0]
print(hex(addr))
lcd = I2cLcd(i2c, addr, 2, 16)

#Declaration du capteur
#DHT = dht.DHT11(Pin(22))  
DHT = dht.DHT22(Pin(22))        

while True:
    
    #On lit le capteur
    DHT.measure()
    temp = DHT.temperature()
    hum = DHT.humidity()

    #On affiche sur l'ecran LCD
    lcd.putstr(f"Temp: {temp} C\n")
    lcd.putstr(f"Hum: {hum} %\n")

    sleep(1)
    #lcd.clear()
