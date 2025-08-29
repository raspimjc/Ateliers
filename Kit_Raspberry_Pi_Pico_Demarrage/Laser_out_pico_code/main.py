import machine                                                       #include hardware devices
import utime                                                         #include delay time

led_external = machine.Pin(15, machine.Pin.OUT)                      #define LED pin function:GP15,ouput function
key = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)          #define DOUT pin function:GP14,input and pull up 


while True:                                                       #main loop
    if key.value() == 0:                                          # check  key pin == input low
        led_external.value(1)                                         # LED output high
        utime.sleep(0.2)                                              #delay 0.2sec
    else:                                                          # DOUT pin == input low
        led_external.value(0)                                         # LED output low
    