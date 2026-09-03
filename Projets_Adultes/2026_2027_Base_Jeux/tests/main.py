from machine import Pin, ADC, SPI, I2C
import time
from neopixel import Neopixel
from buzzer import Buzzer
from random import random, seed
from ili9341 import Display, color565
from utime import sleep, sleep_us, ticks_cpu, ticks_us, ticks_diff 
from time import sleep
from imu import MPU6050
from fusion import Fusion
from mfrc522 import MFRC522 

import test_led
import test_bouton
import test_neopixel
import test_buzzer
import test_electret
import test_ecran_tft
import test_acc_gyr
import test_rfid

#from constantes import *
PIN_LED1 = 6
PIN_NEOPIXEL = 13
PIN_BP1 = 16
PIN_BUZ = 27
PIN_ELECTRET = 28

TFT_SPI_ID = 0
PIN_TFT_SCK = 2
PIN_TFT_MOSI = 3
PIN_TFT_DC = 1
PIN_TFT_CS = 5
PIN_TFT_RST = 0

ACCGYR_I2C_ID = 1
PIN_ACCGYR_SCL = 15
PIN_ACCGYR_SDA = 14

RFID_SPI_ID = 1
PIN_RFID_SCK = 10
PIN_RFID_MISO = 8
PIN_RFID_MOSI = 11
PIN_RFID_CS = 9
PIN_RFID_RST = 13

#Variables globales
TIMEOUT = 5  # secondes
freq_notes = {"do":1046,"do_":1109,
              "re":1175,"re_":1245,
              "mi":1318,
              "fa":1397,"fa_":1480,
              "so":1568,"so_":1661,
              "la":1760,"la_":1864,
              "si":1967}
notes_short = [("mi",0.25),("mi",0.25),("mi",0.5),
         ("mi",0.25),("mi",0.25),("mi",0.5),
         ("mi",0.25),("so",0.25),("do",0.25),("re",0.25),
         ("mi",1),
         ("fa",0.25),("fa",0.25),("fa",0.5),
         ("mi",0.25),("mi",0.25),("mi",0.5),
         ("re",0.25),("re",0.25),("re",0.25),("mi",0.25)]              
lut = [(52463,3),(45693,2),(35141,1),(30141,0)]
              
#Test LED1
LED = Pin(PIN_LED1, Pin.OUT)
debut = time.ticks_ms()
print("Consigne: La LED va clignoter")
while time.ticks_diff(time.ticks_ms(), debut) < TIMEOUT * 1000:
    test_led.test(LED)
print(">>> TEST LED1 PASSED <<<")
        
#Test BP1
bouton = Pin(PIN_BP1, Pin.IN, Pin.PULL_UP)
bouton.irq(trigger = machine.Pin.IRQ_RISING, handler = test_bouton.bouton_handler)
date_dernier_appui = time.ticks_ms()
bouton_actif = False
debut = time.ticks_ms()
print("Consigne: En attente d'un appui sur le BP")
while time.ticks_diff(time.ticks_ms(), debut) < TIMEOUT * 1000:
    test_bouton.test()
print(">>> TEST BP1 PASSED <<<")

#Test Neopixel
neo = Neopixel(8, 0, PIN_NEOPIXEL, "GRB")
neo.brightness(15)
neo.clear()
neo.show()
debut = time.ticks_ms()
print("Consigne: Le ruban va s'allumer en differentes couleurs")
while time.ticks_diff(time.ticks_ms(), debut) < TIMEOUT * 1000:
    test_neopixel.test(neo)
print(">>> TEST NEOPIXEL PASSED <<<")
    
#Test Buzzer
buz = Buzzer(PIN_BUZ)
buz.stop()
print("Consigne: Musique courte Jingle Bells")
test_buzzer.test(buz)
print(">>> TEST BUZZER PASSED <<<")

#Test Electret
mic = ADC(PIN_ELECTRET)
debut = time.ticks_ms()
print("Consigne: Consigne: En attente d'un son")
while time.ticks_diff(time.ticks_ms(), debut) < TIMEOUT * 1000:
    test_electret.test(mic)
print(">>> TEST ELECTRET PASSED <<<")

#Test Ecran TFT
spi = SPI(TFT_SPI_ID, baudrate=10000000, sck=Pin(PIN_TFT_SCK), mosi=Pin(PIN_TFT_MOSI))
display = Display(spi, dc=Pin(PIN_TFT_DC), cs=Pin(PIN_TFT_CS), rst=Pin(PIN_TFT_RST), width=320, height=240, rotation=0)
debut = time.ticks_ms()
print("Consigne: Consigne: Affichage de cubes en mouvement")
test_ecran_tft.test(display,debut,TIMEOUT)
print(">>> TEST ECRAN TFT PASSED <<<")
display.cleanup()

#Test MPU6050 Acc.Gyr.
date_dernier_appui = time.ticks_ms()
i2c = I2C(ACCGYR_I2C_ID, sda=Pin(PIN_ACCGYR_SDA), scl=Pin(PIN_ACCGYR_SCL), freq=10000)
imu = MPU6050(i2c)
fuse = Fusion()
debut = time.ticks_ms()
print("Consigne: En attente d'un mouvement")
while time.ticks_diff(time.ticks_ms(), debut) < TIMEOUT * 1000:
    test_acc_gyr.test(fuse,imu)
print(">>> TEST ACC GYR PASSED <<<")

#Test RFDID
rc522 = MFRC522(spi_id=RFID_SPI_ID,sck=PIN_RFID_SCK,miso=PIN_RFID_MISO,mosi=PIN_RFID_MOSI,cs=PIN_RFID_CS,rst=PIN_RFID_RST)
debut = time.ticks_ms()
print("Consigne: Placez une carte RFID pres du lecteur")
while time.ticks_diff(time.ticks_ms(), debut) < TIMEOUT * 1000:
    test_rfid.test(rc522)
print(">>> TEST RFID PASSED <<<")
