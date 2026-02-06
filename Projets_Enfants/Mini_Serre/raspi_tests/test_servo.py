from machine import Pin, PWM
from time import sleep

servo = PWM(Pin(12))   # fil jaune sur GPIO 12
servo.freq(50)

while True:
    servo.duty_u16(2000)  # gauche - angle 0 degrés
    sleep(1)

    servo.duty_u16(5000)  # milieu - angle 90 degrés
    sleep(1)

    servo.duty_u16(8000)  # droite - angle 180 degrés
    sleep(1)