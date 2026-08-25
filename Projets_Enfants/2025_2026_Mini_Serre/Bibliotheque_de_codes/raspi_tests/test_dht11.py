from machine import Pin
from time import sleep
import dht


DHT = dht.DHT11(Pin(22)) 
#DHT = dht.DHT22(Pin(22)) 
    
while True:
    DHT.measure()
    print(f"Temperature : {DHT.temperature():.1f}")
    print(f"Humidite    : {DHT.humidity():.1f}")
    sleep(1)


