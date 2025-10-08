#Chenillard 4 leds liste

#Import des modules
from machine import Pin
import time

#Initialisation des leds
led_0 = Pin(6, Pin.OUT)
led_1 = Pin(7, Pin.OUT)
led_2 = Pin(8, Pin.OUT)
led_3 = Pin(9, Pin.OUT)

#Déclarer une liste de leds
LED = [led_0,led_1,led_2,led_3]

#Eteindre toutes les leds
for led in LED:
    led.value(0)

#Boucle infinie
while True:
    # Pour chaque led de la liste, inverser l’état de la led
    # Attendre une seconde
    for led in LED:
        led.toggle()
        time.sleep(1)
    