from machine import Pin, ADC
import time

# declaration du potentiometre (ADC 0)
potar = ADC(0)

# fonction qui va lire la valeur du potentiometre
def lit_potar():
    global potar
    return potar.read_u16()

# initialisation des variables
old_val_potar = lit_potar()

# boucle principale
while True:
    # lit la valeur du potentiometre
    valeur_potar  = lit_potar()
    # test si la valeur lue est différente de la précédente
    if valeur_potar != old_val_potar:
        # affiche la valeur du potentiometre
        print(valeur_potar)
        # sauvegarde la nouvelle valeur du potentiometre
        old_val_potar = valeur_potar
    time.sleep(0.3)
    
