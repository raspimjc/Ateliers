from machine import Pin
import time

class Moteur:
    def __init__(self, io_1, io_2):
        self.io_1 = io_1
        self.io_2 = io_2
        
    def marcheAvant(self):
        self.io_1.value(0)
        self.io_2.value(1)
        
    def marcheArriere(self):
        self.io_1.value(1)
        self.io_2.value(0)

    def stop(self):
        self.io_1.value(0)
        self.io_2.value(0)
    

if __name__ == '__main__':    
    print('test classe Moteur:')
    
    print('initialisation')
    io_1 =Pin(8 , Pin.OUT)
    io_2 =Pin(9 , Pin.OUT)
    m1 = Moteur(io_1, io_2)
    io_3 =Pin(10 , Pin.OUT)
    io_4 =Pin(11 , Pin.OUT)
    m2 = Moteur(io_3, io_4)
    
    print('le robot avance...')    
    m1.marcheAvant()
    m2.marcheAvant()
    time.sleep(0.2)
    
    print('le robot s arrete...')    
    m1.stop()
    m2.stop()
    time.sleep(1)
    
    
