#=====================================================
# Main Exemple Buzzer:
# - Chanson jingle bells version avec le tempo
#=====================================================
from machine import Pin
from buzzer import Buzzer
from time import sleep

tempo = 200

# temps des note
D = 0.25 # double croche
C = 0.5 # croche
N = 1 # noir
N_C = 1.5
B = 2 # blanche
R = 4 # ronde



# frequence note
freq_notes = {"do_2":130.81,"do#_2":138.59,
              "re_2":146.83,"re#_2":155.56,
              "mi_2":164.81,
              "fa_2":174.61,"fa#_2":185.00,
              "sol_2":196,"sol#_2":207.65,
              "la_2":220,"la#_2":233.08,
              "si_2":246.94,
              "do_3":261.63,"do#_3":277.18,
              "re_3":293.66,"re#_3":311.13,
              "mi_3":329.63,
              "fa_3":349.23,"fa#_3":369.99,
              "sol_3":392,"sol#_3":415.30,
              "la_3":440,"la#_3":466.16,
              "si_3":493.88,
              "do_4":523.25,"do#_4":554.37,
              "re_4":587.33,"re#_4":622.25,
              "mi_4":659.26,
              "fa_4":698.46,"fa#_4":739.99,
              "sol_4":783.99,"sol#_4":830.61,
              "la_4":880,"la#_4":932.33,
              "si_4":987.77,
              "do_5":1046.50,"do#_5":1108.73,
              "re_5":1174.66,"re#_5":1244.51,
              "mi_5":1318.51,
              "fa_5":1396.91,"fa#_5":1479.98,
              "sol_5":1567.98,"sol#_5":1661.22,
              "la_5":1760.00,"la#_5":1864.66,
              "si_5":1967.53}

#
buz = Buzzer(2)
buz.stop()

#
def joue_note(val_note,time):
    global buz
    buz.set_freq(freq_notes[val_note])
    buz.start()
    sleep((60/tempo)*time)
    buz.stop()
    
#
jingle = [("mi_3",N), ("mi_3",N), ("mi_3",B),
          ("mi_3",N), ("mi_3",N), ("mi_3",B),
          ("mi_3",N), ("sol_3",N), ("do_3",N), ("re_3",N),
          ("mi_3",R),
          ("fa_3",N), ("fa_3",N), ("fa_3",B),
          ("mi_3",N), ("mi_3",N), ("mi_3",B),
          ("re_3",N), ("re_3",N), ("re_3",N), ("mi_3",N),
          ("re_3",B), ("sol_3",B),
          ("mi_3",N), ("mi_3",N), ("mi_3",B),
          ("mi_3",N), ("mi_3",N), ("mi_3",B),
          ("mi_3",N), ("sol_3",N), ("do_3",N), ("re_3",N),
          ("mi_3",R),          
          ("fa_3",N), ("fa_3",N), ("fa_3",B),
          ("mi_3",N), ("mi_3",N), ("mi_3",B),
          ("sol_3",N), ("fa_3",N), ("mi_3",N), ("re_3",N),
          ("do_3",R)]

tetris = [("re_3",N), ("si_2",C), ("do_3",C), ("re_3",N), ("do_3",C), ("si_2",C),
          ("la_2",N_C), ("do_3",C), ("mi_3",N), ("re_3",C), ("do_3",C),
          ("si_2",N), ("si_2",C), ("do_3",C), ("re_3",N), ("mi_3",N),
          ("do_3",N), ("la_2",N), ("la_2",B), # ligne 1
          ("re_3",N), ("re_3",C), ("fa_3",C), ("la_3",N), ("sol_3",C), ("fa_3",C),
          ("mi_3",N_C), ("do_3",C), ("mi_3",N), ("re_3",C), ("do_3",C),
          ("si_2",N), ("si_2",C), ("do_3",C), ("re_3",N), ("mi_3",N),
          ("do_3",N), ("la_2",N), ("la_2",B), # ligne 2
          ("re_3",N), ("re_3",C), ("fa_3",C), ("la_3",N), ("sol_3",C), ("fa_3",C),
          ("mi_3",N_C), ("do_3",C), ("mi_3",N), ("re_3",C), ("do_3",C),
          ("si_2",N), ("si_2",C), ("do_3",C), ("re_3",N), ("mi_3",N),
          ("do_3",N), ("la_2",N), ("la_2",B), # ligne 3
          ("mi_3",N), ("do_3",N), ("re_3",N), ("si_2",N),
          ("do_3",N), ("la_2",N), ("sol#_2",N), ("si_2",N),
          ("mi_3",N), ("do_3",N), ("re_3",N), ("si_2",N),
          ("do_3",C), ("mi_3",C), ("la_3",C), ("sol#_3",C),("mi_3",B), # ligne 4
          ("mi_3",N), ("do_3",N), ("re_3",N), ("si_2",N),
          ("do_3",N), ("la_2",N), ("sol#_2",N), ("si_2",N),
          ("mi_3",N), ("do_3",N), ("re_3",N), ("si_2",N),
          ("la_3",R)]

#notes = jingle
notes = tetris

for note in notes:
    joue_note(note[0],note[1])
    sleep(0.01)
    

         
         
