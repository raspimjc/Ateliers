import machine                                                       #include hardware devices
import utime                                                         #include delay time

led_external = machine.Pin(25, machine.Pin.OUT)                      #define LED pin function:GP15,ouput function
dout = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)          #define DOUT pin function:GP14,input and pull up 

flag = 0

while True:                                                     #main loop
    if dout.value() == 0:                                          # check  DOUT pin == input low
        if flag:
            print('led warning')
            flag = 0
        led_external.value(0)                                         # LED flash warning
        utime.sleep(0.2)                                              #delay 0.2sec
        led_external.value(1)                                         
        utime.sleep(0.2)     
    else:                                                          # DOUT pin == input high
        led_external.value(0)                                         # LED output low
        if flag == 0:
            print('led off')
            flag = 1