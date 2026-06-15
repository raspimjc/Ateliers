import time
from machine import Pin
from constantes import *

#LED = Pin("LED", Pin.OUT) # LED integree a la board 
#LED = Pin(25, Pin.OUT) # LED integree a la board pour le pico (sauf wifi)
LED = Pin(PIN_LED1, Pin.OUT) # LED 1 Mini Serre
#LED = Pin(PIN_LED2, Pin.OUT) # LED 2 Mini Serre
#LED = Pin(PIN_LED3, Pin.OUT) # LED 3 Mini Serre
#LED = Pin(PIN_LED4, Pin.OUT) # LED 4 Mini Serre

def test_led(led):
    led.toggle()
    time.sleep(0.5)
    

if __name__ == '__main__':
    while True:
        test_led(LED)
