
"""Gere les huit boutons, leur anti-rebond et le test du bouton 8."""

from machine import Pin
import time

from constantes import *


class classe_Bouton:
    def __init__(self):

        self.boutons = {
            1: {"pin": Pin(PIN_BP1, Pin.IN, Pin.PULL_UP),
                "date": time.ticks_add(time.ticks_ms(), -501),
                "status": False},
            2: {"pin": Pin(PIN_BP2, Pin.IN, Pin.PULL_UP),
                "date": time.ticks_add(time.ticks_ms(), -501),
                "status": False},
            3: {"pin": Pin(PIN_BP3, Pin.IN, Pin.PULL_UP),
                "date": time.ticks_add(time.ticks_ms(), -501),
                "status": False},
            4: {"pin": Pin(PIN_BP4, Pin.IN, Pin.PULL_UP),
                "date": time.ticks_add(time.ticks_ms(), -501),
                "status": False},
            5: {"pin": Pin(PIN_BP5, Pin.IN, Pin.PULL_UP),
                "date": time.ticks_add(time.ticks_ms(), -501),
                "status": False},
            6: {"pin": Pin(PIN_BP6, Pin.IN, Pin.PULL_UP),
                "date": time.ticks_add(time.ticks_ms(), -501),
                "status": False},
            7: {"pin": Pin(PIN_BP7, Pin.IN, Pin.PULL_UP),
                "date": time.ticks_add(time.ticks_ms(), -501),
                "status": False},
            8: {"pin": Pin(PIN_BP8, Pin.IN, Pin.PULL_UP),
                "date": time.ticks_add(time.ticks_ms(), -501),
                "status": False}
        }
        self.interrupted = False

        # Associer chaque bouton au gestionnaire commun
        for numero, bouton in self.boutons.items():
            bouton["pin"].irq(
                trigger=Pin.IRQ_FALLING,
                handler=lambda pin, n=numero: self.bouton_handler(pin, n)
            )

    # Gestion commune des appuis
    def bouton_handler(self, pin, numero):
        maintenant = time.ticks_ms()
        bouton = self.boutons[numero]

        # Anti-rebond de 500 ms
        if time.ticks_diff(maintenant, bouton["date"]) > 500:
            bouton["status"] = True
            bouton["date"] = maintenant

    # Recuperer un appui une seule fois
    def get_status(self, numero):
        bouton = self.boutons[numero]

        if bouton["status"]:
            bouton["status"] = False
            return True

        return False

    def auto_test(self, timeout_ms=10000):
        """Teste le bouton 8 ; le bouton 1 interrompt le test."""
        self.interrupted = False
        for numero in (8,):
            print("Appuyez sur le bouton {} (delai : {} s).".format(numero, timeout_ms // 1000))
            debut = time.ticks_ms()

            while time.ticks_diff(time.ticks_ms(), debut) < timeout_ms:
                if self.get_status(1):
                    self.interrupted = True
                    print("Auto-test interrompu par le bouton 1.")
                    return False
                if self.get_status(numero):
                    print("Bouton {} : OK".format(numero))
                    break
                time.sleep_ms(10)
            else:
                print("Bouton {} : aucun appui detecte.".format(numero))
                return False

        print("AUTO TEST classe_Bouton : PASSED")
        return True
    
# =================================
# TEST
# =================================
if __name__ == '__main__':
    classe_Bouton().auto_test()
