import machine                                                       #include hardware devices
import utime                                                         #include delay time

led_external = machine.Pin(15, machine.Pin.OUT)                      #define LED pin function:GP15,ouput function
aout = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)          #define AOUT pin function:GP14,input and pull up 

flag = 0

while True:                                                     #main loop
    if aout.value() == 1:                                          # check  AOUT pin == input high
        led_external.value(1)                                         # LED output high
        if flag:
            print('led on')
            flag = 0
        utime.sleep(0.2)                                              #delay 0.2sec
    else:                                                          # AOUT pin == input low
        led_external.value(0)                                         # LED output low
        if flag == 0:
            print('led off')
            flag = 1