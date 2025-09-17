# on a besoin des fonctions "time" et "Pin" (qui est dans "machine") donc on les importe
import time
from machine import Pin

#On choisit le Pin sur lequel on va monter la LED et on lui dit que c'est une sortie
#(pas une entree de signal) c'est a dire que la sortie PIN 0 va fournir l'energie pour commander la LED
LED = Pin(0, Pin.OUT) 
#On donne la valeur 1 à la sortie pour allumer la LED
LED.value(1)
#On lui dit de rester allumée pendant 3 secondes
time.sleep(3)
#On lui dit de s'eteindre
LED.value(0)
#On lui dit de rester éteinte pendant 2 secondes
time.sleep(2)

#fin de travail
#on peut modifier les temps
#puis il faut relancer le programme pour voir le résultat