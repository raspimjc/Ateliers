#Source
#https://stm32python.gitlab.io/fr/docs/Micropython/grove/rfid ** A REGARDER **
#https://electroniqueamateur.blogspot.com/2021/05/lecture-dun-tag-rfid-avec-module-rc522.html

'''
Lecture du numéro (UID) d'un tag RFID.
Module RFID-RC522 et Raspberry Pi Pico

Plus d'infos:
https://electroniqueamateur.blogspot.com/2021/05/lecture-dun-tag-rfid-avec-module-rc522.html

'''
from mfrc522 import MFRC522 # https://github.com/danjperron/micropython-mfrc522
from utime import sleep

def uidToString(uid):
    mystring = ""
    for i in uid:
        mystring = "%02X" % i + mystring
    return mystring
                  
#rc522 = MFRC522(spi_id=0,sck=6,miso=4,mosi=7,cs=5,rst=3)
rc522 = MFRC522(spi_id=1,sck=10,miso=8,mosi=11,cs=9,rst=0)

print("")
print("Placez une carte RFID pres du lecteur.")
print("")

while True:

    (stat, tag_type) = rc522.request(rc522.REQIDL)

    if stat == rc522.OK:
        (stat, uid) = rc522.SelectTagSN()
        
    if stat == rc522.OK:
        print("Carte detectee %s" % uidToString(uid))
        sleep(1) # delai pour éviter les lectures multiples
        