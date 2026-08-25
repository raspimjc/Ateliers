# shared.py

# convention des messages pour le projet:
# utilisation d'un dictionnaire contenant:
# "from": string contenant le nom du module d'origine
# "event" : string contenant un nom d'évènement
# "payload" : forme libre contenant des informations complémentaire pour l'évènement si nécessaire

class EventManager:
    def __init__(self):
        self.__callback_list = list()

    def publish(self, message):
        for cb in self.__callback_list:
            cb(message)

    def subscribe(self, fonction_callback):
        if fonction_callback not in self.__callback_list:
            self.__callback_list.append(fonction_callback)

# Instanciation globale
event_manager = EventManager()