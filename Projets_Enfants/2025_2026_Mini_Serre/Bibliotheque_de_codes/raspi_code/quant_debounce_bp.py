import machine
from machine import Pin, Timer

debounce_time = 80

class BtnState:
    RELEASED = 0
    PRESSED  = 1
    DEBOUNCE = 2

class Quant_Debounce_Bp:
  
    def __init__(self, pin_no, name):
        self.name = name
        self.pin = Pin(pin_no, Pin.IN, Pin.PULL_UP)
        self.state = BtnState.RELEASED
        self.timer = Timer(-1)
        self.bp = "relacher"

        self.pin.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING,
                     handler=self._irq_handler)

    def _irq_handler(self, pin):
        if self.state != BtnState.DEBOUNCE:
            self.state = BtnState.DEBOUNCE
            self.timer.init(mode=Timer.ONE_SHOT,
                            period=debounce_time,
                            callback=self._debounce_done)

    def _debounce_done(self, t):
        level = self.pin.value()
        if level == 0:
            self.state = BtnState.PRESSED
            self._on_pressed()
        else:
            self.state = BtnState.RELEASED
            self._on_released()

    def _on_pressed(self):
        self.bp = "appuyer"

    def _on_released(self):
        self.bp = "relacher"
        pass

    def get_state(self):
        return self.bp
