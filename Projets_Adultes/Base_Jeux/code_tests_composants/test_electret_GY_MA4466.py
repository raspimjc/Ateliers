from machine import Pin, ADC 
import utime, time

mic = ADC(28)# initialisation de l'entrée analogique
# le préamplificateur positionne la tension moyenne à 1.65V pour avoir une sinusoide du signal complète avec la partie négative du signal.
# donc on a une plage de tension de 1.65 à 3.3V
# table de conversion des seuils (volts) en valeur numériques: mic*65536(16bits)/3,3(tension d'alim du micro-electret)
# la valeur maximale lue est definie à 3.25V donc en numerique 64543
# calcul des seuils, -0.3dB d'écart avec seuil de 64543 est = 64543*10puissance(-0.3/10)
# led 8 = 65543 (qui n'esiste pas, mais on a besoin de ce seuil)
# led 7 -0.3dB de 65543= 60235
# led 6 -0.6dB = 56215
# led 5 -0.9dB = 52463
# led 4 -1.2dB = 48961
# led 3 -1.5dB = 45693
# led 2 -1.8dB = 42643
# led 1 - 2.1 dB = 39796
# led 0 -2.4 dB = 37141
# la diminution de 0.3 dB en tension correspond à 6.7% de réduction de puissance
# la diminution de 0.46 dB en tension correspond à 10% de réduction de puissance
# la diminution de 3 dB en tension correspond à 50% de réduction de puissance
# lut = liste de seuils et de N° de led ( seuil, numero de led) = Tulpe
#lut = [(64543,8),(60235,7),(56215,6),(52463,5),(48961,4),(45693,3),(42643,2),(39796,1),(37141,0)]
lut = [(52463,3),(45693,2),(35141,1),(30141,0)]

if __name__ == '__main__':
    print("Start")

    while True: # boucle principale
        ve = mic.read_u16() # lecture de la tension du micro-electret
        #print(ve)
        time.sleep (0.04) # tempo de 0.01s
        
        for (seuil,niveau) in lut:   #pour chaque seuil, comparaison avec ve          
            if ve > seuil:              
                print(niveau)
                break # sort de la boucle pour recommencer une lecture de la tension du micro-electret
