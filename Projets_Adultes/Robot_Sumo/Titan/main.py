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

from main_exemple_telecommande import *
main_exemple_telecommande(r2d2)
