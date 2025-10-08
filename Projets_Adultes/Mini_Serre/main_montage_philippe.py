from machine import Pin, I2C
from time import sleep
from machine_i2c_lcd import I2cLcd
from neopixel import Neopixel
from buzzer import Buzzer
from classe_music_P import Music_P

i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)
addr = i2c.scan()[0]
lcd = I2cLcd(i2c, addr, 2, 16)
leds = Neopixel(30, 0, 18, "GRB")
buz = Buzzer(14)
buz.stop()
music = Music_P(buz)


leds.brightness(15)
leds.clear()
leds.show()

leds.fill((0,0,255))
leds.show()


while True:
    lcd.putstr("Hello Philippe  \n")
    lcd.putstr("MJC Raspi 2025")
    music.joue_melodie_timed(music.We_Wish_You_a_Merry_Christmas,15)
    sleep(1)
    lcd.clear()
