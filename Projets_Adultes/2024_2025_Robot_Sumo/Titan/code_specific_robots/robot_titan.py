from robot import Robot
from moteur_titan import Moteur
from ultrason_basic import Ultrason
from neopixel import Neopixel
from buzzer import Buzzer
from machine_i2c_lcd import I2cLcd

from machine import Pin,I2C
import time

class RobotTitan(Robot):
    
    def __init__(self):
        #Moteur
        self.io_1 =Pin(8 , Pin.OUT)
        self.io_2 =Pin(9 , Pin.OUT)
        self.io_3 =Pin(10 , Pin.OUT)
        self.io_4 =Pin(11 , Pin.OUT)
        #self.moteur_droit = Moteur(self.io_1, self.io_2)              
        #self.moteur_gauche = Moteur(self.io_3, self.io_4)  
        self.moteur_gauche = Moteur(self.io_1, self.io_2)              
        self.moteur_droit = Moteur(self.io_3, self.io_4)  
        self.vitesse_moyenne = 1 #Pas de vitesse sur la carte Cytron
        #Ultrason
        self.us_avant = Ultrason(trigger_pin=2, echo_pin=3)
        #Buzzer
        self.pin_buzzer = 22
        self.volume_moyen = 600
        self.buzzer = Buzzer(self.pin_buzzer)
        self.buzzer.set_volume(self.volume_moyen)
        self.buzzer.stop()
        #Neopixel
        self.pin_neopixel = 0 #Gauche
        #self.pin_neopixel = 1 #Droit
        self.nombre_leds = 8
        self.leds = Neopixel(self.nombre_leds, 0, self.pin_neopixel, "GRB")
        #Telecommande IR
        self.pin_telecommande = 5
        self.Code_Touche_Haut   = 0x18
        self.Code_Touche_Droite = 0x5A
        self.Code_Touche_Bas    = 0x52
        self.Code_Touche_Gauche = 0x08
        self.Code_Touche_0 = 0x19
        self.Code_Touche_1 = 0x45
        self.Code_Touche_2 = 0x46
        self.Code_Touche_3 = 0x47
        self.Code_Touche_4 = 0x44
        self.Code_Touche_5 = 0x40
        self.Code_Touche_6 = 0x43
        self.Code_Touche_7 = 0x07
        self.Code_Touche_8 = 0x15
        self.Code_Touche_9 = 0x09
        #LCD
        self.oled_width = 16
        self.oled_height = 2
        self.oled_color = 0 #Oled basic, no color
        self.pin_i2c_sda = 16
        self.pin_i2c_scl = 17
        self.i2c_num = 0
        self.i2c_dev = I2C(self.i2c_num, scl=Pin(self.pin_i2c_scl), sda=Pin(self.pin_i2c_sda), freq=200000)
        self.addr = self.i2c_dev.scan()[0]
        self.oled = I2cLcd(self.i2c_dev, self.addr, self.oled_height, self.oled_width)
        #Detecteurs de ligne
        #***FAIRE DES FCTS POUR EXTRAIRE L INFO***TROP DIFFERENTS SELON LES ROBOTS

    ###### Fonction moteur ######        
    # controle d'un moteur ou de plusieurs moteur
    # moteur : "droit, "gauche"
    # ordre : "avant", "arriere", "stop"
    # vitesse : vitesse du moteur
    def moteur(self, moteur:str(), ordre:str(), vitesse=50):
        _mot = self.moteur_gauche
        if "droit" == moteur:
            _mot = self.moteur_droit
            
        if "avant" == ordre :
            _mot.marcheAvant()
        elif "arriere" == ordre :
            _mot.marcheArriere()
        else :
            _mot.stop()

    ###### Fonction vehicule ######     
    # Controle du vehicule
    # direction: "avance", "recule","tourne_droit", "tourne_gauche","stop"
    # duree
    # vitesse
    def vehicule(self, ordre:str(), duree=3, vitesse=60):
        if "avance" == ordre :
            self.moteur("droit","avant",vitesse)
            self.moteur("gauche","avant",vitesse)
            time.sleep(duree)
        elif "recule" == ordre :
            self.moteur("droit","arriere",vitesse)
            self.moteur("gauche","arriere",vitesse)
            time.sleep(duree)
        elif "tourne_droit" == ordre :
            self.moteur("droit","arriere",vitesse)
            self.moteur("gauche","avant",vitesse)
            time.sleep(duree)
        elif "tourne_gauche" == ordre :
            self.moteur("droit","avant",vitesse)
            self.moteur("gauche","arriere",vitesse)
            time.sleep(duree)
        else:
            self.moteur("droit","stop",vitesse)
            self.moteur("gauche","stop",vitesse)
            time.sleep(duree)
    
    ###### Fonction ultrason ######          
    # obtient la distance d'un ou plusieurs détecteur
    # detecteur : "avant"
    def distance_cm(self, detecteur):
        return self.us_avant.distance_cm()



if __name__ == '__main__':
    print('test classe robot')    
    # declare le robot
    r2d2 = RobotTitan()
    #
    # Test de la fonction distance
    #
    distance = r2d2.distance_cm("avant")
    print('Distance:', "{0:2.2f}".format(distance), 'cm')
    #
    # Test des fonctions vehicule
    #
    print('Fonctions Vehicule ....')
    print('Avance')
    r2d2.vehicule("avance",3,60)
    r2d2.vehicule("stop",1,0)
    print('Recule')
    r2d2.vehicule("recule",3,60)
    r2d2.vehicule("stop",1,0)
    print('Tourne a droite')
    r2d2.vehicule("tourne_droit",3,60)
    r2d2.vehicule("stop",1,0)
    print('Tourne a gauche')
    r2d2.vehicule("tourne_gauche",3,60)
    r2d2.vehicule("stop",1,0)
