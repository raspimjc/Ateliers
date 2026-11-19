"""Reinitialise les broches GPIO dans un etat neutre au demarrage du Pico."""

from machine import Pin

def reset_pins():
    """
    Met toutes les pins du Pico en entrée flottante (état neutre).
    """
    all_pins = list(range(0, 30))  # GPIO0 à GPIO29
    for pin_num in all_pins:
        try:
            Pin(pin_num, Pin.IN)  # Met la pin en entrée (flottante)
        except Exception:
            pass  # Certaines pins peuvent être réservées ou causer une erreur
                
reset_pins()
