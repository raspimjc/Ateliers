from machine import Pin, I2C
import time
import math
import random
from ssd1306 import SSD1306_I2C

i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)


#Dimensions OLED SSD1306
x_oeil_1 = 20
x_oeil_2 = 70
largeur_oeil = 40
y_oeil = 10
hauteur_oeil = 40

CODE_NOIR = 0
CODE_COULEUR = 10

CODE_TAILLE_MIN = 0
CODE_TAILLE_MAX = 10

TICK=1

def displayTick():
    oled.show()
    time.sleep(TICK)
    
#Fonctions qui gèrent un oeil => effacer les lignes non utilisées ?
def oeil(x,taille):
    #Protection
    if taille < CODE_TAILLE_MIN:
        taille = CODE_TAILLE_MIN
    if taille == CODE_TAILLE_MIN:
        for i in range(y_oeil,y_oeil + hauteur_oeil):
            oled.hline(x,i,largeur_oeil,CODE_NOIR)
    else:
        #Protection
        if taille > CODE_TAILLE_MAX:
            taille = CODE_TAILLE_MAX
        debut = y_oeil - taille
        for i in range(y_oeil + debut,y_oeil + hauteur_oeil):
            oled.hline(x,i,largeur_oeil,CODE_COULEUR)

def oeil_biais(x):
    oled.hline(x,13,largeur_oeil-32,CODE_COULEUR)
    oled.hline(x,14,largeur_oeil-24,CODE_COULEUR)
    oled.hline(x,15,largeur_oeil-16,CODE_COULEUR)
    oled.hline(x,16,largeur_oeil-8,CODE_COULEUR)
    for i in range(17,20):
        oled.hline(x,i,largeur_oeil,CODE_COULEUR)

def oeil_biais_2(x):
    oled.hline(x+32,13,largeur_oeil-32,CODE_COULEUR)
    oled.hline(x+24,14,largeur_oeil-24,CODE_COULEUR)
    oled.hline(x+16,15,largeur_oeil-16,CODE_COULEUR)
    oled.hline(x+8,16,largeur_oeil-8,CODE_COULEUR)
    for i in range(17,20):
        oled.hline(x,i,largeur_oeil,CODE_COULEUR)

#Fonctions qui gèrent les yeux
#=============================
def oled_clean():        
    oeil(x_oeil_1,CODE_TAILLE_MIN)
    oeil(x_oeil_2,CODE_TAILLE_MIN)
    oled.show()
    time.sleep(0.05)
    
def yeux_taille(taille):
    oled_clean()
    oeil(x_oeil_1,taille)
    oeil(x_oeil_2,taille)
    displayTick()    

def clin_oeil_droit():
    oled_clean()
    oeil(x_oeil_1,10)
    oeil(x_oeil_2,5)
    displayTick()    

def clin_oeil_gauche():
    oled_clean()
    oeil(x_oeil_1,5)
    oeil(x_oeil_2,10)
    displayTick()    

def colere():
    oled_clean()
    oeil_biais(x_oeil_1)
    oeil_biais_2(x_oeil_2)
    displayTick()

def depite():
    oled_clean()
    oeil_biais(x_oeil_2)
    oeil_biais_2(x_oeil_1)
    displayTick()

while True:
    #Normal
    yeux_taille(10)
    yeux_taille(5)
    yeux_taille(10)
    clin_oeil_droit()
    yeux_taille(10)
    clin_oeil_gauche()
    yeux_taille(10)
    yeux_taille(2)
    yeux_taille(10)
    colere()
    depite()

