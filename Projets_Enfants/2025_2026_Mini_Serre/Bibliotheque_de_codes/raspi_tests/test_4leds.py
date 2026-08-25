#Import des modules
from machine import Pin
import time

#Initialisation des leds
led_0 = Pin(2, Pin.OUT)
led_1 = Pin(3, Pin.OUT)
led_2 = Pin(4, Pin.OUT)
led_3 = Pin(5, Pin.OUT)

#Eteindre toutes les leds
led_0.value(0)
led_1.value(0)
led_2.value(0)
led_3.value(0)

#Boucle infinie
while True:
    # Pour chaque led, inverser l’état de la led
    # Attendre 500 ms
    led_0.toggle()
    time.sleep(0.5)
    led_1.toggle()
    time.sleep(0.5)
    led_2.toggle()
    time.sleep(0.5)
    led_3.toggle()
    time.sleep(0.5) 