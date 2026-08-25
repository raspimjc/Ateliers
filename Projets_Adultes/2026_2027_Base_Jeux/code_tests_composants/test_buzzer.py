from machine import Pin
from buzzer import Buzzer
from time import sleep
#from constantes import *

# frequences des notes
freq_notes = {"do":1046,"do_":1109,
              "re":1175,"re_":1245,
              "mi":1318,
              "fa":1397,"fa_":1480,
              "so":1568,"so_":1661,
              "la":1760,"la_":1864,
              "si":1967}

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

# declaration du buzzer (Alimentation en 3.3V pour celui de la MJC, sinon il se bloque)
buz = Buzzer(20)
buz.stop()

# fonction qui va jouer une note
def joue_note(val_note,time):
    global buz
    buz.set_freq(freq_notes[val_note])
    buz.start()
    sleep(time)
    buz.stop()

def test_buzzer():
    for note in notes:
        joue_note(note[0],note[1])
        sleep(0.01) 
    

if __name__ == '__main__':
    #Utilisation du try/except pour eteindre le buzzer si on stop le programme
    #Sinon le buzzer s'arrete sur un bip
    try:
        while True:
            test_buzzer()
    except KeyboardInterrupt as e:
        buz.stop()
  
   
    



