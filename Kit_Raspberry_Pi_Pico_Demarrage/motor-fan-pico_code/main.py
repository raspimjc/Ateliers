from machine import Pin, PWM                      #include hardware devices
from time import sleep                            #include delay time

pwm = PWM(Pin(15))                                #define motor run pin function:GP15,PWM function

pwm.freq(1000)                                    #define PWM freq.

while True:
    for duty in range(10,65025,100):              #motor run min.-max.
        pwm.duty_u16(duty)                        
        sleep(0.001)              
    for duty in range(65025, 10, -100):           #motor run max.-min.
        pwm.duty_u16(duty)
        sleep(0.001)