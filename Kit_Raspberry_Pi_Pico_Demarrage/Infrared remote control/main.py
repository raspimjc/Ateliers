from time import sleep_ms, sleep_us
from machine import I2C, Pin
from lcd1602_i2c import I2cLcd


IR_INT = Pin(15, Pin.IN, Pin.PULL_UP)             #INPUT pin

# The PCF8574 has a jumper selectable address: 0x20 - 0x27
DEFAULT_I2C_ADDR = 0x27


def read_Data(self):
    global dat
    global code_dis_flag
    if IR_INT.value() == 1:
        print('IRf')
    else:
        cnt = 0
        while IR_INT.value()==0 and cnt < 400:
            sleep_us(7)
            cnt +=1
            continue
        if cnt >= 400 or cnt < 230:
            print('SHf')
    
        else:
            if IR_INT.value()==1:
                cnt = 0
                while IR_INT.value()==1 and cnt < 215:
                    sleep_us(7)
                    cnt +=1
                    continue
                if cnt >= 215 or cnt < 100:
                    print('SLf')
            
                else:
                    data=[]
                    j=0
                    while j<32:
                        cnt = 0    
                        while IR_INT.value()==0 and cnt < 30:
                            sleep_us(7)
                            cnt +=1
                            continue
                        if cnt >= 30 or cnt < 10:
                            print('CL_bit',j)
                        else:
                            cnt = 0 
                            while IR_INT.value()==1 and cnt < 70:
                                sleep_us(7)
                                cnt +=1
                                continue
                            if cnt >= 70 or cnt < 10:
                                print('CH_bit',j)
                            else:
                                if cnt > 35:
                                    data.append(1)
                                else:
                                    data.append(0)
                        j+=1            
                    
                    code3 = data[16:24]
                    code4 = data[24:32]
                    code3_buf = 0
                    code4_buf = 0
                    for i in range(8):
                        code3_buf+=code3[i]*2**(7-i)
                        code4_buf+=code4[i]*2**(7-i)
                    if code3_buf+code4_buf == 255:
                        dat = code3_buf
                        print('IR code:',dat)                       
                        code_dis_flag = 1

if __name__ == "__main__":    
    i2c = I2C(0,scl=Pin(5), sda=Pin(4), freq=100000)
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
    lcd.clear()   
    IR_INT.irq(handler=read_Data, trigger=Pin.IRQ_FALLING)                     #IO Interrupts
    dat = 0
    code_dis_flag = 0
    while True:
        if code_dis_flag:
            code_dis_flag = 0
            lcd.clear()
            lcd.move_to(5, 0)
            lcd.putstr("IR code:")
            
            if dat == 162:            
                lcd.move_to(6, 1)       
                lcd.putstr("1")
        
            elif dat == 98:            
                lcd.move_to(6, 1)       
                lcd.putstr("2")
            
            elif dat == 226:
                lcd.move_to(6, 1)       
                lcd.putstr("3")
            
            elif dat == 34:
                lcd.move_to(6, 1)       
                lcd.putstr("4")    
            
            elif dat == 2:             
                lcd.move_to(6, 1)       
                lcd.putstr("5")    
            
            elif dat == 194:             
                lcd.move_to(6, 1)       
                lcd.putstr("6")    
            
            elif dat == 224:             
                lcd.move_to(6, 1)       
                lcd.putstr("7")
            
            elif dat == 168:             
                lcd.move_to(6, 1)       
                lcd.putstr("8")    
            
            elif dat == 144:             
                lcd.move_to(6, 1)       
                lcd.putstr("9")   
            
            elif dat == 152:             
                lcd.move_to(6, 1)       
                lcd.putstr("0")
            
            elif dat == 104:             
                lcd.move_to(6, 1)       
                lcd.putstr("*")
            
            elif dat == 176:             
                lcd.move_to(6, 1)       
                lcd.putstr("#")    
            
            elif dat == 24:             
                lcd.move_to(6, 1)       
                lcd.putstr("up")
            
            elif dat == 74:             
                lcd.move_to(6, 1)       
                lcd.putstr("down")
            
            elif dat == 16:
                lcd.move_to(6, 1)       
                lcd.putstr("left")    
            
            elif dat == 90:
                lcd.move_to(6, 1)       
                lcd.putstr("right")    
        
            elif dat == 56:            
                lcd.move_to(6, 1)       
                lcd.putstr("OK")