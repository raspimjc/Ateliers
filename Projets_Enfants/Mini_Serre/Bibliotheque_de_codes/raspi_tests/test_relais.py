import time
from machine import Pin

relais_pompe= Pin(6,Pin.OUT)
relais_brumi= Pin(7,Pin.OUT)

def test_relais(relais):
    relais.toggle()
    time.sleep(1)
    
while True:
    test_relais(relais_pompe)
    test_relais(relais_brumi)
