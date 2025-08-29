from machine import ADC
import time


def main_exemple_lcd(r2d2):

    print("Main Exemple LCD...")
    temp = ADC(4)

    try:
        reading = temp.read_u16() * 3.3 / (65535)
        temperature = 27 - (reading - 0.706)/0.001721

        r2d2.oled.clear()
        r2d2.oled.putstr("Hello Titan !\n")
        r2d2.oled.putstr("CPU Temp:%.2f" % temperature)
        time.sleep(2)
    #Ctrl-C to exit
    except KeyboardInterrupt:
        print('EXIT')


if __name__ == '__main__':
    
    r2d2_name = "Titan"

    if (r2d2_name == "Titan"):
        from robot_titan import RobotTitan
        r2d2 = RobotTitan()
    
    main_exemple_lcd(r2d2)