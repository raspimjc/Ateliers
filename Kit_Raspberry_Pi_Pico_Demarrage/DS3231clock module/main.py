from machine import I2C, Pin, Timer
import time
from ds3231 import DS3231
from lcd1602_i2c import I2cLcd

DEFAULT_I2C_ADDR = 0x27
key1 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)          
key2 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)



def tick(timer):      
    global sys_50ms_cnt
    global flash_flag
    sys_50ms_cnt +=1
    if sys_50ms_cnt >=10:
        sys_50ms_cnt =0
        flash_flag ^= 1
    
    global mode_ptr
    global set_flag
    global key1_cnt
    global key2_cnt
    global key1_press
    global key2_press
    global key_inc_flag
    
    if key1.value()== 0:
        key1_cnt +=1
        if key1_cnt>2 and key1_press==0:
            key1_cnt = 0
            key1_press = 1
            mode_ptr +=1
            set_flag = 1
            if mode_ptr>6:
                mode_ptr = 0                
                
    else:
        key1_cnt = 0    
        key1_press = 0
        
        
        
    if key2.value()== 0:
        key2_cnt +=1
        if key2_cnt>1 and key2_press==0:
            key2_cnt = 0
            key2_press = 1
            key_inc_flag = 1           
    else:
        key2_cnt = 0    
        key2_press = 0    
        
        
        
if __name__ == "__main__":    
    i2c = I2C(0,scl=Pin(5), sda=Pin(4), freq=100000)
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
    lcd.clear()
    
    tim = Timer()
    tim.init(freq=20, mode=Timer.PERIODIC, callback=tick)
    mode_ptr = 0
    set_flag = 0 
    sys_50ms_cnt = 0
    flash_flag = 0
    key1_cnt=0
    key2_cnt=0
    key1_press = 0
    key2_press = 0
    key_inc_flag = 0
    
    ds=DS3231()
    #ds.DATE([21,4,22])
    #ds.TIME([16,14,50])
    while True:
        print('Date:',ds.DATE())
        print('Time:',ds.TIME())
        
        if set_flag:
            if mode_ptr == 1 :
                if key_inc_flag:
                    key_inc_flag = 0
                    date[0] += 1
                    if date[0] >99 :
                        date[0] = 0
                
                if flash_flag:
                    lcd.move_to(8, 0)
                    lcd.putchar(" ")
                    lcd.putchar(" ")
                else:
                    lcd.move_to(8, 0)
                    if date[0] < 10 :
                        lcd.putchar("0")
                    lcd.putstr(str(date[0]))
            
            if mode_ptr == 2 :
                if key_inc_flag:
                    key_inc_flag = 0
                    date[1] += 1
                    if date[1] >12 :
                        date[1] = 1
                
                if flash_flag:
                    lcd.move_to(11, 0)
                    lcd.putchar(" ")
                    lcd.putchar(" ")
                else:
                    lcd.move_to(11, 0) 
                    if date[1] < 10 :
                        lcd.putchar("0")
                    lcd.putstr(str(date[1]))
            
            if mode_ptr == 3 :
                if key_inc_flag:
                    key_inc_flag = 0
                    date[2] += 1
                    if date[2] >31 :
                        date[2] = 1
                
                if flash_flag:
                    lcd.move_to(14, 0)
                    lcd.putchar(" ")
                    lcd.putchar(" ")
                else:
                    lcd.move_to(14, 0) 
                    if date[2] < 10 :
                        lcd.putchar("0")
                    lcd.putstr(str(date[2]))
            
            if mode_ptr == 4 :
                if key_inc_flag:
                    key_inc_flag = 0
                    times[0] += 1
                    if times[0] >23 :
                        times[0] = 0
                
                if flash_flag:
                    lcd.move_to(6, 1)
                    lcd.putchar(" ")
                    lcd.putchar(" ")
                else:
                    lcd.move_to(6, 1)
                    if times[0] < 10 :
                        lcd.putchar("0")
                    lcd.putstr(str(times[0]))           
            
            
            if mode_ptr == 5 :
                if key_inc_flag:
                    key_inc_flag = 0
                    times[1] += 1
                    if times[1] >59 :
                        times[1] = 0
                
                if flash_flag:
                    lcd.move_to(9, 1)
                    lcd.putchar(" ")
                    lcd.putchar(" ")
                else:
                    lcd.move_to(9, 1)
                    if times[1] < 10 :
                        lcd.putchar("0")
                    lcd.putstr(str(times[1])) 
            
            if mode_ptr == 6 :
                mode_ptr = 0
                set_flag = 0
                times[2] = 0
                ds.DATE(date)
                ds.TIME(times)
            
        else:
            date = ds.DATE()
            times = ds.TIME()
            
        
        lcd.move_to(0, 0)
        lcd.putstr("Date: 20")
        if mode_ptr != 1 :   
            lcd.move_to(8, 0)
            if date[0] < 10 :
                lcd.putchar("0")
            lcd.putstr(str(date[0]))
            
        lcd.move_to(10, 0)
        lcd.putchar("-")
            
        if mode_ptr != 2 :
            lcd.move_to(11, 0) 
            if date[1] < 10 :
                lcd.putchar("0")
            lcd.putstr(str(date[1]))
         
        lcd.move_to(13, 0)
        lcd.putchar("-")
         
        if mode_ptr != 3 :
            lcd.move_to(14, 0) 
            if date[2] < 10 :
                lcd.putchar("0")
            lcd.putstr(str(date[2]))
        
         
        lcd.move_to(0, 1)        
        lcd.putstr("Time: ")
        
        if mode_ptr != 4 :    
            lcd.move_to(6, 1)
            if times[0] < 10 :
                lcd.putchar("0")
            lcd.putstr(str(times[0]))
        
        lcd.move_to(8, 1)
        lcd.putchar(":")
            
        if mode_ptr != 5 :
            lcd.move_to(9, 1)
            if times[1] < 10 :
                lcd.putchar("0")
            lcd.putstr(str(times[1]))
        
        lcd.move_to(11, 1)
        lcd.putchar(":")
        if times[2] < 10 :
            lcd.putchar("0")
        lcd.putstr(str(times[2]))
       
        time.sleep(0.1)  
