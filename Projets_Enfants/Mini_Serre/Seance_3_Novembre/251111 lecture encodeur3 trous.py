from machine import Pin
from rotary_irq_rp2 import RotaryIRQ # importation de RotaryIRQ qui est dans le fichier rotary_irq_rp2.py
import time
# initialisation des leds
LED0=Pin(0, Pin.OUT)
LED0.value(0)
LED1=Pin(x, xxx)
LED1.value(x)
LED2=Pin(x, xxx)
LED2.value(x)
LED3=Pin(x, xxxx)
LED3.value(x)
LED=[LED0,LED1,xxx,xxx] #creation de la liste des leds

#Declaration de l'encoder
ENCODER = RotaryIRQ(pin_num_clk=x,pin_num_dt=x,reverse=False,
              incr=1,range_mode=RotaryIRQ.RANGE_UNBOUNDED,
              pull_up=True,half_step=False)

val_old = ENCODER.value() # initialisation de la variable val_old avec la valeur qu'il y a
                         #dans ENCODER.value()
 
def lecture_encoder(enc): # la fonction lecture de l'encodeur
    global val_old
    val_new = enc.value()
    if val_old != val_new:  #si la valeur ancienne de l'encodeur est différente de celle qui
                            #est actuellement, on incremente ou decremente un compteur     
        for led in LED:   # on met toutes les leds à 0 donc éteintes         
            led.value(0)
        I= val_new % 4    # on calcule le reste de la division du compteur par 4 puis qu'il y a 4 leds
        led=LED[I] #on va chercher la led dans la liste qui correpond au reste de la division
        led.value(1) #on met cette led à 1   
        print("valeur =", val_new, I)
        val_old = val_new  # on reinitialise val_old avec la valeur actuelle pour pouvoir détecter
                            #un nouveau changement    
    time.sleep_ms(50)    


if __name__ == '__main__':
    while True:       
        lecture_encoder(ENCODER)
