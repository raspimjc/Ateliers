
"""Teste les boutons et le ruban NeoPixel en affichant les appuis detectes."""

from classe_Bouton import classe_Bouton
from classe_Neopixel import classe_Neopixel
import time

# ==============================
# INITIALISATION
# ==============================
print("Initialisation...")
BPs = classe_Bouton()
lum = classe_Neopixel()

lum.off()

# ==============================
# BOUCLE PRINCIPALE
# ==============================
liste_boutons = [1, 2, 3, 4, 5, 6, 7, 8]
leds_allumees = [False] * len(liste_boutons)
while True:
    for numero in liste_boutons:
        if BPs.get_status(numero):
            index_led = numero - 1
            leds_allumees[index_led] = not leds_allumees[index_led]
            couleur = lum.YELLOW if leds_allumees[index_led] else lum.BLACK
            etat = "allumee" if leds_allumees[index_led] else "eteinte"
            print("Bouton", numero, "appuye, LED", etat)
            lum.set_pixel(index_led, couleur)

    time.sleep_ms(20)
