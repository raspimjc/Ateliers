from time import sleep_ms, sleep_us                                 #include delay time
from machine import I2C, Pin                                        #include hardware device
from lcd1602_i2c import I2cLcd                                      #define LCD1602 Function device

TRIG_OUT = machine.Pin(14, machine.Pin.OUT)                         #define HC-SR04 pin function
ECHO_INT = Pin(15, Pin.IN, Pin.PULL_UP)                             ##define HC-SR04 pin function INPUT pin

# The PCF8574 has a jumper selectable address: 0x20 - 0x27
DEFAULT_I2C_ADDR = 0x27


def read_Data(self):
    global dat
    if ECHO_INT.value() == 0:
        dat = 0
    else:
        cnt = 0
        while ECHO_INT.value()==1 and cnt < 2000:
            sleep_us(7)
            cnt +=1
            continue
        if cnt >= 2000:
            dat = 0
    
        else:
            dat = int(cnt*30/58)
             

if __name__ == "__main__":    
    i2c = I2C(0,scl=Pin(5), sda=Pin(4), freq=100000)                    #define LCD I/O PIN and Freq.
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)                          #define I2C defult address.
    lcd.clear()
    TRIG_OUT.value(0)
    ECHO_INT.irq(handler=read_Data, trigger=Pin.IRQ_RISING)                     #IO Interrupts
    dat = 0
    while True:
        TRIG_OUT.value(1)
        sleep_us(3)
        TRIG_OUT.value(0)        
        sleep_ms(100)
       
        lcd.move_to(5, 0)
        lcd.putstr("Range:")        
        lcd.move_to(6, 1)       
        lcd.putstr(str(dat))
        lcd.putstr("cm")
        lcd.putstr(" ")
        lcd.putstr(" ")
        