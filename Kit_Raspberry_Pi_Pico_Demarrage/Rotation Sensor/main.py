from machine import I2C, Pin, Timer
#import time
from time import sleep_ms, sleep_us
from lcd1602_i2c import I2cLcd

DEFAULT_I2C_ADDR = 0x27
    
SW = machine.Pin(3, machine.Pin.IN,machine.Pin.PULL_UP) 
CLK = machine.Pin(6, machine.Pin.IN,machine.Pin.PULL_UP)
DT = machine.Pin(7, machine.Pin.IN,machine.Pin.PULL_UP)    

dis_cnt = 0

def tick(timer):
    global dis_cnt
    dis_cnt += 1

    
if __name__ == "__main__":    
    i2c = I2C(0,scl=Pin(5), sda=Pin(4), freq=100000)
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
    lcd.clear()
    flag = 0
    fh_l = 0
    resetflag = 0
    globalCount = 0    
    fret = 0
    fsetl = 0
    fsetr = 0    
    tim = Timer()
    tim.init(freq=10, mode=Timer.PERIODIC, callback=tick)
    
    while True:
        if fh_l:
            while (CLK.value() == 1 and DT.value() == 0 and fh_l == 1):
                lastSib = 1
                currentSib = 0
                flag =1
            if flag:
                fh_l = 0
                
            while (CLK.value() == 0 and DT.value() == 1 and fh_l == 1):
                lastSib = 0
                currentSib = 1
                flag =1             
            if flag:
                fh_l = 0
                
        else:
            while (CLK.value() == 1 and DT.value() == 0 and fh_l == 0):
                lastSib = 0
                currentSib = 1
                flag =1
            if flag:
                fh_l = 1
                
            while (CLK.value() == 0 and DT.value() == 1 and fh_l == 0):
                lastSib = 1
                currentSib = 0
                flag =1                
            if flag:
                fh_l = 1
                
        while not SW.value():
                resetflag = 1
        
        if resetflag:
                globalCount = 0
                resetflag = 0
                print ('Count reset')
                fret = 1
                dis_cnt = 0
                continue
        if flag:
                if lastSib == 0 and currentSib == 1:
                        print ('right rotate')
                        fsetr = 1
                        globalCount += 1
                if lastSib == 1 and currentSib ==0:
                        print ('left rotate')
                        fsetl = 1
                        globalCount -=1
                flag =0
                dis_cnt = 0
                print ('current = %s' % (globalCount))
                
                while (CLK.value() == 1 and DT.value() == 0):
                    sleep_us(100)
                while (CLK.value() == 0 and DT.value() == 1):
                    sleep_us(100)
                print('fh_l is',fh_l)
                
        if CLK.value() == 0 and DT.value() == 0:
            fh_l = 0
             
        if CLK.value() == 1 and DT.value() == 1:
            fh_l = 1       
                
        if dis_cnt > 3:
                dis_cnt = 0
                if fret:
                    fret = 0
                    lcd.clear()
                    lcd.move_to(1, 0)
                    lcd.putstr("Count reset")
                    lcd.move_to(1, 1)        
                    lcd.putstr("current:")
                    lcd.putstr(str(globalCount))
                if fsetr:
                    fsetr = 0
                    lcd.clear()
                    lcd.move_to(1, 0)
                    lcd.putstr("right rotate")
                    lcd.move_to(1, 1)        
                    lcd.putstr("current:")
                    lcd.putstr(str((globalCount)))
                    
                if fsetl:
                    fsetl = 0
                    lcd.clear()
                    lcd.move_to(1, 0)
                    lcd.putstr("left rotate")
                    lcd.move_to(1, 1)        
                    lcd.putstr("current:")
                    lcd.putstr(str((globalCount)))    