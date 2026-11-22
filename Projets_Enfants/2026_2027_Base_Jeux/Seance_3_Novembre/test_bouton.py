from machine import Pin
import time

# Boutons branchés entre la broche et GND
bouton = Pin(16, Pin.IN, Pin.PULL_UP)
#PULL UP signifie qu'a l'intérieur du Pico la broche est reliée au VCC (1)
#Si on n'appuie pas sur le bouton, la sortie reste en l'air et donc connectée en interne au VCC
#Si on appuie sur le bouton, on force la connection à la masse (0)

while True:
    if bouton.value() == 0:
        print("Bouton Appuyé")
    else:
        print("Bouton Relaché")
    time.sleep_ms(50)
