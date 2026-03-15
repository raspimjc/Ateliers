# Simulation serre, affichage température et humidité, lecture des BP 
# ce verif fonctionnement des leds, BP et capteur affichage lors de la connexion de l'USB:



from neopixel import Neopixel
from machine import Pin #importation des classes et modules que l'on a besoin
import time
from machine import I2C                                      
from lcd1602_i2c import I2cLcd                                     
import dht
from bouton_mach_etat import Bouton_Mach_Etat
# initialisation de l'afficheur
# The PCF8574 has a jumper selectable address: 0x20 - 0x27         
DEFAULT_I2C_ADDR = 0x27                                      #define I2C Address
i2c = I2C(0,scl=Pin(5), sda=Pin(4), freq=100000)               #define LCD I/O PIN and Freq.
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)                     #define I2C default address.
lcd.clear() #efface l'afficheur

capteur = dht.DHT22(Pin(2)) # initialisation du capteur

# Initialisation des leds en sortie
Led_1= Pin(15,Pin.OUT)  # led rouge 
Led_2= Pin(14,Pin.OUT)  # led verte 
Led_3= Pin(13,Pin.OUT)	# led blue
Led_4= Pin(12,Pin.OUT)	# led jaune
# extinction des leds
Led_1.value(1)
Led_2.value(1)
Led_3.value(1)
Led_4.value(1)

bp1 = Bouton_Mach_Etat(16,"bp1")
bp2 = Bouton_Mach_Etat(17,"bp2")
bp3 = Bouton_Mach_Etat(18,"bp3")
bp4 = Bouton_Mach_Etat(19,"bp4")


leds = Neopixel(8,0,20,"GRB")
leds.brightness(10)




def affichage():     # cette fonction permet de faire l'affichage des textes et valeurs
                    # on dit où doit se positionner le curseur, puis on donne le texte ou les valeurs mesurées
    
    lcd.move_to(0, 0)  # affiche sur ligne 0 à partir du caractère 0 (jusquà 16)
    lcd.putstr("Temp:") # le texte comporte 6 caractères
    lcd.move_to(7, 0) # donc on affiche à partir du 7ieme de la ligne 0
    lcd.putstr(str(Temp)) #comme ce sont des caractères que l'on va afficher,
    lcd.move_to(11, 0)                     # il faut mettre str devant la valeur mesurée
    lcd.putstr(" "+chr(0xDF) + "C")  # pour afficher le caractère "°", il faut chr(0xDF)
    # idem ligne 1
    lcd.move_to(0, 1)  
    lcd.putstr("Humi:")
    lcd.move_to(7, 1)
    lcd.putstr(str(Hum))
    lcd.putstr(" %")
       
   
time.sleep(1)     # le DHT22 renvoie au maximum une mesure toute les 1s
capteur.measure()     # Recuperère les mesures du capteur
Temp =capteur.temperature()
Hum =capteur.humidity()
Hum=round(Hum,1)
affichage()
print(f"Temperature : {Temp:.1f}°C")
print(f"Humidite    : {Hum:.1f}%")

while True:
    Led_1.value(0)
    Led_2.value(0)
    Led_3.value(0)
    Led_4.value(0)
    time.sleep (1)
    Led_1.value(1)
    Led_2.value(1)
    Led_3.value(1)
    Led_4.value(1)
    time.sleep (1)
    leds.fill((110,50,100))
    leds.show()
    time.sleep(3)
    leds.clear()
    leds.show()
    time.sleep(1)
    leds.fill((110,50,10))
    leds.show()
    time.sleep(3)
    leds.clear()
    leds.show()
    pass
    
   
    






  
    
    
   


    
      
       


