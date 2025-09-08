from machine import Pin
from robot import Robot
from moteur_goliath import Moteur
from ultrason_basic import Ultrason
import time



class RobotGoliath(Robot):
    
    def __init__(self):
        #Moteur
        self.io_1 =Pin(13 , Pin.OUT)
        self.io_2 =Pin(12 , Pin.OUT)
        self.io_pwm =Pin(11 )
        self.moteur_droit = Moteur(self.io_1, self.io_2, self.io_pwm)              
        self.io_3 =Pin(17 , Pin.OUT)
        self.io_4 =Pin(16 , Pin.OUT)
        self.io_pwm2 =Pin(18 )
        self.moteur_gauche = Moteur(self.io_3, self.io_4, self.io_pwm2)   
        self.vitesse_moyenne = 1#Pas de vitesse
        #Ultrason
        self.us_avant = Ultrason(trigger_pin=1, echo_pin=0)
    
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
                
    # obtient la distance d'un ou plusieurs détecteur
    # detecteur : "avant"
    def distance_cm(self, detecteur):
        return self.us_avant.distance_cm()

if __name__ == '__main__':
    print('test classe robot')    
    # declare le robot
    r2d2 = RobotGoliath()
    # lecture de la distance
    distance = r2d2.distance_cm("avant")
    print('Distance:', "{0:2.2f}".format(distance), 'cm')
    # avance
    print('Avance')
    r2d2.moteur("droit","avant",60)
    r2d2.moteur("gauche","avant",60)
    time.sleep(0.6)    
    # stop
    r2d2.moteur("droit","stop",60)
    r2d2.moteur("gauche","stop",60)
    time.sleep(0.6)    
    # recule
    print('Recule')
    r2d2.moteur("droit","arriere",60)
    r2d2.moteur("gauche","arriere",60)
    time.sleep(0.6)    
    # stop
    r2d2.moteur("droit","stop",60)
    r2d2.moteur("gauche","stop",60)
    time.sleep(0.6)    
    # tourne
    print('Tourne')
    r2d2.moteur("droit","avant",60)
    r2d2.moteur("gauche","arriere",60)
    time.sleep(0.6)    
    # stop
    r2d2.moteur("droit","stop",60)
    r2d2.moteur("gauche","stop",60)
    time.sleep(0.6)    
    # tourne
    print('Tourne de l autre cote')
    r2d2.moteur("droit","arriere",60)
    r2d2.moteur("gauche","avant",60)
    time.sleep(0.6)    
    # stop
    r2d2.moteur("droit","stop",60)
    r2d2.moteur("gauche","stop",60)
    time.sleep(0.6)    
  