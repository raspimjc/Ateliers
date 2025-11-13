from machine import xxxxxxxxx
from time import sleep
import dht

#Declaration du capteur
DHT11 = dht.DHT11(Pin(xxxxxxx))       

#Declaration des leds Pin
led_0 = Pin(xxxx, Pin.OUT)
led_1 = Pin(xxxx, xxxxxxx)
led_2 = Pin(xxxx, xxxxxxx)
led_3 = Pin(xxxx, xxxxxxx)

#Declaration des leds sous forme de liste
LEDS = [xxxx, xxxxx, xxxxx, xxxxxxx]

#Eteindre toutes les leds
for item in LEDS:
    item.value(xxxx)
    

# --- Boucle principale ---
while True:
    #On lit le capteur
    DHT11.measure()
    temp = DHT11.temperature()
    hum = DHT11.humidity()
    #On affiche sur la console pour vérifier la valeur
    print("Température:", temp, "°C  |  Humidité:", hum, "%")

    if temp < 21:
        #Eteindre toutes les leds
        for i in range(0, 4):
            LEDS[i].value(0)
            
    elif temp < 22:
        #Allumer la premiere led, eteindre les autres
        LEDS[0].value(1)
        LEDS[1].value(0)
        LEDS[2].value(0)
        LEDS[3].value(0)
        
    elif temp < 23:
        #Allumer les 2 premieres leds, eteindre les autres
        LEDS[0].value(1)
        LEDS[1].value(1)
        LEDS[2].value(0)
        LEDS[3].value(0)
        
    elif temp < 24:
        #Allumer les 3 premieres leds, eteindre la derniere
        xxxxxxxxxxxxx
        xxxxxxxxxxxxx
        xxxxxxxxxxxxx
        xxxxxxxxxxxxx
        
    else:
        #Allumer toutes les leds
        xxxxxxxxxxxxx
    
    #Attendre 2 secondes avant de relire la température
    xxxxxxxxxxxxx(2)
