import time
from machine import Pin
from constantes_laurence import *

RELAIS = Pin(PIN_RELAIS, Pin.OUT) 

def test_relais(relais):
    relais.toggle()
    time.sleep(1)
    
if __name__ == '__main__':
    while True:
        test_relais(RELAIS)

