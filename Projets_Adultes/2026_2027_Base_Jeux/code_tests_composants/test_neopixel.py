from neopixel import Neopixel
import time
#from constantes import *

# declaration du ruban de leds 
NUM_LED = 8 #Nbre de leds
neo = Neopixel(NUM_LED, 0, 12, "GRB")

# on definit la luminosite des leds / 255
neo.brightness(15)
# on eteint toute les leds
neo.clear()
# on affiche
neo.show()

def test_neopixel(leds):
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

if __name__ == '__main__':
    while True:
        test_neopixel(neo)

