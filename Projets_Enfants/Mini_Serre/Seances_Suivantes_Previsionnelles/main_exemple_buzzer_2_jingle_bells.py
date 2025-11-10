#=====================================================
# Main Exemple Buzzer:
# - Chanson jingle bells version simple
#=====================================================
from machine import Pin
from buzzer import Buzzer
from time import sleep

# frequences des notes
freq_notes = {"do":1046,"do_":1109,
              "re":1175,"re_":1245,
              "mi":1318,
              "fa":1397,"fa_":1480,
              "so":1568,"so_":1661,
              "la":1760,"la_":1864,
              "si":1967}


# declaration du buzzer (Pin2, alimentation en 3.3V pour celui de la MJC)
buz = Buzzer(2)
buz.stop()

# fonction qui va jouer une note
def joue_note(val_note,time):
    global buz
    buz.set_freq(freq_notes[val_note])
    buz.start()
    sleep(time)
    buz.stop()

#Jingle Bells
notes = [("mi",0.25),("mi",0.25),("mi",0.5),
         ("mi",0.25),("mi",0.25),("mi",0.5),
         ("mi",0.25),("so",0.25),("do",0.25),("re",0.25),
         ("mi",1),
         ("fa",0.25),("fa",0.25),("fa",0.5),
         ("mi",0.25),("mi",0.25),("mi",0.5),
         ("re",0.25),("re",0.25),("re",0.25),("mi",0.25),
         ("re",0.5),("so",0.5),
         ("mi",0.25),("mi",0.25),("mi",0.5),
         ("mi",0.25),("mi",0.25),("mi",0.5),
         ("mi",0.25),("so",0.25),("do",0.25),("re",0.25),
         ("mi",1),
         ("fa",0.25),("fa",0.25),("fa",0.5),
         ("mi",0.25),("mi",0.25),("mi",0.5),
         ("so",0.25),("fa",0.25),("mi",0.25),("re",0.25),
         ("do",1)]

while True:
    for note in notes:
        joue_note(note[0],note[1])
        sleep(0.01) 

  
   
    



