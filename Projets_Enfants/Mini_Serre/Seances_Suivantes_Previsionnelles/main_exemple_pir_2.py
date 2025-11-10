#=====================================================
# Main Exemple PIR:
# - Detection d'une presence et allumage du sapin en rouge
#=====================================================
from machine import Pin
from neopixel import Neopixel
import time

# declaration du detecteur infra rouge
pir_sensor = Pin(16, Pin.IN)
# declaration du ruban de leds (Pin 0)
NUMLED = 30
leds = Neopixel(NUMLED, 0, 0, "GRB")

# on definit la luminosite des leds
leds.brightness(15)
# on eteint toute les leds
leds.clear()
# on affiche
leds.show()

while True:
    time.sleep(1)
    reading = pir_sensor.value()
    print(reading)
    #si quelquechose a ete detecte
    if reading == 1:
        # on allume toutes les leds du sapin en rouge
        leds.fill((255,0,0))
        leds.show()
        time.sleep(1)
    #si rien  n'a ete detecte
    else:
        # on eteint les leds du sapin
        leds.clear() # equivalent a: leds.fill((0,0,0))
        leds.show()
        time.sleep(2)

    
   
    


