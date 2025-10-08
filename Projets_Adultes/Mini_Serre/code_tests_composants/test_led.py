import time
from machine import Pin

#LED = Pin("LED", Pin.OUT) # LED integree a la board 
#LED = Pin(25, Pin.OUT) # LED integree a la board pour le pico (sauf wifi)
LED = Pin(2, Pin.OUT) # LED 1 Mini Serre
#LED = Pin(3, Pin.OUT) # LED 2 Mini Serre
#LED = Pin(4, Pin.OUT) # LED 3 Mini Serre
#LED = Pin(5, Pin.OUT) # LED 4 Mini Serre

def test_led(led):
    led.toggle()
    time.sleep(0.5)
    

if __name__ == '__main__':
    while True:
        test_led(LED)
