
from machine import Pin, I2C
import time
from time import sleep
from imu import MPU6050
from fusion import Fusion

#from constantes import *
ACCGYR_I2C_ID = 1
PIN_ACCGYR_SCL = 15
PIN_ACCGYR_SDA = 14


#Variables globales
date_dernier_appui = time.ticks_ms()


#Test
def test(fuse,imu):
    global date_dernier_appui
    if time.ticks_diff(time.ticks_ms(), date_dernier_appui) > 300: 
        date_dernier_appui = time.ticks_ms() # "remise a zero"
        fuse.update_nomag(imu.accel.xyz, imu.gyro.xyz)
        if (fuse.roll > 20):
            print("deplacement_gauche")
        elif (fuse.roll < (-20)):
            print("deplacement_droite")
        elif (fuse.pitch > 20):
            print("deplacement_bas")
        elif (fuse.pitch < (-20)):
            print("deplacement_haut")

#Main    
if __name__ == '__main__':
    #Declaration
    i2c = I2C(ACCGYR_I2C_ID, sda=Pin(PIN_ACCGYR_SDA), scl=Pin(PIN_ACCGYR_SCL), freq=10000)
    imu = MPU6050(i2c)
    fuse = Fusion()
    #Test
    print("Consigne: En attente d'un mouvement")
    while True:
        test(fuse,imu)