from shared import event_manager
from machine import Pin
from fsm_core import *

# une machine d'état est définie comme suit:
# une liste d'état, chaque état est un dictionnaire de la forme:
# {"etat":"nom_de_l_etat", "entry":fonction_d_entree, "exit":fonction_de_sortie, "events":liste_d_evenement}
# liste_d_evenement : un évenement est un dictionnaire de la forme:
# {"event":"nom_de_l_evenement", "transition":fonction_de_transition, "etat_suivant":"nom_du_nouvel_etat"}

class RegulationThermique:
    def __init__(self):
        # declare les actionneurs
        self.__ventilateur = Pin(7, Pin.OUT)
        self.__chauffage = Pin(6, Pin.OUT)
        # TODO servo moteur
        # éteint les actionneur
        self.__ventilateur.value(0)
        self.__chauffage.value(0)
        # souscrit aux évènements
        event_manager.subscribe(self.__event_callback)
        # variables de régulation
        self.__consigne = 20 # °C
        self.__delta_inférieur = 2 # °C
        self.__delta_superieur = 2 # °C
        # définition de la fsm
        self.__fsm = [{"etat":"IDLE", "entry":None, "exit":None, "events":[
                            {"event":"trop_froid", "transition":None, "etat_suivant":"CHAUFFAGE"},
                            {"event":"trop_chaud", "transition":None, "etat_suivant":"OUVERT"}]
                        },
                        {"etat":"CHAUFFAGE", "entry":None, "exit":None, "events":[
                            {"event":"trop_chaud", "transition":None, "etat_suivant":"IDLE"}]
                        },
                        {"etat":"OUVERT", "entry":None, "exit":None, "events":[
                            {"event":"trop_froid", "transition":None, "etat_suivant":"IDLE"},
                            {"event":"trop_chaud", "transition":None, "etat_suivant":"VENTILATION"}]
                        },
                        {"etat":"VENTILATION", "entry":None, "exit":None, "events":[
                            {"event":"trop_froid", "transition":None, "etat_suivant":"IDLE"}]
                        }
                    ]
        self.__current_state = "IDLE"
        # TODO appeler la fonction d'entrée de l'état de départ

    def __event_callback(self, message):
        #print(f"receive message : {message}")    
        # securité, on s'assure que la clé qui nous intéresse existe dans le message
        if "event" in message:
            if "temperature" == message["event"]:
                new_temperature = message["payload"]
                print("Température: {:.1f}°C".format(new_temperature))
                print("Consigne: {:.1f}°C".format(self.__consigne))
                fsm_event = None
                if new_temperature > (self.__consigne+self.__delta_superieur):
                    # on doit refroidir
                    fsm_event = "trop_chaud"
                elif new_temperature < (self.__consigne-self.__delta_inférieur):
                    # on doit chauffer
                    fsm_event = "trop_froid"
                
                # si il y a un evenement, appeler la fsm
                if fsm_event:
                    # TODO pour ne pas ralentir le programme il faudrait lancer un timer one shot
                    print(f"etat courant {self.__current_state}, evenement {fsm_event}")
                    self.__current_state = fsm_run(self.__fsm, self.__current_state, fsm_event)
                    print(f"nouvel etat {self.__current_state}")
    


        