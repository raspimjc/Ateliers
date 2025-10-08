from machine import Pin
from time import sleep
import dht


DHT11 = dht.DHT11(Pin(22)) 

def test_dht(capteur):
    sleep(1)
    # Le DHT11 renvoie au maximum une mesure toute les 1s
    capteur.measure()
    # Récupère les mesures du capteur
    print(f"Temperature : {capteur.temperature():.1f}")
    print(f"Humidite    : {capteur.humidity():.1f}")
    
    
if __name__ == '__main__':
    while True:
        test_dht(DHT11)



