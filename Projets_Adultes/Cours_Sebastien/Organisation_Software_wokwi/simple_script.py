import time
time.sleep(0.1) # Wait for USB to become ready

from machine import Pin

##---------------------------------------------
# la led doit s'allumer tant que le bouton est appuyé
##---------------------------------------------
def simple_script_basic():
    print("Simple script basic")

    led = Pin(0, Pin.OUT)
    bp = Pin(15, Pin.IN, Pin.PULL_UP)

    led.value(0)

    while True:
        if bp.value():
            led.value(0)
        else:
            led.value(1)


##---------------------------------------------
# la led change d'état (allumé/éteint) a chaque appui bouton
##---------------------------------------------
def simple_script_tele():
    print("Simple script tele")

    # déclare la led et le bouton
    led = Pin(0, Pin.OUT)
    bp = Pin(15, Pin.IN, Pin.PULL_UP)

    # éteint la led
    led.value(0)

    # initialise l'état du bouton
    bp_previous_value = bp.value()

    # initilise une variable demandant de changer l'état de la led
    request_led_toggle = False

    while True:
        # gestion du bouton
        if bp_previous_value != bp.value():
            bp_previous_value = bp.value()
            print(f"bp_previous_value {bp_previous_value}")
            if 0 == bp_previous_value:
                # il s'agit d'un appui passage de 1 à 0
                request_led_toggle = True

        # gestion de la led
        if request_led_toggle:
            led.toggle()
            request_led_toggle = False


##---------------------------------------------
# la led change d'état (allumé/éteint) a chaque appui bouton
##---------------------------------------------
def simple_script_tele_debounce():
    print("Simple script tele debounce")

    # déclare la led et le bouton
    led = Pin(0, Pin.OUT)
    bp = Pin(15, Pin.IN, Pin.PULL_UP)

    # éteint la led
    led.value(0)

    # initialise l'état du bouton
    bp_previous_value = bp.value()

    # initilise une variable indiquant une action bouton
    bp_event = None

    # initialise deux variables de debounce du bouton
    bp_previous_time = time.ticks_ms()
    bp_debounce_counter = 3

    while True:
        # gestion du bouton
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


        # gestion de la led
        if bp_event == "press":
            led.toggle()

##---------------------------
##---------------------------
simple_script_tele_debounce()
