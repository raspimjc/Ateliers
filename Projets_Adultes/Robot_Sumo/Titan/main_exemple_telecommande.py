from ir_rx_nec import NEC_16
from machine import Pin
import time


#Fonctions utiles pour declarer la telecommande 
def callback(data, addr, ctrl):
    global data_received, IR_data
    if (data > 0):
        IR_data = data
        data_received = True
        

#Declaration et initialisation de variables internes
data_received = False
IR_data = 0

#
#<> = Fleches deplacement
#0 = Neopixel
#1 = Buzzer Zelda
#2 = Deplacement Robot
#3 = Detection objet
#4 = Affichage
#
#9 = Show
#
def main_exemple_telecommande(r2d2):

    #global r2d2
    print("Main Exemple Telecommande...")

    global data_received,IR_data
    vitesse = r2d2.vitesse_moyenne
    ir = NEC_16(Pin(r2d2.pin_telecommande, Pin.IN), callback)   

    try:
        while True:
            if data_received:
                #print('Data 0x{:02x}'.format(IR_data))
                if (IR_data == r2d2.Code_Touche_Haut):
                    print('Touche H: on avance')
                    r2d2.vehicule("avance",2,vitesse)
                    r2d2.vehicule("stop",0.5,vitesse)    

                elif (IR_data == r2d2.Code_Touche_Bas):
                    print('Touche B: on recule')
                    r2d2.vehicule("recule",2,vitesse)
                    r2d2.vehicule("stop",0.5,vitesse)    

                elif (IR_data == r2d2.Code_Touche_Droite):
                    print('Touche D: on tourne a droite')
                    r2d2.vehicule("tourne_droit",2,vitesse)
                    r2d2.vehicule("stop",0.5,vitesse)    
                    
                elif (IR_data == r2d2.Code_Touche_Gauche):
                    print('Touche G: on tourne a gauche')
                    r2d2.vehicule("tourne_gauche",2,vitesse)
                    r2d2.vehicule("stop",0.5,vitesse)    

                elif (IR_data == r2d2.Code_Touche_0):
                    print('Touche 0: neopixel')
                    main_exemple_neopixel(r2d2)

                elif (IR_data == r2d2.Code_Touche_1):
                    print('Touche 1: buzzer 12 sec')
                    main_exemple_buzzer(r2d2)

                elif (IR_data == r2d2.Code_Touche_2):
                    print('Touche 2: deplacement robot')
                    main_exemple_deplacement_robot(r2d2)
                    
                elif (IR_data == r2d2.Code_Touche_3):
                    print('Touche 3: detection objet')
                    main_exemple_detection_objet(r2d2)
                    
                elif (IR_data == r2d2.Code_Touche_4):
                    print('Touche 4: affichage')
                    if (r2d2_name == "Titan"):
                        main_exemple_lcd(r2d2)
                    else:
                        main_exemple_oled(r2d2)
                        main_exemple_oled_2(r2d2)
                        
                elif (IR_data == r2d2.Code_Touche_9):
                    print('Touche 9: SHOW !!')
                    r2d2.vehicule("avance",2,vitesse)
                    r2d2.vehicule("recule",2,vitesse)
                    r2d2.vehicule("tourne_droit",2,vitesse)
                    r2d2.vehicule("tourne_gauche",2,vitesse)
                    r2d2.vehicule("stop",0.5,vitesse)
                    main_exemple_neopixel(r2d2)
                    main_exemple_buzzer(r2d2)                    
                    if (r2d2_name == "Titan"):
                        main_exemple_lcd(r2d2)
                    else:
                        main_exemple_oled(r2d2)
                        main_exemple_oled_2(r2d2)
                    main_exemple_detection_objet(r2d2)

                else:
                    print('Touche non programmée: 0x{:02x}'.format(IR_data))
                data_received = False
    #Ctrl-C to exit
    except KeyboardInterrupt:
        print('EXIT')
        r2d2.vehicule("stop",0.5,vitesse) 

if __name__ == '__main__':
    
    from main_exemple_neopixel import *
    from main_exemple_buzzer import *
    from main_exemple_deplacement_robot import *
    from main_exemple_detection_objet import *

    #r2d2_name = "PicoGo"
    r2d2_name = "Yaboom"
    #r2d2_name = "Titan"

    if (r2d2_name == "PicoGo"):
        from robot_picogo import RobotPicoGo
        r2d2 = RobotPicoGo()
    elif (r2d2_name == "Yaboom"):
        from robot_yaboom import RobotYaboom
        from main_exemple_oled import *
        from main_exemple_oled_2 import *
        r2d2 = RobotYaboom()
    elif (r2d2_name == "Titan"):
        from robot_titan import RobotTitan
        from main_exemple_lcd import *
        r2d2 = RobotTitan()

    main_exemple_telecommande(r2d2)