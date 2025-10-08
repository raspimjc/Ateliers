from machine import Pin
from time import sleep
import dht

# --- Configuration des périphériques ---
capteur = dht.DHT11(Pin(22))         # capteur sur GPIO 2
led_pins = [Pin(i, Pin.OUT) for i in range(6, 10)]  # LEDs sur GPIO 6 à 9

def eteindre_leds():
    for led in led_pins:
        led.off()

def afficher_barre(nb_leds):
    """Allume nb_leds LEDs en partant de la première"""
    for i in range(4):
        led_pins[i].value(1 if i < nb_leds else 0)

# --- Boucle principale ---
while True:
    try:
        capteur.measure()
        temp = capteur.temperature()
        hum = capteur.humidity()

        print("Température:", temp, "°C  |  Humidité:", hum, "%")

        # Détermine combien de LEDs allumer selon la température
        if temp < 20:
            nb = 1
        elif temp < 25:
            nb = 2
        elif temp < 29:
            nb = 3
        else:
            nb = 4

        afficher_barre(nb)
        sleep(2)

    except OSError as e:
        print("Erreur de lecture du capteur DHT11:", e)
        eteindre_leds()
        sleep(2)
