#Chenillard 4 leds simple

#Import des modules
from machine import Pin
import time

#Initialisation des leds
led_0 = Pin(6, Pin.OUT)
led_1 = Pin(7, Pin.OUT)
led_2 = Pin(8, Pin.OUT)
led_3 = Pin(9, Pin.OUT)

#Eteindre toutes les leds
led_0.value(0)
led_1.value(0)
led_2.value(0)
led_3.value(0)

#Boucle infinie
while True:
    # Pour chaque led, inverser l’état de la led
    # Attendre une seconde
    led_0.toggle()
    time.sleep(1)
    led_1.toggle()
    time.sleep(1)
    led_2.toggle()
    time.sleep(1)
    led_3.toggle()
    time.sleep(1) 