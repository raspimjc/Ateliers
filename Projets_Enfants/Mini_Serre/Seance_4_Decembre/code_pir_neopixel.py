from machine import Pin
from neopixel import Neopixel
from time import sleep

#declaration du capteur PIR
capteur = Pin(13, Pin.IN)
valeur_detection = 1

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
    valeur_lue = capteur.value()
    
    #si quelquechose a ete detecte
    if valeur_lue == valeur_detection:
        print("Presence detectée")
        # on allume toutes les leds du sapin en rouge
        leds.fill((255,0,0))
        leds.show()
    #sinon
    else:
        print("Rien a signaler")
        # on eteint les leds du sapin
        leds.clear() # equivalent a: leds.fill((0,0,0))
        leds.show()
        
    #on attends 1 seconde avant de relire 
    sleep(1)

    
   
    


