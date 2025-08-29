
from time import sleep_ms, ticks_ms                                #include delay time
from machine import I2C, Pin                                       #include hardware device
from lcd1602_i2c import I2cLcd                                     #define LCD1602 Function device
from dht11 import DHT11                                            #define DHT11 Function device


# The PCF8574 has a jumper selectable address: 0x20 - 0x27         
DEFAULT_I2C_ADDR = 0x27#0X27#                                      #define I2C Address

dht = DHT11(15)                                                    #define DHT11 pin function:GP15
def readTaHData():
    DATA = dht.read_data()    
    t = DATA[0]                                                    #read Temp.& Humidity
    h = DATA[1]                                                    
    return [str(t),str(h)]                                         

if __name__ == "__main__":    
    i2c = I2C(0,scl=Pin(5), sda=Pin(4), freq=100000)               #define LCD I/O PIN and Freq.
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)                     #define I2C defult address.
    lcd.clear() 
    while True:
        dat = readTaHData()                                        #read Temp.& Humidity     
        sleep_ms(1000)                                             #delay time 1000ms
        lcd.move_to(1, 0)
        lcd.putstr("Temp:")
        lcd.move_to(9, 0)
        lcd.putstr(str(dat[0]))
        lcd.putstr("c")
        lcd.move_to(1, 1)
        lcd.putstr("Humi:")
        lcd.move_to(9, 1)
        lcd.putstr(str(dat[1]))
        lcd.putstr("%")
