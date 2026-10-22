import time
time.sleep(0.1) # Wait for USB to become ready

print("Serre Regul temperature !")

import shared
from ihm_led import IhmLed
from sensor_dht22 import SensorDHT22
from regulation_thermique import RegulationThermique
from ventilateur import Ventilateur
from chauffage import Chauffage
from cli import Cli
from bouton import Bouton

## IHM
# demarre la led de vie sur la bonne broche
ihm_led = IhmLed(2)

## capteurs
# demarre la mesure
temperature_sensor = SensorDHT22(22)

## actionneur
# demarre le ventilateur
act_ventilateur = Ventilateur(7)
# demarre le chauffage
act_chauffage = Chauffage(6)

## regulation
# demarre la régulation thermique
regulation_thermique = RegulationThermique()

## boutons
bp1 = Bouton(4,"bp1")
bp2 = Bouton(5,"bp2")

## debug cli
debug_cli = Cli()

