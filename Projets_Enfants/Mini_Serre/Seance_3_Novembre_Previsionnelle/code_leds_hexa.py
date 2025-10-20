from machine import Pin
from time import sleep

# Configuration des 4 LED sur les broches GPIO 6 à 9
led_pins = [Pin(i, Pin.OUT) for i in range(6, 10)]

def afficher_valeur(valeur):
    """Affiche une valeur (0–15) en binaire sur les 4 LED"""
    for i in range(4):
        bit = (valeur >> i) & 1
        led_pins[i].value(bit)

while True:
    for n in range(16):  # 0x0 à 0xF
        afficher_valeur(n)
        print("Affichage:", hex(n))
        sleep(0.5)  # délai entre les changements
