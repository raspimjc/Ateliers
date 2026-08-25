from machine import Pin
import time
import utime

class Ultrason:

    def __init__(self, trigger_pin, echo_pin):
        '''
        trigger_pin: Output pin to send pulses
        echo_pin: Readonly pin to measure the distance
        '''
        # Init trigger pin (out)
        self.trigger = Pin(trigger_pin, mode=Pin.OUT, pull=None)
        self.trigger.value(0)
        # Init echo pin (in)
        self.echo = Pin(echo_pin, mode=Pin.IN, pull=None)     
        
    def dist(self):
        self.trigger.value(1)
        utime.sleep_ms(10)
        self.trigger.value(0)
        while(self.echo.value() == 0):
            pass
        ts=utime.ticks_us()
        while(self.echo.value() == 1):
            pass
        te=utime.ticks_us()
        distance=((te-ts)*0.034)/2
        return distance   
        
    def distance_cm(self):
        """
        Get the distance in centimeters with floating point operations.
        It returns a float
        """
        cms = self.dist()
        return cms
        
    def distance_mm(self):
        """
        Get the distance in milimeters without floating point operations.
        """
        mm = self.dist()*10
        return mm

if __name__ == '__main__':
    print('test classe Ultrason')
    sensor = Ultrason(trigger_pin=14, echo_pin=15)
    
    while True:
        distance = sensor.distance_cm()
        print('Distance:', "{0:2.2f}".format(distance), 'cm')
        time.sleep(1)