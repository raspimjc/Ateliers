from machine import Pin, PWM
import time

#Declaration du bouton
bouton = Pin(0, machine.Pin.IN, Pin.PULL_UP) 

#Declaration du servo
servo = PWM(Pin(12))   
servo.freq(50)
servo.duty_u16(2000)

#Declaration d'une variable compteur
compteur = 2000

while True:
    #On regarde l'etat du bouton
    if bouton.value() == 0:
        compteur = compteur + 1000
        print("Compteur = ",compteur)                        
    
    #On verifie et on corrige si besoin
    #les valeurs du compteur
    if (compteur > 8000):
        compteur = 8000
    
    #On envoie la valeur au servo
    servo.duty_u16(compteur)
    
    #On attends un peu (pour éviter les rebonds du BP)
    time.sleep(0.3)

