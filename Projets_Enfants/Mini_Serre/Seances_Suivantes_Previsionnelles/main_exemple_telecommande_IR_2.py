from machine import Pin
from ir_rx_nec import NEC_16
import time

#Declaration et initialisation de variables internes
data_received = False
IR_data = 0

#Definition du code de chaque touche en fonction de la telecommande utilisée
Touche_0 = 0x19
Touche_1 = 0x45
Touche_2 = 0x46
Touche_3 = 0x47
Touche_4 = 0x44
Touche_5 = 0x40
Touche_6 = 0x43
Touche_7 = 0x07
Touche_8 = 0x15
Touche_9 = 0x09
Touche_H = 0x18
Touche_D = 0x5A
Touche_B = 0x52
Touche_G = 0x08
Touhe_OK = 0x1C

#Fonctions utiles pour declarer la telecommande 
def callback(data, addr, ctrl):
    global data_received, IR_data
    if (data > 0):
        IR_data = data
        data_received = True
        
ir = NEC_16(Pin(3, Pin.IN), callback)

#Boucle principale:
#Récupere le code reçu et selon sa valeur effectue une action (ici simple printf)
while True:
    if data_received:
        #print('Data 0x{:02x}'.format(IR_data))
        if (IR_data == Touche_0):
            print('Touche 0')
        elif (IR_data == Touche_1):
            print('Touche 1')
        else:
            print('Touche non programmée')
        data_received = False
