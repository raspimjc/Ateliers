from machine import Pin
import time
import dht

time.sleep(0.1) # Wait for USB to become ready

# CONSTANTE
# definit les seuils d'humidite bas et haut
SEUIL_HUMIDITE_BAS=30
SEUIL_HUMIDITE_HAUT=80

# FONCTION
def afficher_humidite( valeur ):
    print(f"humidite : {valeur:.1f}%")
    # A FAIRE utiliser le bandeau de led

# PROGRAMME PRINCIPAL

print("Boucle regulation humidite !")

# INIT
# initiliser le bandeau led
relais4_ventilateur = Pin(9, Pin.OUT) 
relais2_brumisateur = Pin(7, Pin.OUT)
#DHT = dht.DHT11(Pin(22)) 
DHT = dht.DHT22(Pin(22)) 

# place les actionneur dans leur etat par defaut
relais4_ventilateur.value(1)    # eteint le brumisateur
relais2_brumisateur.value(1)    # eteint la pompe
mon_etat = "attente"     # variable d'etat du programme : "humidifie" / "attente" / "ventille"

# boucle principale
while True:
    # on prend la mesure
    DHT.measure()
    # on affiche le niveau d'humidite
    afficher_humidite( DHT.humidity() )
    # en fonction de notre etat
    if mon_etat == "attente":
        # si l'humidite est en dessous du seuil bas
        if DHT.humidity() < SEUIL_HUMIDITE_BAS:
            # on allume le brumisateur
            relais2_brumisateur.value(0)
            # on eteint le ventilateur
            relais4_ventilateur.value(1)
            # on indique notre nouvel etat
            mon_etat = "humidifie"
        elif DHT.humidity() > SEUIL_HUMIDITE_HAUT:
            # on eteint le brumisateur
            relais2_brumisateur.value(1)
            # on allume le ventilateur
            relais4_ventilateur.value(0)
            # on indique notre nouvel etat
            mon_etat = "ventille"
    elif mon_etat == "humidifie":
        # on regarde si on est passe au dessus du seuil d'humidite pour arrêter le brumisateur
        if DHT.humidity() > SEUIL_HUMIDITE_BAS:
            # on eteint le brumisateur
            relais2_brumisateur.value(1)
            # on indique notre nouvel etat
            mon_etat = "attente"
    elif mon_etat == "ventille":
        # on regarde si on est passe en dessous du seuil d'humidite pour arrêter le ventilateur
        if DHT.humidity() < SEUIL_HUMIDITE_HAUT:
            # on eteint le ventilateur
            relais4_ventilateur.value(1)
            # on indique notre nouvel etat
            mon_etat = "attente"


