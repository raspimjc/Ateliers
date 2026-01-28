# Pilotage d'un servo-moteur SG90 pour lever  le capot de la serre
# on va donner une impulsion au servo-moteur et il va tourner d'un certain angle
# on va le commander aussi avec les boutons poussoirs ouvrir et fermer
# si on relache le PB, le servo s'rretera en position intermédiaire

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

# definition de l'increment de pas du servomoteur
Increment=100

# positionnement à 0 capot fermé
Pulseinit = 5300 #On va pouvoir aller de "pulse"= 5300 à 8300 représentant un angle de rotation
#de 0° à 90° du servo-moteur, 
servo.duty_u16(Pulseinit) #fait tourner le servo-moteur de l'angle correpondant à "pulseinit"
print('capot fermé')
Pulse = Pulseinit # "Pulse" va être la variable que l'on va faire bouger pour commander le servo moteur
# on l'initialise avec la valeur de "pulseinit" au début
sleep_ms(50)


while True :
    # on ouvre
    if 5200<=Pulse<= 8300:				# arrêt de la commande à 8300
        if BP_Ouvre.value() == 0:     # if BP_Ouvre.value() == 0: # on teste si le niveau
                                        #de tension sur le GPIO est à 0V ou pas
                                        # si oui, alors on fait ce qu'il y a sur les lignes suivantes
        
            Pulse = Pulse + Increment   # Pulse= Pulse + Increment #on ajoute la valeur de la variable Increment
                                        # à l'angle précédant
                                        # il peut monter à 8200+100, il faut pouvoir redescendre
                                        # donc 8400 au "if" ci dessous 
            print("Pulse = ", Pulse, "  on ouvre")
            servo.duty_u16(Pulse)
            
    # on ferme
    if 5300<= Pulse<= 8400:   			# arrêt de la commande à 5300
        if BP_Ferme.value() == 0:	# if BP_Ferme.value() == 0: # on teste si le niveau de tension
                                        #sur le GPIO est à 0V ou pas
                                        # si oui, alors on fait ce qu'il y a sur les lignes suivantes
            Pulse = Pulse - Increment  # il peut descendre à 5300 -100, il faut pouvoir remonter
                                        #donc 5200 au "if" ci dessus
            print("Pulse = ", Pulse, "  on ferme")
            servo.duty_u16(Pulse)
        sleep_ms(100)   
    
    # en dehors de la plage 5200-8400, on ne fait rien
    
    
    
    
       
       
       
            
    