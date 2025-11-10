from machine import Pin, PWM
from rotary_irq_rp2 import RotaryIRQ
from neopixel import Neopixel
import time

#Declaration de l'encoder
r = RotaryIRQ(pin_num_clk=28,pin_num_dt=27,reverse=False,
              incr=1,range_mode=RotaryIRQ.RANGE_UNBOUNDED,
              pull_up=True,half_step=False)

#Declaration du ruban de leds (Pin 0)
NUM_LED = 30
PIN_NB = 0
leds = Neopixel(NUM_LED, 0, PIN_NB, "GRB")
leds.brightness(15)
leds.clear()
leds.show()

#Declaration de quelques couleurs 
couleur_rouge = (255,0,0)
couleur_vert = (0,255,0)
couleur_bleu = (0,0,255)
couleur_noir = (0,0,0)

#Initialisations diverses
val_old = r.value()
print("valeur depart =", val_old)

leds.set_pixel_line(0,3,couleur_bleu)
leds.show()

#Boucle principale:
#Effectue la rotation d'un bloc de leds selon la valeur de l'encoder
while True:
    val_new = r.value()
    if val_old != val_new:
        print("valeur =", val_new)
        #On change de sens selon la polarité de la valeur: postif/negatif
        #if (val_new >= 0):
        #On change de sens selon la valeur: augmente ou diminue
        if (val_new > val_old):
            leds.rotate_right(1)
            leds.show()
        else:
            leds.rotate_left(1)
            leds.show()
        val_old = val_new     
    time.sleep_ms(50)

  

