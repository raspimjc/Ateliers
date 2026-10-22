from machine import Timer

# une machine d'état est définie comme suit:
# une liste d'état, chaque état est un dictionnaire de la forme:
# {"etat":"nom_de_l_etat", "entry":fonction_d_entree, "exit":fonction_de_sortie, "events":liste_d_evenement}
# liste_d_evenement : un évenement est un dictionnaire de la forme:
# {"event":"nom_de_l_evenement", "transition":fonction_de_transition, "etat_suivant":"nom_du_nouvel_etat"}


class FsmCore:
    def __init__(self, fsm_def, starting_state):
        # sauvegarde les paramètres
        self.__fsm = fsm_def
        self.__current_state = starting_state
        # définit un timer
        self.__timer = None
        # définit une liste d'event à traiter
        self.__events = list()
        #Timer()
        #self.__tick_timer.init(mode=Timer.PERIODIC, period=3000, callback=self.__tick)

    def process(self, event):
        self.__events.append(event)
        if None == self.__timer:
            self.__timer=Timer()
            self.__timer.init(mode=Timer.ONE_SHOT, period=100, callback=self.__tick)

    def __tick(self, timer):
        if self.__events :
            event = self.__events.pop(0)
            # assume que les paramètres d'entrée sont valide !
            next_state = self.__current_state
            # cherche la définition de l'état
            for state in self.__fsm:
                if state["etat"] == self.__current_state:
                    #print(f"etat trouve {state}")
                    # recherche l'evenement est dans la liste
                    for evt in state["events"]:
                        if evt["event"] == event:
                            # définit le prochain état
                            next_state = evt["etat_suivant"]
                            # appel la fonction de sortie d'état si l'état change
                            if self.__current_state != next_state:
                                print("fsm exit call")
                                if state["exit"]:
                                    state["exit"]()
                            # l'évènement est connu, process it
                            if evt["transition"]:
                                evt["transition"]()
                            # appel la fonction d'entrée dans le nouvel état si l'état change
                            if self.__current_state != next_state:
                                print("fsm entry call")
                                for n_state in self.__fsm:
                                    if n_state["etat"] == next_state:
                                        if n_state["entry"]:
                                            n_state["entry"]()
                                        break
                            break
                    break

            self.__current_state = next_state
            if self.__events :
                self.__timer.init(mode=Timer.ONE_SHOT, period=100, callback=self.__tick)
            else:
                self.__timer.deinit()
                self.__timer = None

