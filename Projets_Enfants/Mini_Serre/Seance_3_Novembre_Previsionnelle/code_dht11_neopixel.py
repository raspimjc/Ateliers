from machine import Pin
from time import sleep
from neopixel import Neopixel
import dht


#Declaration du capteur
DHT11 = dht.DHT11(Pin(22))       

#Declaration du ruban de leds
NUM_LED = 20
PIN_NB = 0
leds = Neopixel(NUM_LED, 0, PIN_NB, "GRB")

#On definit la luminosite des leds / 255
leds.brightness(15)
#On eteint le ruban
leds.clear()
#On affiche
leds.show()

while True:
    #On lit le capteur
    DHT11.measure()
    temp = DHT11.temperature()
    hum = DHT11.humidity()
    #On affiche sur la console pour vérifier la valeur
    print("Température:", temp, "°C  |  Humidité:", hum, "%")

    #si la temperature est inférieure à 21
    if temp < 21:
        #Allumer le ruban en bleu
        leds.fill((0,0,255))
    
    #si la temperature est inférieure à 22
    elif temp < 22:
        #Allumer le ruban en vert
        leds.fill((0,255,0))
        
    #si la temperature est inférieure à 23
    elif temp < 23:
        #Allumer le ruban en orange
        leds.fill((255,127,0))

    #si la temperature est supérieure ou égale à 24      
    else: #temp >= 24:
        #Allumer le ruban en rouge
        leds.fill((255,0,0))

    #On affiche
    leds.show()        
    
    #Attendre 2 secondes avant de relire la température
    sleep(2)
