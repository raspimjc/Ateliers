from machine import Pin
from ir_rx_nec import NEC_16
import time

#Declaration et initialisation de variables internes
data_received = False
IR_data = 0

#Definition du code de chaque touche en fonction de la telecommande utilisée
Touche_0 = 0x00
Touche_1 = 0x00
Touche_2 = 0x00
Touche_3 = 0x00
Touche_4 = 0x00
Touche_5 = 0x00
Touche_6 = 0x00
Touche_7 = 0x00
Touche_8 = 0x00
Touche_9 = 0x00
Touche_H = 0x00
Touche_D = 0x00
Touche_B = 0x00
Touche_G = 0x00
Touhe_OK = 0x00

#Fonctions utiles pour declarer la telecommande 
def callback(data, addr, ctrl):
    global data_received, IR_data
    if (data > 0):
        IR_data = data
        data_received = True
        
ir = NEC_16(Pin(3, Pin.IN), callback)

#Boucle principale:
#Récupere le code reçu et l'affiche dans la console
while True:
    if data_received:
        print('Data 0x{:02x}'.format(IR_data))
        data_received = False