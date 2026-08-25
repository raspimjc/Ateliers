from machine import Pin
from time import sleep
import dht

#Declaration du capteur
DHT = dht.DHT11(Pin(22))  
#DHT = dht.DHT22(Pin(22))            

#Declaration des leds
led_0 = Pin(6, Pin.OUT)
led_1 = Pin(7, Pin.OUT)
led_2 = Pin(8, Pin.OUT)
led_3 = Pin(9, Pin.OUT)

#Declaration des leds sous forme de liste
LEDS = [led_0,led_1,led_2,led_3]

#Eteindre toutes les leds
for item in LEDS:
    item.value(0)
    

# --- Boucle principale ---
while True:
    #On lit le capteur
    DHT.measure()
    temp = DHT.temperature()
    hum = DHT.humidity()
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
        LEDS[0].value(1)
        LEDS[1].value(1)
        LEDS[2].value(1)
        LEDS[3].value(0)
        
    else:
        #Allumer toutes les leds
        for i in range(0, 4):
            LEDS[i].value(1)

    #Attendre 2 secondes avant de relire la température
    sleep(2)
