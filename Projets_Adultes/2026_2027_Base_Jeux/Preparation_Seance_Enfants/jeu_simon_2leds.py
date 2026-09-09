from machine import Pin
import time
import random

# Declaration des boutons et des leds
leds = [
    Pin(6, Pin.OUT), #rouge
    Pin(7, Pin.OUT) #verte
]

boutons = [
    Pin(16, Pin.IN, Pin.PULL_UP), #bouton sous la led rouge
    Pin(17, Pin.IN, Pin.PULL_UP) #bouton sous la led verte
]

# Fonctions utiles pour simplifier la lisibilité du code
def allumer_led(index):
    leds[index].on()
    time.sleep(0.5)
    leds[index].off()
    time.sleep(0.2)
    
# On stocke également la gestion du bouton dans une fonction 
# pour simplifier la lecture du code    
def attendre_bouton():
    while True:
        for i, bouton in enumerate(boutons):
            if bouton.value() == 0:  # appui
                leds[i].on()
                while bouton.value() == 0:
                    pass
                leds[i].off()
                time.sleep(0.1)
                return i
                                
def afficher_sequence():
    time.sleep(0.5)
    for couleur in sequence_jeu:
        allumer_led(couleur)
        
# Fonctions vides à compléter !!!!
def erreur():
    # pass indique qu'on ne fait rien dans cette fonction pour l'instant 
    # et que c'est ok
    pass

def victoire():
    # pass indique qu'on ne fait rien dans cette fonction pour l'instant 
    # et que c'est ok
    pass
    
# Initialisation
# On éteint toutes les leds    
for i in range(2):
    leds[i].off()       
time.sleep(1)

# On les rallume pour vérifier qu'elles sont toutes ok 
for i in range(2):
    leds[i].on()       
time.sleep(1)

# On les re éteint pour commencer à jouer
for i in range(2):
    leds[i].off()        
time.sleep(1)

# On vide la liste qui contient la sequence de jeu
# On va la construire pas à pas dans le code
sequence_jeu = []


# Programme principal
print("Jeu de Simon")

while True:
    # Ajoute une nouvelle étape
    sequence_jeu.append(random.randint(0, 1))

    # Calcul du niveau selon la longueur de la sequence
    niveau = len(sequence_jeu)
    print("Niveau :", niveau)
    
    # On joue la séquence
    afficher_sequence()

    # Vérification de la saisie du joueur
    perdu = False
    for couleur_attendue in sequence_jeu:
        choix_joueur = attendre_bouton()
        if choix_joueur != couleur_attendue:
            print("Perdu ! Score :", len(sequence_jeu) - 1)
            erreur()
            sequence_jeu = [] #on recommence, on efface la sequence de jeu
            break
        else:
            victoire()
            
    # On attend un peu
    time.sleep(1)