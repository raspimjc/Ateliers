#=====================================================
# Main Exemple Ruban LEDs Neopixel:
# - On allume et eteint toutes les leds en meme temps
#=====================================================
from neopixel import Neopixel
import time

# DECLARATIONS:
# -------------

# declaration du ruban de leds (Pin 0)
NUM_LED = 30
PIN_NB = 18 #0
leds = Neopixel(NUM_LED, 0, PIN_NB, "GRB")

# INITIALISATIONS:
# ----------------

# on definit la luminosite des leds / 255
leds.brightness(15)
# on eteint toute les leds
leds.clear()
# on affiche
leds.show()

# BOUCLE PRINCIPALE:
# ------------------
while True:
    # on allume toutes les leds du sapin en rouge
    leds.fill((255,0,0))
    leds.show()
    time.sleep(1)
    # on allume toutes les leds du sapin en vert
    leds.fill((0,255,0))
    leds.show()
    time.sleep(1)
    # on allume toutes les leds du sapin en bleu
    leds.fill((0,0,255))
    leds.show()
    time.sleep(1)    
