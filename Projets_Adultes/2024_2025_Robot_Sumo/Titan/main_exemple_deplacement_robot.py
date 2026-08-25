import time


def main_exemple_deplacement_robot(r2d2):

    print("Main Exemple Deplacement Robot...")    
    vitesse = r2d2.vitesse_moyenne

    try:
        r2d2.vehicule("avance",1,vitesse)
        r2d2.vehicule("stop",1,vitesse)    

        r2d2.vehicule("recule",1,vitesse)
        r2d2.vehicule("stop",1,vitesse)
        
        for loop in range(2):

            r2d2.vehicule("tourne_gauche",1,vitesse)
            r2d2.vehicule("stop",1,vitesse)

            r2d2.vehicule("tourne_droit",1,vitesse)
            r2d2.vehicule("stop",1,vitesse)
            
    #Ctrl-C to exit
    except KeyboardInterrupt:
        print('EXIT')
        r2d2.vehicule("stop",1,vitesse)

if __name__ == '__main__':
    
    #r2d2_name = "PicoGo"
    r2d2_name = "Yaboom"
    #r2d2_name = "Titan"
    #r2d2_name = "Bob"

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
    
    main_exemple_deplacement_robot(r2d2)