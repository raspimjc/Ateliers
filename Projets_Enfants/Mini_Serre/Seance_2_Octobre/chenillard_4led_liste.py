#Chenillard 4 leds liste

#Import des modules
from machine import Pin
import time

#Initialisation des leds
led_0 = Pin(0, Pin.OUT)
led_1 = Pin(1, Pin.OUT)
led_2 = Pin(2, Pin.OUT)
led_3 = Pin(3, Pin.OUT)

#Déclarer une liste de leds
LEDS = [led_0,led_1,led_2,led_3]

#Eteindre toutes les leds
for item in LEDS:
    item.value(0)

#Boucle infinie
while True:
    # Pour chaque led de la liste, inverser l’état de la led
    # Attendre une seconde
    for item in LEDS:
        item.toggle()
        time.sleep(1)
    