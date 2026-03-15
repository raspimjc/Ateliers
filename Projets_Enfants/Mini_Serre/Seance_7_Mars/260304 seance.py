#L’objectif est de rentrer sur la console de Thonny
#4 messages de max 16 caractères au choix du programmeur,
#puis le programme affiche « prêt » sur l’afficheur lcd
#et suivant l’appui du bouton, on a le message correspondant
#sur l’afficheur.

from machine import I2C, Pin
import time
from quant_debounce_bp import Quant_Debounce_Bp
from lcd1602_i2c import*
# --- Lecture des messages dans la console ---
print("Attention mettre le curseur dans la console avant de taper les messages")
msg1 = input("Message 1 (ligne 1) : ")
msg2 = input("Message 2 (ligne 2) : ")
msg3 = input("Message 3 (ligne 1) : ")
msg4 = input("Message 4 (ligne 2) : ")
# --- LCD ---
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
# --- Boutons ---
bp1 = Quant_Debounce_Bp(16, "bp1")
bp2 = Quant_Debounce_Bp(17, "bp2")
bp3 = Quant_Debounce_Bp(18, "bp3")
bp4 = Quant_Debounce_Bp(19, "bp4")
lcd.clear()
lcd.putstr("Pret...")
# --- Boucle principale ---
while True:
    if bp1.get_state() == "bp1":
        lcd.clear()
        lcd.move_to(0,0)
        lcd.putstr(msg1)
        bp1.bp = None
    if bp2.get_state() == "bp2":
        lcd.clear()
        lcd.move_to(0,1)
        lcd.putstr(msg2)
        bp2.bp = None
    if bp3.get_state() == "bp3":
        lcd.clear()
        lcd.move_to(0,0)
        lcd.putstr(msg3)
        bp3.bp = None
    if bp4.get_state() == "bp4":
        lcd.clear()
        lcd.move_to(0,1)
        lcd.putstr(msg4)
        bp4.bp = None
    time.sleep(0.05)

