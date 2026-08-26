
from machine import Pin, I2C
import time
from time import sleep
from constantes import *

from imu import MPU6050
from fusion import Fusion


#== Declaration du MPU6050
i2c = I2C(I2C_LCD_ID, sda=Pin(PIN_I2C1_SDA), scl=Pin(PIN_I2C1_SCL), freq=10000)
imu = MPU6050(i2c)
fuse = Fusion()


#== Initialisation du MPU6050
date_dernier_selection_mpu6050 = time.ticks_ms()

#==========================================#
# Fonctions                                #
#==========================================#

while True:

    #==== Joueur 2 = MPU6050
    if time.ticks_diff(time.ticks_ms(), date_dernier_selection_mpu6050) > 300: 
        date_dernier_selection_mpu6050 = time.ticks_ms() # "remise a zero"
        fuse.update_nomag(imu.accel.xyz, imu.gyro.xyz)
        '''
        print("Pitch, Roll: {:7.3f} {:7.3f}".format(
            fuse.pitch,
            fuse.roll))
        '''        
        if (fuse.roll > 20):
            print("deplacement_gauche")
        elif (fuse.roll < (-20)):
            print("deplacement_droite")
        elif (fuse.pitch > 20):
            print("deplacement_bas")
        elif (fuse.pitch < (-20)):
            print("deplacement_haut")


