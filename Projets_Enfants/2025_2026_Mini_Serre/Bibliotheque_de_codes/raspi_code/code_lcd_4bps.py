from machine import Pin, I2C
from machine_i2c_lcd import I2cLcd
from time import sleep
import time
from quant_debounce_bp import Quant_Debounce_Bp

# --- Declaration de l'ecran LCD ---
i2c = I2C(1, scl=Pin(15), sda=Pin(14), freq=400000)
addr = i2c.scan()[0]
print(hex(addr))
lcd = I2cLcd(i2c, addr, 2, 16)

# --- Lecture des messages dans la console ---
print("Attention mettre le curseur dans la console avant de taper les messages")
msg1 = input("Message 1 (ligne 1) : ")
msg2 = input("Message 2 (ligne 2) : ")
msg3 = input("Message 3 (ligne 1) : ")
msg4 = input("Message 4 (ligne 2) : ")

# --- Boutons ---
bp1 = Quant_Debounce_Bp(0, "bp1")
bp2 = Quant_Debounce_Bp(1, "bp2")
bp3 = Quant_Debounce_Bp(11, "bp3")
bp4 = Quant_Debounce_Bp(10, "bp4")

lcd.clear()
lcd.putstr("Pret...")

# --- Boucle principale ---
while True:
    if bp1.get_state() == "appuyer":
        lcd.clear()
        lcd.move_to(0,0)
        lcd.putstr(msg1)
        bp1.bp = None
    if bp2.get_state() == "appuyer":
        lcd.clear()
        lcd.move_to(0,1)
        lcd.putstr(msg2)
        bp2.bp = None
    if bp3.get_state() == "appuyer":
        lcd.clear()
        lcd.move_to(0,0)
        lcd.putstr(msg3)
        bp3.bp = None
    if bp4.get_state() == "appuyer":
        lcd.clear()
        lcd.move_to(0,1)
        lcd.putstr(msg4)
        bp4.bp = None
    time.sleep(0.05)

