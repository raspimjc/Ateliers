from machine import Pin, I2C
from time import sleep
from machine_i2c_lcd import I2cLcd
from rotary_irq_rp2 import RotaryIRQ 
from constantes import *

# === Initialisation des objets ===
i2c = I2C(I2C_LCD, scl=Pin(PIN_LCD_SCL), sda=Pin(PIN_LCD_SDA), freq=400000)
addr = i2c.scan()[0]
#print(hex(addr))
lcd = I2cLcd(i2c, addr, 2, 16)
r = RotaryIRQ(pin_num_clk=PIN_ENC_CLK,pin_num_dt=PIN_ENC_DT,reverse=False,
              incr=1,range_mode=RotaryIRQ.RANGE_UNBOUNDED,
              pull_up=True,half_step=False)
sw = Pin(PIN_ENC_SW, Pin.IN, Pin.PULL_UP)

# === Menu principal ===
menu_items = [
    "Menu 1",
    "Menu 2",
    "Menu 3",
    "Menu 4",
    "Menu 5"
]
index = 0

# === Fonction pLCD ===
def lcd_message(text, line=0):
    """Affiche du texte sur une ligne"""
    lcd.move_to(0, line)
    lcd.putstr(text)

# === Fonction pour afficher le menu ===
def afficher_menu():
    lcd.clear()
    lcd_message("> " + menu_items[index], 0)
    if index + 1 < len(menu_items):
        lcd_message("  " + menu_items[index + 1], 1)

# === Fonctions ===
def execute_mode():
    global index
    if index == 0:
        lcd.clear()
        lcd_message("Dans Menu 1", 0)
        sleep(2)
    elif index == 1:
        lcd.clear()
        lcd_message("Dans Menu 2", 0)
        sleep(2)
    elif index == 2:
        lcd.clear()
        lcd_message("Dans Menu 3", 0)
        sleep(2)
    elif index == 3:
        lcd.clear()
        lcd_message("Dans Menu 4", 0)
        sleep(2)
    elif index == 4:
        lcd.clear()
        lcd_message("Dans Menu 5", 0)
        sleep(2)
    else:
        afficher_menu()
        
    afficher_menu()

# === Démarrage ===
lcd.clear()
lcd_message(" Menu de Noel ", 0)
lcd_message(" MJC Raspi 2025", 1)
sleep(2)
afficher_menu()

# === Boucle principale ===
last_val = r.value()

while True:
    val = r.value()
    if val != last_val:
        index = val
        afficher_menu()
        last_val = val

    if sw.value() == 0:  # Bouton pressé
        execute_mode()
        # Attente relâchement (anti-rebond)
        while sw.value() == 0:
            sleep(0.05)

    sleep(0.05)
