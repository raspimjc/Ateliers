from machine import Pin
import time

bouton = machine.Pin(1, machine.Pin.IN, Pin.PULL_UP) 

while True:
    if bouton.value() == 0:
        print("Bouton actif")
    else:
        print("Bouton inactif")
    time.sleep_ms(50)
