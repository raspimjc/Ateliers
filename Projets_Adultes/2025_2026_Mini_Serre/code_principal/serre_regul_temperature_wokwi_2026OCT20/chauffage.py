from shared import event_manager
from machine import Pin

class Chauffage:
    def __init__(self, io):
        # instancie l'io du ventilateur
        self.__chauffage = Pin(io, Pin.OUT)
        # arrête le ventilateur
        self.__chauffage.value(0)
        # souscrit aux évènements
        event_manager.subscribe(self.__event_callback)

    def __event_callback(self, message):
        if "event" in message:
            if "chauffage" == message["event"]:
                if 0 == message["payload"]:
                    self.__chauffage.value(1)
                    event_manager.publish({"from":"Chauffage", "event":"etat_chauffage", "payload":0})
                else :
                    self.__chauffage.value(0)
                    event_manager.publish({"from":"Chauffage", "event":"etat_chauffage", "payload":100})
