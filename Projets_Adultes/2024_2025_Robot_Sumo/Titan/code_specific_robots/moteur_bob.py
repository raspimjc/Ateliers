from PicoAutonomousRobotics import KitronikPicoRobotBuggy
import time

class Moteur:
    def __init__(self, kprBuggy, moteur_cote = 'l'):
        self.kpr = kprBuggy
        self.moteur_cote =  moteur_cote
        self.stop()
        print('pense a mettre le switch a ON')

    def marcheAvant(self, vitesse=50):
        self.kpr.motorOn(self.moteur_cote, 'f',vitesse)
        
    def marcheArriere(self, vitesse=50):
        self.kpr.motorOn(self.moteur_cote, 'r',vitesse)
        
    def stop(self):
        self.kpr.motorOff(self.moteur_cote)
    
if __name__ == '__main__':
    print('test classe moteur')
    kprb = KitronikPicoRobotBuggy()
    # Initialisation des moteurs
    m1 = Moteur(kprb, 'l')
    m2 = Moteur(kprb, 'r')
    print('le robot avance')    
    m1.marcheAvant()
    m2.marcheAvant()
    time.sleep(0.2)
    print('le robot s arrete')    
    m1.stop()
    m2.stop()    
    
    
