from machine import Pin
import time
import random
from machine import Pin, I2C
from machine_i2c_lcd import I2cLcd

#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
from neopixel import Neopixel
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#Version 1: Affichage des informations du jeu sur la console
#
#Version 2: Affichage des informations du jeu sur un ecran LCD
#
#Version 3: Utilisation du ruban Neopixel pour afficher le niveau de jeu par exemple
#   Niveau 1 à 4: toutes les leds en vert
#   Niveau 5 à 10:  "" en jaune
#   Niveau 10 et +: "" en rouge
#
#Version 4: Utilisation du ruban Neopixel comme bar graph...
#   Niveau 1 à 4:   leds 0-2 en vert
#   Niveau 5 à 10:  leds 0-2 en vert + leds 3-5 en jaune 
#   Niveau 10 et +: leds 0-2 en vert + leds 3-5 en jaune + leds 6-8 en rouge
#
#Pour aller plus loin:
#   Faire clignoter toutes les leds quand on perd
#   Faire une animation quand on gagne
#   Accélerer le jeu après le niveau 5

#----------------------------------------------
# Declaration des boutons et des leds
#----------------------------------------------

# Definition des LEDs
leds = [
    Pin(4, Pin.OUT), #rouge
    Pin(2, Pin.OUT), #verte
    Pin(3, Pin.OUT), #bleu
    Pin(5, Pin.OUT)  #jaune
]

# Definition des boutons
boutons = [
    Pin(0, Pin.IN, Pin.PULL_UP), #bouton sous la led rouge
    Pin(1, Pin.IN, Pin.PULL_UP), #bouton sous la led verte
    Pin(11, Pin.IN, Pin.PULL_UP), #bouton sous la led bleu
    Pin(10, Pin.IN, Pin.PULL_UP) #bouton sous la led jaune
]

# Declaration de l'ecran LCD
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
addr = i2c.scan()[0]
#print(hex(addr))
lcd = I2cLcd(i2c, addr, 2, 16)

#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# Declaration du ruban de leds
NUM_LED = 8
PIN_NB = 13
ruban = Neopixel(NUM_LED, 0, PIN_NB, "GRB")
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#--------------------------------------------------------
# Fonctions utiles pour simplifier la lisibilité du code
#--------------------------------------------------------

# Comme les leds sont branchées en "collecteur ouvert" leur commande est "inversée"
# On définit 2 functions "pour le cacher"
def led_on(index):
    leds[index].off()

def led_off(index):
    leds[index].on()

# Pour simplifier la lecture du code on regroupe toutes les commandes
# pour allumer la led pendant un instant dans une fonction
def allumer_led(index):
    led_on(index)
    time.sleep(0.5)
    led_off(index)
    time.sleep(0.2)
    
#--------------------------------------------------------
# Fonctions du jeu
#--------------------------------------------------------

# On stocke également la gestion du bouton dans une fonction 
# pour simplifier la lecture du code    
def attendre_bouton():
    while True:
        for i, bouton in enumerate(boutons):
            if bouton.value() == 0:  # appui
                led_on(i)
                while bouton.value() == 0:
                    pass
                led_off(i)
                time.sleep(0.1)
                return i
                                
def afficher_sequence():
    time.sleep(0.5)
    for couleur in sequence_jeu:
        allumer_led(couleur)
        
#--------------------------------------------------------
# Fonctions vides à compléter !!!!
#--------------------------------------------------------        

def erreur():
    # pass indique qu'on ne fait rien dans cette fonction pour l'instant 
    # et que c'est ok
    lcd.clear()
    lcd.putstr(" Perdu ! \n")
    time.sleep(1)

def victoire():
    # pass indique qu'on ne fait rien dans cette fonction pour l'instant 
    # et que c'est ok
    lcd.clear()
    lcd.putstr(" Niveau ok ! \n")
    time.sleep(1)
    
#----------------------------------------------
# Initialisation
#----------------------------------------------

# On éteint toutes les leds    
for i in range(4):
    led_off(i)       
time.sleep(1)

# On les rallume pour vérifier qu'elles sont toutes ok 
for i in range(4):
    led_on(i)       
time.sleep(1)

# On les re éteint pour commencer à jouer
for i in range(4):
    led_off(i)       
time.sleep(1)

# On vide la liste qui contient la sequence de jeu
# On va la construire pas à pas dans le code
sequence_jeu = []

#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
# on definit la luminosite des leds / 255
ruban.brightness(15)
# on eteint toute les leds
ruban.clear()
# on affiche
ruban.show()
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#----------------------------------------------
# Programme principal
#----------------------------------------------

lcd.clear()
lcd.putstr(" Jeu de Simon ! \n")
lcd.putstr(" MJC 2025-2026 \n")
time.sleep(1)

print("Jeu de Simon")

while True:
    # Ajoute une nouvelle étape
    sequence_jeu.append(random.randint(0, 3))

    # Calcul du niveau selon la longueur de la sequence
    niveau = len(sequence_jeu)
    print("Niveau :", niveau)
    
    #vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    if (niveau <= 4):
        ruban.fill((0,255,0)) # Vert        
    if (niveau > 5) and (niveau <= 10):
        ruban.fill((255,255,0)) # Jaune
    if (niveau > 10):
        ruban.fill((255,0,0)) # Rouge
    ruban.show()
    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    
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
            #print("Bravo !")
            victoire()
            
    # On attend un peu
    time.sleep(1)