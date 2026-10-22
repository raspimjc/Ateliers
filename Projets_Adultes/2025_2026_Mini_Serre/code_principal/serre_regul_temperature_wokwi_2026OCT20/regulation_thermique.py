from shared import event_manager
from machine import Pin
from fsm_core import FsmCore
from servomoteur import Servo

# une machine d'état est définie comme suit:
# une liste d'état, chaque état est un dictionnaire de la forme:
# {"etat":"nom_de_l_etat", "entry":fonction_d_entree, "exit":fonction_de_sortie, "events":liste_d_evenement}
# liste_d_evenement : un évenement est un dictionnaire de la forme:
# {"event":"nom_de_l_evenement", "transition":fonction_de_transition, "etat_suivant":"nom_du_nouvel_etat"}

class RegulationThermique:
    def __init__(self):
        # servo moteur
        self.__servo = Servo(12)
        # souscrit aux évènements
        event_manager.subscribe(self.__event_callback)
        # variables de régulation
        self.__consigne = 20 # °C
        self.__delta_inférieur = 2 # °C
        self.__delta_superieur = 2 # °C
        # définition de la fsm
        self.__fsm_def = [{"etat":"IDLE", "entry":None, "exit":None, "events":[
                            {"event":"trop_froid", "transition":None, "etat_suivant":"CHAUFFAGE"},
                            {"event":"trop_chaud", "transition":None, "etat_suivant":"OUVERT"}]
                        },
                        {"etat":"CHAUFFAGE", "entry":self.__state_CHAUFFAGE_entry, "exit":self.__state_CHAUFFAGE_exit, "events":[
                            {"event":"trop_chaud", "transition":None, "etat_suivant":"IDLE"}]
                        },
                        {"etat":"OUVERT", "entry":self.__state_OUVERT_entry, "exit":None, "events":[
                            {"event":"encore_trop_froid", "transition":None, "etat_suivant":"IDLE"},
                            {"event":"trop_froid", "transition":self.__state_OUVERT_trop_froid, "etat_suivant":"OUVERT"},
                            {"event":"trop_chaud", "transition":self.__state_OUVERT_trop_chaud, "etat_suivant":"OUVERT"},
                            {"event":"encore_trop_chaud", "transition":None, "etat_suivant":"VENTILATION"}]
                        },
                        {"etat":"VENTILATION", "entry":self.__state_VENTILATION_entry, "exit":self.__state_VENTILATION_exit, "events":[
                            {"event":"trop_froid", "transition":None, "etat_suivant":"OUVERT"}]
                        }
                    ]
        # instancie la fsm
        self.__fsm = FsmCore(self.__fsm_def, "IDLE")

    def __event_callback(self, message):
        #print(f"receive message : {message}")    
        # securité, on s'assure que la clé qui nous intéresse existe dans le message
        if "event" in message:
            if "temperature" == message["event"]:
                new_temperature = message["payload"]
                #print("Température: {:.1f}°C".format(new_temperature))
                #print("Consigne: {:.1f}°C".format(self.__consigne))
                self.__process_temperature(new_temperature)
            elif "servo_maximum" == message["event"]:
                #print("servo_maximum")
                self.__fsm.process("encore_trop_chaud")
            elif "servo_minimum" == message["event"]:
                self.__fsm.process("encore_trop_froid")


    def __process_temperature( self, i_temperature ):
        fsm_event = None
        # hysteresis basique
        # TODO ajouter une moyenne glissante et prendre en compte que tout les x echantillons
        if i_temperature > (self.__consigne+self.__delta_superieur):
            # on doit refroidir
            fsm_event = "trop_chaud"
        elif i_temperature < (self.__consigne-self.__delta_inférieur):
            # on doit chauffer
            fsm_event = "trop_froid"
        
        # si il y a un evenement, appeler la fsm
        if fsm_event:
            # TODO pour ne pas ralentir le programme il faudrait lancer un timer one shot
            #print(f"etat courant {self.__current_state}, evenement {fsm_event}")
            self.__fsm.process(fsm_event)
            #print(f"nouvel etat {self.__current_state}")
    
    def __state_CHAUFFAGE_entry(self):
        # on allume le chauffage
        #print(f"__state_CHAUFFAGE_entry")
        event_manager.publish({"from":"RegulT", "event":"chauffage", "payload":100})

    def __state_CHAUFFAGE_exit(self):
        # on eteint le chauffage
        #print(f"__state_CHAUFFAGE_exit")
        event_manager.publish({"from":"RegulT", "event":"chauffage", "payload":0})

    def __state_OUVERT_entry(self):
        # on ouvre de 30°
        #print(f"__state_OUVERT_entry")
        self.__servo.move(30)

    def __state_OUVERT_trop_chaud(self):
        # on ouvre de 30 de plus
        self.__servo.increment(30)

    def __state_OUVERT_trop_froid(self):
        # on ferme de 30 de moins
        self.__servo.decrement(30)

    def __state_VENTILATION_entry(self):
        # on allume le ventilateur
        #print(f"__state_VENTILATION_entry")
        event_manager.publish({"from":"RegulT", "event":"ventilation", "payload":100})

    def __state_VENTILATION_exit(self):
        # on eteint le ventilateur
        #print(f"__state_VENTILATION_exit")
        event_manager.publish({"from":"RegulT", "event":"ventilation", "payload":0})
