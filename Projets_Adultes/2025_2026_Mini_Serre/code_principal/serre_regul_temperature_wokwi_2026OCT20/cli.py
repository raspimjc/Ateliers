from shared import event_manager

class Cli:
    def __init__(self):
        # souscrit aux évènements
        event_manager.subscribe(self.__event_callback)

    def __event_callback(self, message):
        if "event" in message:
            print(message)