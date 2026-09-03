from machine import Pin
import time

#from constantes import *
PIN_LED1 = 6

#Test
def test(led):
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)

#Main    
if __name__ == '__main__':
    #Declaration    
    LED = Pin(PIN_LED1, Pin.OUT)
    #Test    
    print("Consigne: La LED va clignoter")
    while True:        
        test(LED)
