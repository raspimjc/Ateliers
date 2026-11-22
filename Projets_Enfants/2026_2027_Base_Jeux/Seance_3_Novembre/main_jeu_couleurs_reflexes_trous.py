# COULEURS REFLEXES - Code a trous
#
# Deux joueurs s'affrontent. Chaque joueur surveille sa couleur.
# - Joueur 1 : bleu
# - Joueur 2 : vert
#
# Les couleurs defilent sur les deux NeoPixels.
# Bonne couleur : +1 point
# Mauvaise couleur : -1 point
# Personne n'appuie : 0 point

# Complete les blancs en t'aidant des codes de test
# - test_bouton
# - test_neopixel

from machine import Pin
from neopixel import Neopixel
import time
import random

# Les boutons sont branches entre la broche et GND.
# Trou 1 : entre 16 et 17, indique la broche du bouton du joueur 1.
# Trou 2 : indique la broche du bouton du joueur 2.
bouton1 = Pin(_____, Pin.IN, Pin.PULL_UP)
bouton2 = Pin(_____, Pin.IN, Pin.PULL_UP)

# Deux NeoPixels sont branches sur GPIO 13.
# Trou 3 : nombre de LEDs visibles, ici 2.
# Trou 4 : numero de la broche GPIO du ruban, ici 13.
NOMBRE_LEDS = _____
NUMERO_GPIO = _____
leds = Neopixel(NOMBRE_LEDS, 0, NUMERO_GPIO, "GRB")

# Trou 5 : rouge = (255, 0, 0), test_neopixel donne les autres couleurs.
rouge = _____
vert = _____
bleu = _____
jaune = (255, 255, 0)

# Cette liste contient toutes les couleurs qui defilent.
couleurs = [rouge, vert, bleu, jaune]

# Trou 6 : luminoisite du test_neopixel, utilisee avec brightness(...).
leds.brightness(_____)
leds.clear()
leds.show()

score1 = 0
score2 = 0

# Trou 7 : nombre de manches a jouer, par exemple 10.
nombre_manches = _____

# Trou 8 : duree en millisecondes pour chaque couleur.
# 1000 ms = 1 seconde ; 500 ms = 1/2 seconde ; 700 ms = 0,7 seconde.
# Plus le nombre est petit, plus le jeu est rapide.
vitesse_jeu = _____

# Attendre que les deux boutons soient relaches.
def attendre_relachement():
    while bouton1.value() == 0 or bouton2.value() == 0:
        time.sleep_ms(10)

for manche in range(nombre_manches):
    print("Manche", manche + 1)
    attendre_relachement()

    debut = random.randint(0, len(couleurs) - 1)
    resultat = 0

    for indice in range(len(couleurs)):
        couleur = couleurs[(debut + indice) % len(couleurs)]
        leds.fill(couleur)
        leds.show()

        fin = time.ticks_add(time.ticks_ms(), vitesse_jeu)
        while time.ticks_diff(fin, time.ticks_ms()) > 0:
            # Trou 9 : avec PULL_UP, un bouton appuye vaut 0.
            if bouton1.value() == _____:
                if couleur == bleu:
                    # Trou 10 : ajoute un point avec +1.
                    score1 = score1 + _____
                    resultat = 1
                else:
                    # Trou 11 : retire un point avec -1.
                    score1 = score1 - _____
                    resultat = -1
                break

            # Trou 12 : avec PULL_UP, un bouton appuye vaut 0.
            if bouton2.value() == _____:
                if couleur == vert:
                    # Trou 13 : ajoute un point avec +1.
                    score2 = score2 + _____
                    resultat = 1
                else:
                    # Trou 14 : retire un point avec -1.
                    score2 = score2 - _____
                    resultat = -1
                break

            time.sleep_ms(10)

        if resultat != 0:
            break

    if resultat == 0:
        print("Personne n'a appuye : 0 point")
    elif resultat == -1:
        print("Erreur : -1 point")
    else:
        print("Bonne couleur : +1 point")

    print("Scores - Bleu:", score1, "Vert:", score2)
    leds.clear()
    leds.show()
    attendre_relachement()
    time.sleep(1)

print("Fin du jeu")
print("Score final - Bleu:", score1, "Vert:", score2)
