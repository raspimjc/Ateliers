from machine import Pin
import time

bouton = Pin(0, machine.Pin.IN, Pin.PULL_UP) 

while True:
    if bouton.value() == 0:
        print("Bouton Appuyé")
    else:
        print("Bouton Relaché")
    time.sleep_ms(50)
