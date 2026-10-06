#https://wokwi.com/projects/475883471827510273

from machine import Pin
import time
time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico!")

led_lettre = Pin(25, Pin.OUT)
led_morse = Pin(9, Pin.OUT)

TIRET_TIME = 1
POINT_TIME = TIRET_TIME/2

S = (".",".",".")
O = ("-","-","-")

message = (S,O,S)


led_lettre.value(0)
led_morse.value(0)

print ("debut du message")

for lettre in message:
    
    for symbole in lettre:
      led_morse.value(1)
      if symbole == "-":
        time.sleep(TIRET_TIME)
      else:
        time.sleep(POINT_TIME)
      led_morse.value(0)
      time.sleep(POINT_TIME)
    
    led_lettre.toggle()

print("fin du message")