from neopixel import Neopixel
import time

#from constantes import *
PIN_NEOPIXEL = 13

#Test
def test(leds):
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

#Main    
if __name__ == '__main__':
    #Declaration
    neo = Neopixel(8, 0, PIN_NEOPIXEL, "GRB")
    #Init
    neo.brightness(15)
    neo.clear()
    neo.show()
    #Test
    print("Consigne: Le ruban va s'allumer en differentes couleurs")
    while True:
        test(neo)

