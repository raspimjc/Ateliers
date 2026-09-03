from machine import Pin
from buzzer import Buzzer
import time

#from constantes import *
PIN_BUZ = 27

#Variables globales
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
         
notes_short = [("mi",0.25),("mi",0.25),("mi",0.5),
         ("mi",0.25),("mi",0.25),("mi",0.5),
         ("mi",0.25),("so",0.25),("do",0.25),("re",0.25),
         ("mi",1),
         ("fa",0.25),("fa",0.25),("fa",0.5),
         ("mi",0.25),("mi",0.25),("mi",0.5),
         ("re",0.25),("re",0.25),("re",0.25),("mi",0.25)]
         
# fonction qui va jouer 1 note
def joue_note(buz,val_note,duree):
    buz.set_freq(freq_notes[val_note])
    buz.start()
    time.sleep(duree)
    buz.stop()

#Test
def test(buz):
    for note in notes_short:
        joue_note(buz,note[0],note[1])
        time.sleep(0.01) 
    
#Main    
if __name__ == '__main__':
    #Declaration (Alimentation en 3.3V pour celui de la MJC, sinon il se bloque)
    buz = Buzzer(PIN_BUZ)
    #Init
    buz.stop()    
    #Test
    print("Consigne: Musique courte Jingle Bells")
    #Utilisation du try/except pour eteindre le buzzer si on stop le programme
    #Sinon le buzzer s'arrete sur un bip
    try:
        while True:
            test(buz)
    except KeyboardInterrupt as e:
        buz.stop()
  
   
    



