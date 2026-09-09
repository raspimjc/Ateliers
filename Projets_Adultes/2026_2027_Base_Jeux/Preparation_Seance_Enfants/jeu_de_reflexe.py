# 🎯 DUEL DE RÉFLEXES
## Principe du jeu
## Une LED va s'allumer au hasard :
## 🔴 LED rouge → appuyer sur le bouton rouge
## 🟢 LED verte → appuyer sur le bouton vert
## Le joueur doit être **le plus rapide possible** !
## Le programme mesure son **temps de réaction**.

from machine import Pin
import time
import random

## Declaration des boutons et des leds
leds = [
    Pin(6, Pin.OUT),       # rouge
    Pin(7, Pin.OUT)        # verte
]

boutons = [
    Pin(16, Pin.IN, Pin.PULL_UP),   # bouton rouge
    Pin(17, Pin.IN, Pin.PULL_UP)    # bouton vert
]

## Fonction: Attendre qu'un bouton soit appuyé
def attendre_bouton():
    while True:
        for i, bouton in enumerate(boutons):
            if bouton.value() == 0:
                return i

## Fonction: Éteindre les LEDs
def eteindre_leds():
    for led in leds:
        led.off()

## Programme principal
print("DUEL DE REFLEXES")

# Test des LEDs
for led in leds:
    led.on()
time.sleep(1)
eteindre_leds()
time.sleep(1)

while True:

    print("PREPAREZ-VOUS...")
    # On attend un peu avant de lancer le jeu
    time.sleep(random.uniform(1, 3))
    # Choisir une LED au hasard
    led_choisie = random.randint(0, 1)
    # Allumer la LED
    leds[led_choisie].on()

    # On commence à mesurer le temps
    debut = time.ticks_ms()

    # Attendre le bouton du joueur
    choix_joueur = attendre_bouton()

    # Calculer le temps de réaction
    fin = time.ticks_ms()
    temps_reaction = time.ticks_diff(fin, debut)

    # Éteindre les LEDs
    eteindre_leds()

    # Vérification
    if choix_joueur == led_choisie:
        print("BRAVO !")
        print("Temps de réaction :", temps_reaction, "ms")
    else:
        print("MAUVAIS BOUTON !")
    time.sleep(2)

