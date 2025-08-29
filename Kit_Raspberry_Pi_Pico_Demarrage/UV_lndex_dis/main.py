from time import sleep_ms, ticks_ms
from machine import I2C, Pin
from lcd1602_i2c import I2cLcd

sensor_temp = machine.ADC(0)          #GP26
conversion_factor = 3.3 / (65535)

# The PCF8574 has a jumper selectable address: 0x20 - 0x27
DEFAULT_I2C_ADDR = 0x27#0X27#


if __name__ == "__main__":    
    i2c = I2C(0,scl=Pin(5), sda=Pin(4), freq=100000)
    lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
    lcd.clear() 
    while True:
        reading = sensor_temp.read_u16() * conversion_factor
        adv = reading
        print('AD is',adv)
        
        if adv > 1.170:            
            dat =11
        elif adv > 1.079:
            dat =10
        elif adv > 0.976:
            dat =9    
        elif adv > 0.881:
            dat =8    
        elif adv > 0.795:
            dat =7
        elif adv > 0.696:
            dat =6    
        elif adv > 0.606:
            dat =5    
        elif adv > 0.503:
            dat =4    
        elif adv > 0.408:
            dat =3    
        elif adv > 0.318:
            dat =2    
        elif adv > 0.227:
            dat =1
        else:
            dat =0
            
        lcd.move_to(1, 0)
        lcd.putstr("UV lndex:")
        lcd.move_to(11, 0)
        lcd.putstr(str(dat))
        lcd.putchar(" ")
        sleep_ms(500)
