#=====================================================
# Main Exemple Buzzer:
# - On apprend a eteindre le buzzer
#=====================================================
from machine import Pin
from buzzer import Buzzer
import time


# declaration du buzzer (Pin2, alimentation en 3.3V)
buz = Buzzer(2)
#buz.stop()

# fonction qui va arreter le buzzer
def buzzer_stop(pin):
    buz_stop = Pin(pin, Pin.OUT)
    buz_stop.value(1)

time.sleep(1)
buzzer_stop(2)

while True:
    pass
   
    



