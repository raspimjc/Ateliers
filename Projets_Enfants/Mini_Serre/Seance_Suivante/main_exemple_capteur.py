#=====================================================
# Detection simple d'une presence par PIR ou LDR
# Affichage sur la console
#=====================================================
from machine import Pin
from time import sleep


# declaration du capteur
capteur = Pin(13, Pin.IN)
valeur_detection = 0 # 1 pour le PIR, 0 pour la LDR

while True:
    valeur_lue = capteur.value()
    
    #si quelquechose a ete detecte
    if valeur_lue == valeur_detection:
        print("Presence detectée")
    #sinon
    else:
        print("Rien a signaler")
    #on attends 1 seconde avant de relire
        
    sleep(1)

    
   
    


