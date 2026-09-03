from machine import Pin, ADC 
import time

#from constantes import *
PIN_ELECTRET = 28

#Variables globales
lut = [(52463,3),(45693,2),(35141,1),(30141,0)]

#Test
def test(micro):
    global lut
    ve = micro.read_u16() # lecture de la tension du micro-electret
    time.sleep (0.04) # tempo de 0.01s    
    for (seuil,niveau) in lut:   #pour chaque seuil, comparaison avec ve          
        if ve > seuil:              
            print(niveau)
            break # sort de la boucle pour recommencer une lecture de la tension du micro-electret

#Main    
if __name__ == '__main__':
    #Declaration
    mic = ADC(PIN_ELECTRET)
    print("Consigne: En attente d'un son")
    while True: # boucle principale
        test(mic)
       
