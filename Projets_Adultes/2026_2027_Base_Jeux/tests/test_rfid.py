from mfrc522 import MFRC522 
from utime import sleep

#from constantes import *
RFID_SPI_ID = 1
PIN_RFID_SCK = 10
PIN_RFID_MISO = 8
PIN_RFID_MOSI = 11
PIN_RFID_CS = 9
PIN_RFID_RST = 13

def uidToString(uid):
    mystring = ""
    for i in uid:
        mystring = "%02X" % i + mystring
    return mystring
                  

#print(hex(rc522._rreg(0x37)))

#Test
def test(rc522):
    stat, tag_type = rc522.request(rc522.REQIDL)
    #print("stat =", stat)
    if stat == rc522.OK:
        print("Carte détectée")
        stat, uid = rc522.SelectTagSN()
        #if stat == rc522.OK:
        print(uid)  
        print(stat)
        
#Main    
if __name__ == '__main__':
    #Declaration
    rc522 = MFRC522(spi_id=RFID_SPI_ID,sck=PIN_RFID_SCK,miso=PIN_RFID_MISO,mosi=PIN_RFID_MOSI,cs=PIN_RFID_CS,rst=PIN_RFID_RST)
    #Test
    print("Consigne: Placez une carte RFID pres du lecteur")
    while True:
        test(rc522)
