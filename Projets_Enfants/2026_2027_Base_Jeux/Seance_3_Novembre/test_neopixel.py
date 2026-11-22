from neopixel import Neopixel
#    def brightness(valeur_luminosite)
#    def fill(couleur)
#    def set_pixel(numero_pixel, couleur)
#    def show()
#    def clear()
import time

# declaration du ruban de leds
NOMBRE_LEDS = 2
NUMERO_GPIO = 13
leds = Neopixel(NOMBRE_LEDS, 0, NUMERO_GPIO, "GRB")

# declaration de quelques couleurs (R,G,B) min 0 max 255
rouge = (255,0,0)
vert = (0,255,0)
bleu = (0,0,255)

# on definit la luminosite des leds / 255
leds.brightness(15)
# on eteint toute les leds
leds.clear()
# on affiche
leds.show()


while True:
    # on allume toutes les leds en bleu pendant 1 sec
    leds.fill(bleu)
    leds.show()
    time.sleep(1)
    
    # on allume tour a tour  les leds en vert
    for i in range (0,NOMBRE_LEDS):
        leds.set_pixel(i,vert)
        leds.show()
        time.sleep(0.5)
    # on recommence la boucle    
    time.sleep(0.5)