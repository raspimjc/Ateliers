from machine import Pin
import time
import dht

time.sleep(0.1) # Wait for USB to become ready

# CONSTANTES
# definit les seuils d'humidite bas et haut
SEUIL_HUMIDITE_BAS=58
SEUIL_HUMIDITE_HAUT=60

# FONCTIONS
def afficher_etat_humidite( etat, valeur ):
    print(f"etat : {etat}")
    print(f"humidite : {valeur:.1f}%")
    
def allumer_brumisateur( relais ):
    relais.value(0)
    time.sleep(0.1)
    relais.value(1)

def eteindre_brumisateur( relais ):
    relais.value(0)
    time.sleep(0.1)
    relais.value(1)
    time.sleep(0.5)
    relais.value(0)
    time.sleep(0.1)
    relais.value(1)
    
def allumer_ventilateur( relais ):
    relais.value(0)

def eteindre_ventilateur( relais ):
    relais.value(1)


# PROGRAMME PRINCIPAL

print("Boucle regulation humidite !")

# INIT
relais4_ventilateur = Pin(9, Pin.OUT) 
relais2_brumisateur = Pin(7, Pin.OUT)
#DHT = dht.DHT11(Pin(22)) 
DHT = dht.DHT22(Pin(22)) 
time.sleep(1) # attente que le capteur humidité soit opérationnel

# place les actionneurs dans leur etat par defaut
eteindre_ventilateur(relais4_ventilateur)  # eteint le ventilateur

mon_etat = "attente"     # variable d'etat du programme : "humidifie" / "attente" / "ventille"

# boucle principale
while True:

    # on prend la mesure
    DHT.measure()
    
    # on affiche le niveau d'humidite
    afficher_etat_humidite( mon_etat, DHT.humidity() )
    
    # en fonction de notre etat
    if mon_etat == "attente":
        # si l'humidite est en dessous du seuil bas
        if DHT.humidity() < SEUIL_HUMIDITE_BAS:
            # on allume le brumisateur
            allumer_brumisateur(relais2_brumisateur)
            # on indique notre nouvel etat
            mon_etat = "humidifie"
        elif DHT.humidity() > SEUIL_HUMIDITE_HAUT:
            # on allume le ventilateur
            allumer_ventilateur(relais4_ventilateur)
            # on indique notre nouvel etat
            mon_etat = "ventille"
            
    elif mon_etat == "humidifie":
        # on regarde si on est passe au dessus du seuil d'humidite pour arrêter le brumisateur
        if DHT.humidity() > SEUIL_HUMIDITE_BAS:
            # on eteint le brumisateur
            eteindre_brumisateur(relais2_brumisateur)
            # on indique notre nouvel etat: attente
            mon_etat = "attente"
            
    elif mon_etat == "ventille":
        # on regarde si on est passe en dessous du seuil d'humidite pour arrêter le ventilateur
        if DHT.humidity() < SEUIL_HUMIDITE_HAUT:
            # on eteint le ventilateur
            eteindre_ventilateur(relais4_ventilateur)
            # on indique notre nouvel etat: attente
            mon_etat = "attente"



