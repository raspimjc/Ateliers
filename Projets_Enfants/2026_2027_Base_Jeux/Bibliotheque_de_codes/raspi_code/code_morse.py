from machine import Pin
import time

time.sleep(0.1)  # Attendre que l'USB soit prêt

print("Hello, Pi Pico!")

# LEDS
led_lettre = Pin(6, Pin.OUT)
led_morse = Pin(7, Pin.OUT)

# TIMING MORSE
POINT_TIME = 0.2
TIRET_TIME = 0.6
PAUSE_SYMBOLE = 0.3
PAUSE_LETTRE = 0.7

# CODE MORSE
S = (".", ".", ".")
O = ("-", "-", "-")

# Message : SOS
message = (S, O, S)

# INITIALISATION
led_lettre.value(0)
led_morse.value(0)

print("debut du message")

# ENVOI DU MESSAGE

for lettre in message:

    for symbole in lettre:

        # Allumer la LED Morse
        led_morse.value(1)

        if symbole == "-":
            time.sleep(TIRET_TIME)
        else:
            time.sleep(POINT_TIME)

        # Éteindre la LED Morse
        led_morse.value(0)

        # Pause entre deux symboles
        time.sleep(PAUSE_SYMBOLE)

    # Indiquer le changement de lettre
    led_lettre.toggle()

    # Pause supplémentaire entre deux lettres
    time.sleep(PAUSE_LETTRE)

print("fin du message")