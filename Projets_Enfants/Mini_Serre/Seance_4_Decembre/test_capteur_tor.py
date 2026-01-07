#=====================================================
# Detection simple d'une presence
# par un capteur TOR (Tout ou Rien)
# Affichage sur la console
#=====================================================
from machine import Pin
from time import sleep

'''
#declaration du capteur PIR
capteur = Pin(13, Pin.IN)
valeur_detection = 1

#declaration du capteur LDR
capteur = Pin(14, Pin.IN)
valeur_detection = 0
'''
#declaration du capteur SON
capteur = Pin(15, Pin.IN)
valeur_detection = 1

while True:
    valeur_lue = capteur.value()
    
    #si quelquechose a ete detecte
    if valeur_lue == valeur_detection:
        print("Presence detectée")
        
    #sinon
    else:
        print("Rien a signaler")
        
    #on attends avant de relire        
    sleep(0.01)

    
   
    


