from machine import Pin, PWM
import time

class Moteur:
    def __init__(self, io_1, io_2, io_pwm, frequency = 5000):
        self.io_1 = io_1
        self.io_2 = io_2
        self.io_pwm = PWM(io_pwm)
        self.io_pwm.freq(frequency)

    def marcheAvant(self,vitesse=100):
        self.io_1.value(1)
        self.io_2.value(0)
        self.io_pwm.duty_u16(int(65536*(vitesse/100)))
        
    def marcheArriere(self,vitesse=100):
        self.io_1.value(0)
        self.io_2.value(1)
        self.io_pwm.duty_u16(int(65536*(vitesse/100)))
        
    def stop(self):
        self.io_1.value(1)
        self.io_2.value(1)
    

if __name__ == '__main__':    
    print('test classe Moteur:')
    
    print('initialisation')
    io_1 =Pin(13 , Pin.OUT)
    io_2 =Pin(12 , Pin.OUT)
    io_pwm =Pin(11 )
    m1 = Moteur(io_1, io_2, io_pwm)

    io_3 =Pin(17 , Pin.OUT)
    io_4 =Pin(16 , Pin.OUT)
    io_pwm2 =Pin(18 )
    m2 = Moteur(io_3, io_4, io_pwm2)
    
    print('le robot avance...')    
    m1.marcheAvant()
    m2.marcheAvant()
    time.sleep(0.2)
    
    print('le robot s arrete...')    
    m1.stop()
    m2.stop()
    time.sleep(1)
    
    
