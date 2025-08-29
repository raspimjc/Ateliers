from machine import ADC
from mqtt import Mqtt
import time


def main_exemple_mqtt(r2d2):

    print("Main Exemple MQTT...")

    # declare MQTT
    mqtt = Mqtt(r2d2_name)

    temp = ADC(4)

    try:
        while True:
            reading = temp.read_u16() * 3.3 / (65535)
            temperature = 27 - (reading - 0.706)/0.001721
            print(temperature)

            # envoie des données sur MQTT
            mqtt.publish("Code", "43")
            mqtt.publish("Message", "Mon nom est {fname}, Version {age}".format(fname = r2d2_name, age = 007))
            mqtt.publish("Data/Temperature", "{0:2.2f}".format(temperature))
           
            time.sleep(2)
    #Ctrl-C to exit
    except KeyboardInterrupt:
        print('EXIT')


if __name__ == '__main__':

    #r2d2_name = "PicoGo"
    #r2d2_name = "Yaboom" ###KO, debrancher le lecteur MP3
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
    
    main_exemple_mqtt(r2d2)