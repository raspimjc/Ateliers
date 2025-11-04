import time
time.sleep(0.1) # Wait for USB to become ready

from machine import Pin

# bouton
bp = Pin(15, Pin.IN, Pin.PULL_UP)

# initialise l'état du bouton
bp_previous_value = bp.value()

# initialise deux variables de debounce du bouton
bp_previous_time = time.ticks_ms()
bp_debounce_counter = 3

def bp_tick():
    global bp_previous_value
    global bp_previous_time
    global bp_debounce_counter

    # lecture toute les 20 ms
    bp_event = None
    if (time.ticks_ms() - bp_previous_time) > 20:
        l_bp_value = bp.value()
        bp_previous_time = time.ticks_ms()
        if bp_previous_value == l_bp_value:
            if 0 != bp_debounce_counter:
                bp_debounce_counter -= 1
                if 0 == bp_debounce_counter:
                    # on a un état stable
                    if l_bp_value :
                        # c'est un relacher 
                        bp_event = "release"
                    else:
                        bp_event = "press"
        else:
            bp_debounce_counter = 3
        bp_previous_value = l_bp_value
    return bp_event


# led
led = Pin(0, Pin.OUT)

def led_init():
    # éteint la led
    led.value(0)

def led_tick(event):
    if event == "press":
        led.toggle()



def main_simple_fonction():
    print("Simple fonction")

    # initialise
    led_init()

    # boucle principale
    while True:
        # gestion du bouton
        evt = bp_tick()

        # gestion de la led
        led_tick(evt)

##---------------------------
##---------------------------
main_simple_fonction()