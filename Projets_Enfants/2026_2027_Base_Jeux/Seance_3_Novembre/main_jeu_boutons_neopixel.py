# DUEL DE REFLEXES - Correction
#
# Deux joueurs s'affrontent avec un bouton chacun. Les deux LEDs deviennent
# bleues pendant l'attente, puis vertes au signal. Le premier joueur qui appuie
# gagne : sa LED devient verte et celle de son adversaire devient rouge.

from machine import Pin
from neopixel import Neopixel
import time
import random

# Boutons branchés entre la broche et GND
# Le joueur 1 a le bouton sur GPIO 16, le joueur 2 sur GPIO 17.
bouton1 = Pin(16, Pin.IN, Pin.PULL_UP)
bouton2 = Pin(17, Pin.IN, Pin.PULL_UP)

# Deux NeoPixels sont branches sur GPIO 13.
NOMBRE_LEDS = 2
NUMERO_GPIO = 13
leds = Neopixel(NOMBRE_LEDS, 0, NUMERO_GPIO, "GRB")

# Les couleurs sont donnees dans l'ordre (rouge, vert, bleu).
rouge = (255,0,0)
vert = (0,255,0)
bleu = (0,0,255)

# on definit la luminosite des leds 15 (max 255)
leds.brightness(15)
# on eteint toute les leds
leds.clear()
# on affiche
leds.show()

while True:
    # Attendre que les deux joueurs aient relache leur bouton.
    # Avec PULL_UP, un bouton appuye vaut 0.
    while bouton1.value() == 0 or bouton2.value() == 0:
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
    if bouton1.value() == 0:
        leds.set_pixel(0, vert)
        leds.set_pixel(1, rouge)
    else:
        leds.set_pixel(0, rouge)
        leds.set_pixel(1, vert)
        
    leds.show()
    time.sleep(2)