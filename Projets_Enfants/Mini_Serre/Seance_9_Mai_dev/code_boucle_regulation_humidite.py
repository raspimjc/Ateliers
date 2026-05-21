from machine import Pin
import time
import dht

time.sleep(0.1) # Wait for USB to become ready

# CONSTANTE
# definit les seuils d'humidite bas et haut
SEUIL_HUMIDITE_BAS=58
SEUIL_HUMIDITE_HAUT=60

# FONCTION
def afficher_humidite( valeur ):
    print(f"humidite : {valeur:.1f}%")
    # A FAIRE utiliser le bandeau de led

def allumer_brumisateur( brum ):
    brum.value(0)
    time.sleep(0.1)
    brum.value(1)

def eteindre_brumisateur( brum ):
    brum.value(0)
    time.sleep(0.1)
    brum.value(1)
    time.sleep(0.5)
    brum.value(0)
    time.sleep(0.1)
    brum.value(1)

# PROGRAMME PRINCIPAL

print("Boucle regulation humidite !")

# INIT
# initiliser le bandeau led
relais4_ventilateur = Pin(9, Pin.OUT) 
relais2_brumisateur = Pin(7, Pin.OUT)
#DHT = dht.DHT11(Pin(22)) 
DHT = dht.DHT22(Pin(22)) 
time.sleep(1) # attente que le capteur humidité soit opérationnel

# place les actionneur dans leur etat par defaut
relais4_ventilateur.value(1)    # eteint le ventilateur
mon_etat = "attente"     # variable d'etat du programme : "humidifie" / "attente" / "ventille"

# boucle principale
while True:
    # on prend la mesure
    DHT.measure()
    # on affiche le niveau d'humidite
    afficher_humidite( DHT.humidity() )
    print(f"etat {mon_etat}")
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
            relais4_ventilateur.value(0)
            # on indique notre nouvel etat
            mon_etat = "ventille"
    elif mon_etat == "humidifie":
        # on regarde si on est passe au dessus du seuil d'humidite pour arrêter le brumisateur
        if DHT.humidity() > SEUIL_HUMIDITE_BAS:
            # on eteint le brumisateur
            eteindre_brumisateur(relais2_brumisateur)
            # on indique notre nouvel etat
            mon_etat = "attente"
    elif mon_etat == "ventille":
        # on regarde si on est passe en dessous du seuil d'humidite pour arrêter le ventilateur
        if DHT.humidity() < SEUIL_HUMIDITE_HAUT:
            # on eteint le ventilateur
            relais4_ventilateur.value(1)
            # on indique notre nouvel etat
            mon_etat = "attente"



