from machine import Pin, PWM
from servo import Servo
import time
from constantes_laurence import *

moteur_milieu=Servo(pin=PIN_SERVO) 

moteur_milieu_min = 90
moteur_milieu_max = 180

temps_attente = 0.1

def motor_stable():
    moteur_milieu.move(moteur_milieu_min) 
    time.sleep(temps_attente)

def test_amplitude(moteur,angle_min,angle_max):
    for angle in range (moteur_milieu_min,moteur_milieu_max):
        if (angle % 2 == 0): #De 2 en 2
            moteur.move(angle)
            time.sleep(temps_attente)
    for angle in range (moteur_milieu_max,moteur_milieu_min,-1):
        if (angle % 2 == 0):
            moteur.move(angle)
            time.sleep(temps_attente)


motor_stable() #Position Min
test_amplitude(moteur_milieu,moteur_milieu_min,moteur_milieu_max)

