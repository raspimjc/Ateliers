from machine import Pin
import time

#from constantes import *
PIN_BP1 = 16

#Variables globales
date_dernier_appui = time.ticks_ms()
bouton_actif = False

#Handler d'interruption
def bouton_handler(pin):
    global bouton_actif
    global date_dernier_appui
    #anti- rebonds ...
    if time.ticks_diff(time.ticks_ms(), date_dernier_appui) > 500: 
        bouton_actif = True
        #reinitialisation la variable date_dernier_appui
        date_dernier_appui = time.ticks_ms() 

#Test
def test():
    global bouton_actif
    time.sleep(1)
    if bouton_actif:
        print("Bouton actif")
        bouton_actif = False    

#Main    
if __name__ == '__main__':
    #Declaration
    bouton = Pin(PIN_BP1, Pin.IN, Pin.PULL_UP)
    bouton.irq(trigger = machine.Pin.IRQ_RISING, handler = bouton_handler)
    #Test
    print("Consigne: En attente d'un appui sur le BP")
    while True:
        test()

