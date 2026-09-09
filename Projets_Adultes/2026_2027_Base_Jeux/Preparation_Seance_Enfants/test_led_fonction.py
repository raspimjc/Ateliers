import time
from machine import Pin

LED = Pin(6, Pin.OUT) 

def test_led(led):
    led.toggle()
    time.sleep(0.5)
    
while True:
    test_led(LED)
