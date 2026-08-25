from machine import Pin
from time import sleep
from constantes import *


LDR = Pin(PIN_LDR, Pin.IN,Pin.PULL_DOWN)

def test_ldr(ldr):
    sleep(0.1)
    # Lecture du capteur
    value = ldr.value()
    # Récupère les mesures du capteur
    print(f"Lum : {value:.1f}")
    
    
if __name__ == '__main__':
    while True:
        test_ldr(LDR)



