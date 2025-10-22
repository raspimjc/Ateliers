from machine import Pin
import time
from constantes_laurence import *

# declaration du detecteur infra rouge
pir_sensor = Pin(PIN_PIR, Pin.IN)

def test_pir(pir):
    time.sleep(1)
    reading = pir_sensor.value()
    #print(reading)
    if reading == 1:
        print("Presence detectée")
        time.sleep(1)
    else:
        print("Rien a signaler")
        time.sleep(2)
    
if __name__ == '__main__':
    while True:
        test_pir(pir_sensor)


    
   
    


