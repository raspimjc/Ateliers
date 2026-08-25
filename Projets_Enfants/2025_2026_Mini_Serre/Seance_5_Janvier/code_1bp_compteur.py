from machine import Pin
import time

#Declaration du bouton
bouton = Pin(0, machine.Pin.IN, Pin.PULL_UP) 

#Declaration d'une variable compteur
compteur = 0

while True:
    if bouton.value() == 0:
        compteur = compteur + 1
        print("Compteur = ",compteur)        
    
    time.sleep(0.3)




