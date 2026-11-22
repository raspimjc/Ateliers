# COULEURS REFLEXES
#
# Deux joueurs s'affrontent. Chaque joueur doit surveiller sa couleur.
# - Joueur 1 : bleu
# - Joueur 2 : vert
#
# Les couleurs defilent sur les deux NeoPixels.
# Si un joueur appuie pendant sa couleur : +1 point.
# Si un joueur appuie pendant une autre couleur : -1 point.
# Si personne n'appuie : 0 point.

from machine import Pin
from neopixel import Neopixel
import time
import random

# Boutons branches entre la broche et GND.
# Chaque bouton utilise son propre numero de broche GPIO.
bouton1 = Pin(16, Pin.IN, Pin.PULL_UP)
bouton2 = Pin(17, Pin.IN, Pin.PULL_UP)

# Deux NeoPixels branches sur GPIO 13.
# 2 = nombre de LEDs, 13 = broche GPIO utilisee par les LEDs.
leds = Neopixel(2, 0, 13, "GRB")

# Les couleurs sont donnees dans l'ordre Rouge, Vert, Bleu.
# Chaque nombre varie de 0 (eteint) a 255 (maximum).
rouge = (255, 0, 0)
vert = (0, 255, 0)
bleu = (0, 0, 255)
jaune = (255, 255, 0)

# Cette liste contient toutes les couleurs qui peuvent defiler.
couleurs = [rouge, vert, bleu, jaune]

leds.brightness(15)
leds.clear()
leds.show()

score1 = 0
score2 = 0
nombre_manches = 10

# Durée d'affichage de chaque couleur en millisecondes : 1000 ms = 1 seconde.
# Exemple : vitesse_jeu = 500 affiche une couleur pendant 1/2 seconde.
# Exemple : vitesse_jeu = 700 affiche une couleur pendant 0,7 seconde.
# Plus le nombre est petit, plus le jeu est rapide.
vitesse_jeu = 700

# Attendre que les deux boutons soient relaches.
def attendre_relachement():
    while bouton1.value() == 0 or bouton2.value() == 0:
        time.sleep_ms(10)

for manche in range(nombre_manches):
    print("Manche", manche + 1)
    attendre_relachement()

    # Commencer a une couleur aleatoire, puis faire defiler toutes les couleurs.
    debut = random.randint(0, len(couleurs) - 1)
    resultat = 0

    for indice in range(len(couleurs)):
        couleur = couleurs[(debut + indice) % len(couleurs)]
        leds.fill(couleur)
        leds.show()

        # Laisser le temps defini par la variable vitesse_jeu pour appuyer.
        fin = time.ticks_add(time.ticks_ms(), vitesse_jeu)
        while time.ticks_diff(fin, time.ticks_ms()) > 0:
            # Avec PULL_UP, la valeur vaut 0 quand un bouton est appuye.
            if bouton1.value() == 0:
                # Le joueur 1 gagne un point avec le bleu.
                if couleur == bleu:
                    score1 = score1 + 1
                    resultat = 1
                else:
                    score1 = score1 - 1
                    resultat = -1
                break

            if bouton2.value() == 0:
                # Le joueur 2 gagne un point avec le vert.
                if couleur == vert:
                    score2 = score2 + 1
                    resultat = 1
                else:
                    score2 = score2 - 1
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
