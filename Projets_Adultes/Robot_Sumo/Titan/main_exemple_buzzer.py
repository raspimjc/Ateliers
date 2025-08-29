from classe_music_P_zelda import Music_P_zelda
import time
    
    
def main_exemple_buzzer(r2d2):

    print("Main Exemple Buzzer...")
    
    music = Music_P_zelda(r2d2.buzzer)
    melodie = music.The_Legend_of_Zelda_theme
   
    try:
        music.joue_melodie_timed(melodie,12)
    #Ctrl-C to exit
    except KeyboardInterrupt:
        print('EXIT')

if __name__ == '__main__':
    
    #r2d2_name = "PicoGo"
    #r2d2_name = "Yaboom"
    r2d2_name = "Titan"
    
    if (r2d2_name == "PicoGo"):
        from robot_picogo import RobotPicoGo
        r2d2 = RobotPicoGo()
    elif (r2d2_name == "Yaboom"):
        from robot_yaboom import RobotYaboom
        r2d2 = RobotYaboom()
    elif (r2d2_name == "Titan"):
        from robot_titan import RobotTitan
        r2d2 = RobotTitan()
    
    main_exemple_buzzer(r2d2)