from machine import Pin
import time
from quant_debounce_bp import Quant_Debounce_Bp

time.sleep(0.1) # Wait for USB to become ready

print("Test Pompe !")

# INIT
bp1_allumer = Quant_Debounce_Bp(0, "bp1")
bp2_eteindre = Quant_Debounce_Bp(1, "bp2")
led_etat = Pin(2, Pin.OUT) #Led verte
relais1_pompe = Pin(6, Pin.OUT)


# place les actionneur dans leur etat par defaut
relais1_pompe.value(1)  # eteint la pompe
led_etat.value(0)       # eteint la led
mon_etat = "eteint"     # variable d'etat du programme

# boucle principale
while True:
    if mon_etat == "eteint":
        if bp1_allumer.get_state() == "appuyer":
            # on allume la pompe
            relais1_pompe.value(0)
            led_etat.value(1)
            mon_etat = "allumer"
    else:
        if bp2_eteindre.get_state() == "appuyer":
            # on eteint la pompe
            relais1_pompe.value(1)
            led_etat.value(0)
            mon_etat = "eteint"

