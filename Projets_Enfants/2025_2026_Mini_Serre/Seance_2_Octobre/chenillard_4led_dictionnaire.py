#Chenillard 4 leds dictionnaire

#Import des modules
from machine import Pin
import time

#Initialisation des leds
led_0 = Pin(0, Pin.OUT)
led_1 = Pin(1, Pin.OUT)
led_2 = Pin(2, Pin.OUT)
led_3 = Pin(3, Pin.OUT)

#Déclarer une liste de leds
LEDS = [
    {'led': led_0, 'value': 1},
    {'led': led_1, 'value': 1},
    {'led': led_2, 'value': 1},
    {'led': led_3, 'value': 1},
    {'led': led_0, 'value': 0},
    {'led': led_1, 'value': 0},
    {'led': led_2, 'value': 0},
    {'led': led_3, 'value': 0}
]


#Boucle infinie
while True:
    # Pour chaque élément de la liste, on affecte la valeur sur la led selectionnée
    # Attendre une seconde
    for item in LEDS:
        item['led'].value(item['value'])
        time.sleep(1)
    