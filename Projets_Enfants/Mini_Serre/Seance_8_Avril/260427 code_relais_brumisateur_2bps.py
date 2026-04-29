from machine import Pin
import time
from quant_debounce_bp import Quant_Debounce_Bp

time.sleep(0.1) # Wait for USB to become ready

print("Test Brumisateur !")

# INIT
bp3_allumer = Quant_Debounce_Bp(11, "bp3")
bp4_eteindre = Quant_Debounce_Bp(10, "bp4")
led_etat = Pin(4, Pin.OUT) #LED rouge
relais2_brumisateur = Pin(7, Pin.OUT)


# place les actionneur dans leur etat par defaut
relais2_brumisateur.value(1)  # eteint le brumisateur
led_etat.value(1)       # eteint la led
mon_etat = "eteint"     # variable d'etat du programme

# boucle principale
while True:
    if mon_etat == "eteint":
        if bp3_allumer.get_state() == "appuyer":
            # on allume le brumisateur
            relais2_brumisateur.value(0)
            time.sleep(0.05)
            relais2_brumisateur.value(1)
            led_etat.value(0)
            mon_etat = "allumer"
    else:
        if bp4_eteindre.get_state() == "appuyer":
            # on eteint le brumisateur
            relais2_brumisateur.value(0)
            time.sleep(0.1)
            relais2_brumisateur.value(1)
            time.sleep(0.1)
            relais2_brumisateur.value(0)
            time.sleep(0.1)
            relais2_brumisateur.value(1)
            
            led_etat.value(1)
            mon_etat = "eteint"


