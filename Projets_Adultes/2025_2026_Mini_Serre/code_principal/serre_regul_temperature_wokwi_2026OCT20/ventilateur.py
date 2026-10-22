from shared import event_manager
from machine import Pin

class Ventilateur:
    def __init__(self, io):
        # instancie l'io du ventilateur
        self.__ventilateur = Pin(io, Pin.OUT)
        # arrête le ventilateur
        self.__ventilateur.value(1)
        # souscrit aux évènements
        event_manager.subscribe(self.__event_callback)

    def __event_callback(self, message):
        if "event" in message:
            if "ventilation" == message["event"]:
                if 0 == message["payload"]:
                    self.__ventilateur.value(0)
                    event_manager.publish({"from":"Ventilateur", "event":"etat_ventilateur", "payload":0})
                else :
                    self.__ventilateur.value(1)
                    event_manager.publish({"from":"Ventilateur", "event":"etat_ventilateur", "payload":100})
