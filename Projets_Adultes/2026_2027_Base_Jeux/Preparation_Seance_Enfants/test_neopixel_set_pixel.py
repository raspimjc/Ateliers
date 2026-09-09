from neopixel import Neopixel
import time

# declaration du ruban de leds
NUM_LED = 2
leds = Neopixel(NUM_LED, 0, 13, "GRB")

# declaration de quelques couleurs 
couleur_rouge = (255,0,0)
couleur_vert = (0,255,0)
couleur_bleu = (0,0,255)
couleur_noir = (0,0,0)

# on definit la luminosite des leds
leds.brightness(15)
# on eteint toute les leds
leds.clear()
# on affiche
leds.show()

while True:
    # on allume tour a tour  les leds en bleu
    for i in range (0,NUM_LED):
        leds.set_pixel(i,couleur_bleu)
        leds.show()
    time.sleep(1)
    # on allume tour a tour  les leds en vert
    for i in range (0,NUM_LED):
        leds.set_pixel(i,couleur_vert)
        leds.show()
    time.sleep(1)
    #leds.clear()
