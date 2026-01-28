# Pilotage d'un servo-moteur SG90 pour lever  le capot de la serre
# on va donner une impulsion au servo-moteur et il va tourner d'un certain angle
# l'asservissement de la position est géré par l'électronique du servo moteur
# on va le commander avec les boutons poussoirs ouvrir et fermer
# l'angle est déterminé à l'avance, une valeur pour ouvert et une valeur pour fermé


#initialisation 
from machine import Pin, PWM #import des fonctions que l'on a besoin à partir des modules "machine, time,..."

from time import sleep_ms

# initialisation des boutons, N° du GPIO, Pin en entrée, Pin mis à 3.3V (tension haute)
#le niveau de tension sur l'entrée du GPIO va baisser à 0V lorsque l'on va appuyer sur le BP
BP_Ferme = Pin(0, machine.Pin.IN, Pin.PULL_UP) # bouton de gauche
BP_Ouvre = Pin(1, machine.Pin.IN, Pin.PULL_UP) # bouton de droite

servo = PWM(Pin(12))# initialisation de la commande du PWM sur le Pin GPIO17

servo.freq(50) #PWM à 50 hertz fréquence fixe, soit 20ms de temps de cycle, après il faut faire
# varier le rapport cyclique pour changer l'angle du servo



while True:
    if BP_Ouvre.value() == 0:
        
        Pulse = 8000
        servo.duty_u16(Pulse)
        
    if BP_Ferme.value() == 0:
        Pulse = 5000
        servo.duty_u16(Pulse)    
    
    sleep_ms(100)
    
# si l'on appuie deux fois de suite sur 1 des boutons, la consigne ne change pas donc le servo moteur ne bouge pas