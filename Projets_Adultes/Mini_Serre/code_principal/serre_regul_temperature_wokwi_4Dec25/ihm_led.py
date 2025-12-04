from machine import Pin, Timer

class IhmLed:
    def __init__(self, io):
        # instancie une broche
        self.__led = Pin(io, Pin.OUT)
        # éteint la led
        self.__led.value(0)
        # démarre un timer périodique pour la led de vie
        self.__tick_timer = Timer()
        self.__tick_timer.init(mode=Timer.PERIODIC, period=1000, callback=self.__tick)

    def __tick(self, timer):
        # clignotement de vie
        self.__led.toggle()