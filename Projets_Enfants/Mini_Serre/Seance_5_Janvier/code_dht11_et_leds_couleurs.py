from machine import Pin
from time import sleep
import dht

#Declaration du capteur
DHT = dht.DHT11(Pin(22))  
#DHT = dht.DHT22(Pin(22))            

#Declaration des leds
led_verte = Pin(2, Pin.OUT)
led_bleue = Pin(3, Pin.OUT)
led_rouge = Pin(4, Pin.OUT)
led_jaune = Pin(5, Pin.OUT)

#Declaration des leds sous forme de liste
LEDS = [led_verte,led_bleue,led_rouge,led_jaune]

#Eteindre toutes les leds
for item in LEDS:
    item.value(0)
sleep(1)

# --- Boucle principale ---
while True:
    #On lit le capteur
    DHT.measure()
    temp = DHT.temperature()
    hum = DHT.humidity()
    #On affiche sur la console pour vérifier la valeur
    print("Température:", temp, "°C  |  Humidité:", hum, "%")

    if temp < 22:
        #Trop froid
        led_verte.value(0)
        led_bleue.value(1)
        led_rouge.value(0)
            
    elif temp > 23:
        #Trop chaud
        led_verte.value(0)
        led_bleue.value(0)
        led_rouge.value(1)
        
    else: #temp 22 ou 23:
        #Bonne temperature
        led_verte.value(1)
        led_bleue.value(0)
        led_rouge.value(0)

    #Attendre 0.1 secondes avant de relire la température
    sleep(0.1)
