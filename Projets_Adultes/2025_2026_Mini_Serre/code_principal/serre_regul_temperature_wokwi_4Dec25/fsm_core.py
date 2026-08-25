

# une machine d'état est définie comme suit:
# une liste d'état, chaque état est un dictionnaire de la forme:
# {"etat":"nom_de_l_etat", "entry":fonction_d_entree, "exit":fonction_de_sortie, "events":liste_d_evenement}
# liste_d_evenement : un évenement est un dictionnaire de la forme:
# {"event":"nom_de_l_evenement", "transition":fonction_de_transition, "etat_suivant":"nom_du_nouvel_etat"}

# moteur de machine d'état pour traiter un évènement sur une machine d'état donnée
# retourne le nouvel état
def fsm_run(fsm_def, current_state, event):
    # print(f"fsm_run etat courant {current_state}, evenement {event}")
    # assume que les paramètres d'entrée sont valide !
    next_state = current_state
    # cherche la définition de l'état
    for state in fsm_def:
        if state["etat"] == current_state:
            #print(f"etat trouve {state}")
            # recherche l'evenement est dans la liste
            for evt in state["events"]:
                if evt["event"] == event:
                    # définit le prochain état
                    next_state = evt["etat_suivant"]
                    # appel la fonction de sortie d'état si l'état change
                    if current_state != next_state:
                        print("fsm exit call")
                        if state["exit"]:
                            state["exit"]()
                    # l'évènement est connu, process it
                    if evt["transition"]:
                        evt["transition"]()
                    # appel la fonction d'entrée dans le nouvel état si l'état change
                    if current_state != next_state:
                        print("fsm entry call")
                        for n_state in fsm_def:
                            if n_state["etat"] == next_state:
                                if n_state["entry"]:
                                    n_state["entry"]()
                                break
                    break
            break

    return next_state