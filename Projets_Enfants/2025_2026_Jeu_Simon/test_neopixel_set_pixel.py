from neopixel import Neopixel
import time

# Declaration du ruban de leds
NUM_LED = 8
PIN_NB = 13
ruban = Neopixel(NUM_LED, 0, PIN_NB, "GRB")

# Declaration de quelques couleurs 
couleur_rouge = (255,0,0)
couleur_vert = (0,255,0)
couleur_bleu = (0,0,255)
couleur_noir = (0,0,0)
couleur_jaune = (255,255,0)

# on definit la luminosite des leds
ruban.brightness(15)
# on eteint toute les leds
ruban.clear()
# on affiche
ruban.show()

while True:
    # on allume tour a tour  les leds du sapin en bleu
    for i in range (0,NUM_LED):
        ruban.set_pixel(i,couleur_bleu)
        ruban.show()
        time.sleep(0.1)
    ruban.clear()
    ruban.show()

    # on allume un bloc de leds
    ruban.set_pixel_line(5,7,couleur_rouge)
    ruban.show()
    time.sleep(2)
    ruban.clear()
    ruban.show()
    
    # on fait un gradient de couleur
    ruban.set_pixel_line_gradient(1,7,couleur_vert,couleur_bleu)
    ruban.show()
    time.sleep(2)
    ruban.clear()
    ruban.show()
