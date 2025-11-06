from machine import Pin, I2C
import time
from ds3231 import DS3231
from constantes import *

# --- Configuration I2C ---
i2c = I2C(I2C_RTC, sda=Pin(PIN_RTC_SDA), scl=Pin(PIN_RTC_SCL), freq=400000)
addr = i2c.scan()[0]
print(hex(addr))

# --- Instanciation de l’horloge ---
rtc = DS3231(i2c)

# --- (Optionnel) fixer l’heure initiale ---
# Par exemple : 2025-10-09, mercredi (=3), 14:30:00
rtc.set_time(2025, 10, 9, 3, 14, 30, 0)

# --- Boucle pour afficher l’heure chaque seconde ---
while True:
    y, m, d, w, h, mi, s = rtc.get_time()
    print("{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(y, m, d, h, mi, s))
    time.sleep(1)
