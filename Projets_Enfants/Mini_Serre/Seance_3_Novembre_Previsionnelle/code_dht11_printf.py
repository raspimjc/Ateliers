from machine import Pin
from time import sleep
import dht


DHT11 = dht.DHT11(Pin(22)) 
    
while True:
    DHT11.measure()
    print(f"Temperature : {DHT11.temperature():.1f}")
    print(f"Humidite    : {DHT11.humidity():.1f}")
    sleep(1)


