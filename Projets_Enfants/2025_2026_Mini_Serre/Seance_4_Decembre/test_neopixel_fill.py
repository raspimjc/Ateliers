from neopixel import Neopixel
import time

# declaration du ruban de leds
NUM_LED = 30
PIN_NB = 0
leds = Neopixel(NUM_LED, 0, PIN_NB, "GRB")

# on definit la luminosite des leds / 255
leds.brightness(15)
# on eteint toute les leds
leds.clear()
# on affiche
leds.show()


while True:
    # on allume toutes les leds du sapin en rouge pendant 1 sec
    leds.fill((255,0,0))
    leds.show()
    time.sleep(1)
    # on allume toutes les leds du sapin en vert pendant 1 sec
    leds.fill((0,255,0))
    leds.show()
    time.sleep(1)
    # on allume toutes les leds du sapin en bleu pendant 1 sec
    leds.fill((0,0,255))
    leds.show()
    time.sleep(1)    
