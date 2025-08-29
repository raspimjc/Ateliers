from robot import Robot
from moteur_bob import Moteur
from ultrason_bob import Ultrason
from PicoAutonomousRobotics import KitronikPicoRobotBuggy
import time



class RobotBob(Robot):
    
    def __init__(self):
        self.kprb = KitronikPicoRobotBuggy()
        #Moteur
        self.moteur_gauche = Moteur(self.kprb, 'l')
        self.moteur_droit = Moteur(self.kprb, 'r')
        self.vitesse_moyenne = 1#Pas de vitesse
        #Ultrason
        self.us_avant = Ultrason(self.kprb)
        
    
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
    r2d2 = RobotBob()
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
