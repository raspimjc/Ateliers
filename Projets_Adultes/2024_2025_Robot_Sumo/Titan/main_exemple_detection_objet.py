import time


def main_exemple_detection_objet(r2d2):

    print("Main Exemple Detection Objet...")
    vitesse = r2d2.vitesse_moyenne
    
    distance = r2d2.distance_cm("avant")
    print('Distance:', "{0:2.2f}".format(distance), 'cm')
    
    try:
        while (distance > 5):
            if (distance > 20):
                #Moteur tourne a gauche
                print('RAS')
                r2d2.vehicule("tourne_gauche",0.6,vitesse)
            else:
                #Moteur stop
                print('STOP !!!!!!!!!!!!!!!!')
                r2d2.vehicule("stop",0.5,vitesse)
                r2d2.vehicule("avance",1,vitesse)
                r2d2.vehicule("stop",0.5,vitesse)
            distance = r2d2.distance_cm("avant")
            print('Distance:', "{0:2.2f}".format(distance), 'cm')
            
        r2d2.vehicule("stop",3,vitesse)
        
    #Ctrl-C to exit
    except KeyboardInterrupt:
        print('EXIT')
        r2d2.vehicule("stop",3,vitesse)

if __name__ == '__main__':
    #r2d2_name = "PicoGo"
    #r2d2_name = "Yaboom"
    r2d2_name = "Titan"
    #r2d2_name = "Goliath"
    #r2d2_name = "Bob"
    #r2d2_name = "Phil"

    if (r2d2_name == "PicoGo"):
        from robot_picogo import RobotPicoGo
        r2d2 = RobotPicoGo()
    elif (r2d2_name == "Yaboom"):
        from robot_yaboom import RobotYaboom
        r2d2 = RobotYaboom()
    elif (r2d2_name == "Titan"):
        from robot_titan import RobotTitan
        r2d2 = RobotTitan()
    elif (r2d2_name == "Goliath"):
        from robot_goliath import RobotGoliath
        r2d2 = RobotGoliath()
    elif (r2d2_name == "Bob"):
        from robot_bob import RobotBob
        r2d2 = RobotBob()
    elif (r2d2_name == "Phil"):
        from robot_phil import RobotPhil
        r2d2 = RobotPhil()
    
    main_exemple_detection_objet(r2d2)