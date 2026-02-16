# ====================================================================
# En utilisant la bibliotheque de codes:
# Dès que le PIR detecte une présence, 
#   - on allume le ruban de leds
#   - on affiche un message de bienvenue sur le LCD (1ere ligne)
#   - on va lire la température et l'humidité sur le capteur DHT
#   - on les affiche sur l'ecran LCD (2ieme ligne)
#   - Pendant 10 secondes on effectue le comportement suivant
#       - A chaque appui sur un bouton, 
#       - on allume la led correspondante au bouton
#       - on fait tourner le servo d'un certain angle
# ====================================================================

from machine import Pin, I2C, ADC, PWM
from neopixel import Neopixel
from machine_i2c_lcd import I2cLcd
import dht
from time import sleep
from time import ticks_ms, ticks_diff

#declaration du capteur PIR
capteur = Pin(18, Pin.IN)
valeur_detection = 1

# declaration du ruban de leds
NUM_LED = 8
PIN_NB = 13
leds = Neopixel(NUM_LED, 0, PIN_NB, "GRB")

# on definit la luminosite des leds / 255
leds.brightness(15)
# on eteint toute les leds
leds.clear()
# on affiche
leds.show()

#Declaration de l'ecran LCD
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
addr = i2c.scan()[0]
print(hex(addr))
lcd = I2cLcd(i2c, addr, 2, 16)

#Declaration du capteur
#DHT = dht.DHT11(Pin(22))  
DHT = dht.DHT22(Pin(22))  

#Declaration des boutons
bp1 = Pin(0, machine.Pin.IN, Pin.PULL_UP) 
bp2 = Pin(1, machine.Pin.IN, Pin.PULL_UP) 

valeur_bp1 = 0
valeur_bp2 = 0

#Declaration des leds
led_1 = Pin(2, Pin.OUT)
led_2 = Pin(3, Pin.OUT)
led_3 = Pin(4, Pin.OUT)
led_4 = Pin(5, Pin.OUT)

#Eteindre toutes les leds
led_1.value(0)
led_2.value(0)
led_3.value(0)
led_4.value(0)

#Declaration du servo
servo = PWM(Pin(12))  
servo.freq(50)
servo.duty_u16(2000)  # gauche - angle 0 degrés

# On regarde la valeur des boutons pendant 5 secondes
timeout = 10000  # 10000 ms = 10 secondes
debut = ticks_ms()

while True:
    valeur_lue = capteur.value()
    
    #si quelquechose a ete detecte
    if valeur_lue == valeur_detection:
        print("Presence detectée")
        # on allume toutes les leds du sapin en rouge
        leds.fill((255,0,0))
        leds.show()   
        # on affiche un message de bienvenue
        lcd.putstr(" Hello Raspi ! \n")

        #On lit le capteur
        DHT.measure()
        temp = DHT.temperature()
        hum = DHT.humidity()

        #On affiche sur l'ecran LCD
        lcd.putstr(f"{temp}C {hum}% \n")

        # On regarde la valeur des boutons jusqu'a timeout
        while ticks_diff(ticks_ms(), debut) < timeout:

            valeur_bp1 = bp1.value()
            valeur_bp2 = bp2.value()

            if valeur_bp1 == 0:
                led_1.value(1)
                servo.duty_u16(3000)  
            else:
                led_1.value(0)      
            if valeur_bp2 == 0:
                led_2.value(1)
                servo.duty_u16(4000)  
            else:
                led_2.value(0)    
            '''        
            if valeur_bp3 == 0:
                led_3.value(1)
                servo.duty_u16(5000)  
            else:
                led_3.value(0)
            if valeur_bp4 == 0:
                led_4.value(1)
                servo.duty_u16(6000)  
            else:
                led_4.value(0)   
            '''               
            sleep(0.05)  # petite pause pour stabilité (50 ms)      
    #sinon
    else:
        print("Rien a signaler")
        # on eteint les leds du sapin
        leds.clear() # equivalent a: leds.fill((0,0,0))
        leds.show()
        # on eteint l'ecran LCD
        lcd.clear()

    #on attends avant de relire        
    sleep(1)
