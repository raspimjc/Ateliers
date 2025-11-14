from machine import Pin
from time import sleep
import dht


DHT = dht.DHT11(Pin(xxxxxx)) 
#DHT = dht.DHT22(Pin(xxxxxx)) 
    
while True:
    DHT.measure()
    print(f"Temperature : {DHT.temperature():.1f}")
    print(f"Humidite    : {DHT.humidity():.1f}")
    sleep(1)


