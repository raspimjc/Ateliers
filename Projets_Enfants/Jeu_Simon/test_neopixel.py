from neopixel import Neopixel
import time

# Declaration du ruban de leds
NUM_LED = 8
PIN_NB = 13
ruban = Neopixel(NUM_LED, 0, PIN_NB, "GRB")

# on definit la luminosite des leds / 255
ruban.brightness(15)
# on eteint toute les leds
ruban.clear()
# on affiche
ruban.show()


while True:
    # on allume toutes les leds du sapin en rouge pendant 1 sec
    ruban.fill((255,0,0))
    ruban.show()
    time.sleep(1)
    # on allume toutes les leds du sapin en vert pendant 1 sec
    ruban.fill((0,255,0))
    ruban.show()
    time.sleep(1)
    # on allume toutes les leds du sapin en jaune pendant 1 sec
    ruban.fill((255,255,0))
    ruban.show()
    time.sleep(1)    
