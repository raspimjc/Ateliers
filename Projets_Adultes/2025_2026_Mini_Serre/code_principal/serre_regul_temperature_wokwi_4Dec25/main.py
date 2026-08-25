import time
time.sleep(0.1) # Wait for USB to become ready

print("Serre Regul temperature !")

import shared
from ihm_led import IhmLed
from sensor_dht22 import SensorDHT22
from regulation_thermique import RegulationThermique

# demarre la led de vie sur la bonne broche
ihm_led = IhmLed(2)
# demarre la mesure
temperature_sensor = SensorDHT22(22)
# demarre la régulation thermique
regulation_thermique = RegulationThermique()
