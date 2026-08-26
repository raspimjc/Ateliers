from machine import Pin, PWM
import time

#Buzzer perso
class Buzzer:
    def __init__(self, i_io):
        self._io_pwm = PWM(Pin(i_io, Pin.OUT))
        self.stop()
        self.set_volume(1000)
        
    def start(self):
        self._io_pwm.duty_u16(self._volume)
        
    def stop(self):
        self._io_pwm.duty_u16(0)
        
    def set_volume(self, i_volume):
        self._volume = i_volume
        
    def set_freq(self, i_freq):
        self._io_pwm.freq(int(i_freq))


if __name__ == '__main__':
    print("debut")
    buz = Buzzer(2) 
    buz.set_freq(440)
    buz.start()
    time.sleep(0.2)
    buz.set_freq(1046)
    time.sleep(0.2)
    buz.stop()
    print("fin")
    