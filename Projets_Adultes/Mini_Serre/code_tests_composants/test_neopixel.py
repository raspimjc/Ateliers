from neopixel import Neopixel
import time

# declaration du ruban de leds 
NUM_LED = 30 #Nbre de leds
PIN_NB  = 13 #Pin
leds = Neopixel(NUM_LED, 0, PIN_NB, "GRB")

# on definit la luminosite des leds / 255
leds.brightness(15)
# on eteint toute les leds
leds.clear()
# on affiche
leds.show()

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
