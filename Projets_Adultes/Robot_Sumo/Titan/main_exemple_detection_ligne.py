import time


def main_exemple_detection_ligne(r2d2):

    print("Main Exemple Detection Ligne...")
    vitesse = r2d2.vitesse_moyenne

    Tracing_1 = machine.Pin(r2d2.pin_detecteur_1, machine.Pin.IN)
    Tracing_2 = machine.Pin(r2d2.pin_detecteur_2, machine.Pin.IN)
    Tracing_3 = machine.Pin(r2d2.pin_detecteur_3, machine.Pin.IN)
    Tracing_4 = machine.Pin(r2d2.pin_detecteur_4, machine.Pin.IN)

    try:
        for i in range(0, 11):
            print("T1: %d T2: %d T3: %d T4: %d "%(Tracing_1.value(),Tracing_2.value(),Tracing_3.value(),Tracing_4.value()))
            #0=blanc 1=noir
            time.sleep(0.6)
            if Tracing_1.value() == 1:
                print('Tourne Gauche')
            elif Tracing_4.value() == 1:
                print('Tourne Droite')
            else:
                print('Avance')
    #Ctrl-C to exit
    except KeyboardInterrupt:
        print('EXIT')
        print('Stop')

if __name__ == '__main__':
    
    #r2d2_name = "PicoGo"
    r2d2_name = "Yaboom"
    #r2d2_name = "Titan"
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

    main_exemple_detection_ligne(r2d2)