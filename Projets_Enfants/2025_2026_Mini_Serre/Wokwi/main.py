import time
from machine import Pin

relais_pompe= Pin(6,Pin.OUT)
relais_brumi= Pin(7,Pin.OUT)
relais_ventilo = Pin(9,Pin.OUT)

def test_relais(relais):
    relais.toggle()
    time.sleep(1)
    
if __name__ == '__main__':
    while True:
        test_relais(relais_pompe)
        test_relais(relais_brumi)
        test_relais(relais_ventilo)        
