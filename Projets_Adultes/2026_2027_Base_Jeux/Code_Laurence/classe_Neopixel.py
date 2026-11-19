
"""Commande le ruban NeoPixel et fournit un test visuel de ses LEDs."""

from machine import Pin
from neopixel import Neopixel
import time

from constantes import *


class classe_Neopixel:
    def __init__(self):

        self.nombre_leds = 8
        self.strip = Neopixel(self.nombre_leds, 0, PIN_NEOPIXEL, "GRB")
        self.strip.brightness(15)
        
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 150, 0)
        self.GREEN = (0, 255, 0)
        self.CYAN = (0, 255, 255)
        self.BLUE = (0, 0, 255)
        self.PURPLE = (180, 0, 255)
        self.WHITE = (255, 255, 255)
        self.COLORS = (self.BLACK, self.RED, self.YELLOW, self.GREEN, self.CYAN, self.BLUE, self.PURPLE, self.WHITE)
        self.strip.fill(self.RED)

    def colors(self):
        self.strip.set_pixel(0, self.RED)
        self.strip.set_pixel(1, self.GREEN)
        self.strip.set_pixel(2, self.BLUE)
        self.strip.set_pixel(3, self.YELLOW)
        self.strip.set_pixel(4, self.RED)
        self.strip.set_pixel(5, self.GREEN)
        self.strip.set_pixel(6, self.BLUE)
        self.strip.set_pixel(7, self.YELLOW)
        self.strip.show()  

    def off(self):
        self.strip.clear()
        self.strip.show()

    def set_pixel(self, numero, couleur):
        if not 0 <= numero < self.nombre_leds:
            raise IndexError("Numero de LED hors limites : {}".format(numero))
        self.strip.set_pixel(numero, couleur)
        self.strip.show()

    def afficher_couleurs(self, couleurs):
        if len(couleurs) != self.nombre_leds:
            raise ValueError(
                "Il faut fournir une couleur pour chacune des {} LEDs.".format(
                    self.nombre_leds
                )
            )
        self.strip.clear()
        for numero, couleur in enumerate(couleurs):
            self.strip.set_pixel(numero, couleur)
        self.strip.show()

    def all_colors(self):
        for color in self.COLORS:    
            self.strip.fill(color)
            self.strip.show()
            time.sleep(0.5)

    def set_color(self,color):
        self.strip.fill(color)
        self.strip.show()

    def set_color_clignote(self,color,duree,nbre):
        for i in range(nbre):
            self.strip.fill(color)
            self.strip.show()
            time.sleep(duree)
            self.off()
            time.sleep(duree)

    def chase(self):
        raise NotImplementedError

    def rainbow(self):
        raise NotImplementedError

    def auto_test(self, timeout_ms=10000, boutons=None):
        """Lance une sequence visuelle pour controler les 8 Neopixels.

        Le ruban ne fournit pas de retour d'etat : ce test verifie donc que les
        commandes sont envoyees sans erreur. Il faut egalement observer que
        chaque LED s'allume et restitue bien les trois couleurs primaires.
        """
        delai_ms = min(300, max(100, timeout_ms // 32))
        test_reussi = True
        self.interrupted = False

        try:
            print("AUTO TEST Neopixel : defilement blanc, puis rouge / vert / bleu.")

            # Controle de l'ordre et de la presence de chaque LED.
            for numero in range(self.nombre_leds):
                if boutons is not None and boutons.get_status(1):
                    self.interrupted = True
                    print("Auto-test interrompu par le bouton 1.")
                    return False
                self.strip.clear()
                self.strip.set_pixel(numero, self.WHITE)
                self.strip.show()
                time.sleep_ms(delai_ms)

            # Controle des trois composantes de couleur du WS2812.
            for nom, couleur in (("rouge", self.RED),
                                 ("vert", self.GREEN),
                                 ("bleu", self.BLUE)):
                if boutons is not None and boutons.get_status(1):
                    self.interrupted = True
                    print("Auto-test interrompu par le bouton 1.")
                    return False
                print("  {}".format(nom))
                self.strip.fill(couleur)
                self.strip.show()
                time.sleep_ms(delai_ms)

        except Exception as erreur:
            test_reussi = False
            print("Erreur Neopixel : {}".format(erreur))
        finally:
            self.off()

        print("AUTO TEST classe_Neopixel : {}".format("PASSED" if test_reussi else "FAILED"))
        return test_reussi
    
# =================================
# TEST
# =================================
if __name__ == '__main__':
    classe_Neopixel().auto_test()
