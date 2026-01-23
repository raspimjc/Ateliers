from machine import Pin
import time

#Declaration du bouton
bouton = Pin(0, machine.Pin.IN, Pin.PULL_UP) 

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

#Declaration d'une variable compteur
compteur = 0

while True:
    if bouton.value() == 0:
        compteur = compteur + 1
        print("Compteur = ",compteur)
    
    if compteur == 1:
        led_0.value(1)
        led_1.value(0)
        led_2.value(0)
        led_3.value(0)
    elif compteur == 2:
        led_0.value(1)
        led_1.value(1)
        led_2.value(0)
        led_3.value(0)
    elif compteur == 3:
        led_0.value(1)
        led_1.value(1)
        led_2.value(1)
        led_3.value(0)
    elif compteur == 4:
        led_0.value(1)
        led_1.value(1)
        led_2.value(1)
        led_3.value(1)
    else:
        led_0.value(0)
        led_1.value(0)
        led_2.value(0)
        led_3.value(0)
    
    time.sleep(0.3)





