from machine import Pin, ADC
from neopixel import Neopixel
import time

# configuration
NUMLED = 24#30

# declaration du potentiometre (ADC 0)
potar = ADC(0)
# declaration du ruban de leds (Pin 0)
leds = Neopixel(NUMLED,0,0,"GRB")

# fonction qui va lire la valeur du potentiometre
def lit_potar():
    global potar
    return potar.read_u16()

# fonction qui va definir la led a allumer en fonction de la valeur du potentiometre
def get_led_for( potar_value ):
    return (((NUMLED-1)*potar_value)/65535)


# definit la luminosite des leds
leds.brightness(15)
# on eteint toute les leds
leds.clear()
# on affiche
leds.show()

# initialisation des variables
old_val_potar = lit_potar()

# boucle principale
while True:
    # lit la valeur du potentiometre
    valeur_potar  = lit_potar()
    # test si la valeur lue est différente de la précédente
    if valeur_potar != old_val_potar:
        # affiche la valeur du potentiometre
        print(valeur_potar)
        # sauvegarde la nouvelle valeur du potentiometre
        old_val_potar = valeur_potar
        # converti la valeur du potentiometre en numero de led
        numero_led = int(get_led_for( valeur_potar ))
        # affiche toute les leds jusqu'au numero de led
        print(f"led a allumer : {numero_led}")
        leds.clear()
        for i in range (0,numero_led):
            leds.set_pixel(i,(128,0,120))
        leds.show()
        
    time.sleep(0.3)
    
