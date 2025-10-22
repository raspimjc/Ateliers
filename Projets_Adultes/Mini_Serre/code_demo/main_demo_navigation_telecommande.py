from machine import Pin, I2C
from time import sleep
from machine_i2c_lcd import I2cLcd
from ir_rx_nec import NEC_16
from constantes_laurence import *

# === Initialisation des objets ===
i2c = I2C(I2C_LCD, scl=Pin(PIN_LCD_SCL), sda=Pin(PIN_LCD_SDA), freq=400000)
addr = i2c.scan()[0]
#print(hex(addr))
lcd = I2cLcd(i2c, addr, 2, 16)


# === Definitions ===
Touche_0 = 0x19
Touche_1 = 0x45
Touche_2 = 0x46
Touche_3 = 0x47
Touche_4 = 0x44
Touche_5 = 0x40
Touche_6 = 0x43
Touche_7 = 0x07
Touche_8 = 0x15
Touche_9 = 0x09
Touche_H = 0x18
Touche_D = 0x5A
Touche_B = 0x52
Touche_G = 0x08
Touhe_OK = 0x1C

# === Menu principal ===
# === Menu principal ===
menu_items = [
    "Menu 1",
    "Menu 2",
    "Menu 3",
    "Menu 4",
    "Menu 5"
]
index = 0
mode = None

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
        

# === Fonction de callback télécommande ===
def on_ir_command(code, addr, ext):
    #print("Code reçu:", hex(code))
    global index, mode

    if code == Touche_H:
        index = (index - 1) % len(menu_items)
        afficher_menu()

    elif code == Touche_B:
        index = (index + 1) % len(menu_items)
        afficher_menu()

    elif code == Touhe_OK:
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
            
        afficher_menu()

    elif code == Touche_G:
        lcd.clear()
        lcd_message("Retour menu...", 0)
        sleep(1)
        afficher_menu()
        
# === Démarrage télécommande ===
remote = NEC_16(Pin(PIN_IR, Pin.IN), on_ir_command)

# === Démarrage ===
lcd.clear()
lcd_message(" Menu de Noel ", 0)
lcd_message(" MJC Raspi 2025", 1)
sleep(2)
afficher_menu()

# === Boucle principale ===
while True:
    sleep(1)