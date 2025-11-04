import time
time.sleep(0.1) # Wait for USB to become ready

from machine import Pin


class Bouton:

    def __init__(self, io):
        self.__bp = Pin(io, Pin.IN, Pin.PULL_UP)
        self.__bp_previous_value = self.__bp.value()
        self.__bp_previous_time = time.ticks_ms()
        self.__bp_debounce_counter = 3
        self.__evt_cb = list()

    def tick(self):
        # lecture toute les 20 ms
        bp_event = None
        if (time.ticks_ms() - self.__bp_previous_time) > 20:
            l_bp_value = self.__bp.value()
            self.__bp_previous_time = time.ticks_ms()
            if self.__bp_previous_value == l_bp_value:
                if 0 != self.__bp_debounce_counter:
                    self.__bp_debounce_counter -= 1
                    if 0 == self.__bp_debounce_counter:
                        # on a un état stable
                        if l_bp_value :
                            # c'est un relacher 
                            bp_event = "release"
                        else:
                            bp_event = "press"
            else:
                self.__bp_debounce_counter = 3
            self.__bp_previous_value = l_bp_value
        if bp_event:
            self.__publish(bp_event)

    def subscribe(self, func):
        self.__evt_cb.append(func)

    def __publish(self, evt):
        for cb in self.__evt_cb:
            cb(evt)



class Led:

    def __init__(self, io):
        self.__led = Pin(io, Pin.OUT)
        self.__led.value(0)

    def tick(self):
        pass

    def evt_cb(self, event):
        if event == "press":
            self.__led.toggle()





def main_pub_sub_class():
    print("Pub sub class")

    # initialise
    led_violet = Led(0)
    mon_bp = Bouton(15)
    mon_bp1 = Bouton(16)

    mon_bp.subscribe(led_violet.evt_cb)
    mon_bp1.subscribe(led_violet.evt_cb)

    # boucle principale
    while True:
        # gestion du bouton
        mon_bp.tick()
        mon_bp1.tick()

        # gestion de la led
        led_violet.tick()

##---------------------------
##---------------------------
main_pub_sub_class()