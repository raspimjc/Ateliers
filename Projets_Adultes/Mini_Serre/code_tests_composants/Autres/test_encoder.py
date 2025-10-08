from machine import Pin, PWM
from rotary_irq_rp2 import RotaryIRQ
import time

#Declaration de l'encoder
ENCODER = RotaryIRQ(pin_num_clk=28,pin_num_dt=27,reverse=False,
              incr=1,range_mode=RotaryIRQ.RANGE_UNBOUNDED,
              pull_up=True,half_step=False)


val_old = ENCODER.value()

def test_encoder(enc):
    global val_old
    val_new = enc.value()
    if val_old != val_new:
        print("valeur =", val_new)
        val_old = val_new     
    time.sleep_ms(50)    


if __name__ == '__main__':
    while True:       
        test_encoder(ENCODER)

