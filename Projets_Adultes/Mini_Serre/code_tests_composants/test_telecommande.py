from machine import Pin
from ir_rx_nec import NEC_16
import time

#Declaration et initialisation de variables internes
data_received = False
IR_data = 0

#Fonctions utiles pour declarer la telecommande 
def callback(data, addr, ctrl):
    global data_received, IR_data
    if (data > 0):
        IR_data = data
        data_received = True
        
ir = NEC_16(Pin(20, Pin.IN), callback)

def test_telecommande():
    global data_received, IR_data
    if data_received:
        print('Data 0x{:02x}'.format(IR_data))
        data_received = False    


if __name__ == '__main__':
    while True:
        test_telecommande()
