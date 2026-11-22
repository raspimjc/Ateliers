# DUEL DE REFLEXES - Code a trous
#
# Deux joueurs s'affrontent avec un bouton chacun. Les deux LEDs deviennent
# bleues pendant l'attente, puis vertes au signal. Le premier joueur qui appuie
# gagne : sa LED devient verte et celle de son adversaire devient rouge.

# Complete les blancs en t'aidant des codes de test
# - test_bouton
# - test_neopixel
# Ne lance le programme qu'une fois tous les blancs remplis.

from machine import Pin
from neopixel import Neopixel
import time
import random

# Les boutons sont branches entre la broche et GND.
# Le joueur 1 a le bouton sur GPIO 16, le joueur 2 sur GPIO 17.
bouton1 = Pin(_____, Pin.IN, Pin.PULL_UP)
bouton2 = Pin(_____, Pin.IN, Pin.PULL_UP)

# Deux NeoPixels sont branches sur GPIO 13.
NOMBRE_LEDS = _____
NUMERO_GPIO = _____
leds = Neopixel(NOMBRE_LEDS, 0, NUMERO_GPIO, "GRB")

# Les couleurs sont donnees dans l'ordre (rouge, vert, bleu).
rouge = _____
vert = _____
bleu = _____

# on definit la luminosite des leds 15 (max 255)
leds.brightness(_____)
# on eteint toute les leds
leds.clear()
# on affiche
leds.show()

while True:
    # Attendre que les deux joueurs aient relache leur bouton.
    # Avec PULL_UP, un bouton appuye vaut 0.
    while bouton1.value() == _____ or bouton2.value() == _____:
        time.sleep_ms(10)

    # LEDs bleues
    leds.fill(bleu)
    leds.show()
    
    # on attend le signal pendant un temps aléatoire entre 2 et 5 secondes
    time.sleep(random.randint(2, 5))

    # LEDs vertes : appuyez !
    leds.fill(vert)
    leds.show()

    # Attendre qu'un joueur appuie.
    # Avec PULL_UP, un bouton appuye vaut 0.
    while bouton1.value() == 1 and bouton2.value() == 1:
        time.sleep_ms(10)

    # La LED verte indique le gagnant.
    if bouton1.value() == _____:
        leds.set_pixel(0, vert)
        leds.set_pixel(1, rouge)
    else:
        leds.set_pixel(0, rouge)
        leds.set_pixel(1, vert)

    leds.show()
    time.sleep(2)


