#=====================================================
# Main Exemple PIR:
# - Detection simple d'une presence
#=====================================================
from machine import Pin
import time


# declaration du detecteur infra rouge
pir_sensor = Pin(16, Pin.IN)

while True:
    time.sleep(1)
    reading = pir_sensor.value()
    print(reading)
    #si quelquechose a ete detecte
    if reading == 1:
        print("Presence detectée")
        time.sleep(1)
    #si rien  n'a ete detecte
    else:
        print("Rien a signaler")
        time.sleep(2)

    
   
    


