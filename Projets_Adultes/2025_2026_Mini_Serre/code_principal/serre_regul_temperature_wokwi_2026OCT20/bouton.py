from machine import Pin, Timer
from shared import event_manager




class Bouton:
    def __init__(self, io, nom):
        # instancie la pin
        self.__pin = Pin(io, Pin.IN, Pin.PULL_UP)
        # sauvegarde le nom du bouton
        self.__name = nom
        # démarre un timer périodique
        self.__tick_timer = Timer()
        self.__tick_timer.init(mode=Timer.PERIODIC, period=20, callback=self.__tick)
        # lit l'état actuel
        self.__old_state = self.__pin.value()

    def __tick(self, timer):
        # lire l'etat du bouton
        c_state = self.__pin.value()
        if c_state != self.__old_state:
            # changement d'état
            self.__old_state = c_state
            if 0 == c_state:
                event_manager.publish({"from":"bouton", "event":f"{self.__name}_PRESS", "payload":None})
            else:
                event_manager.publish({"from":"bouton", "event":f"{self.__name}_RELEASE", "payload":None})
