from machine import Pin, PWM, Timer
import time

pwm = PWM(Pin(2))
key1 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)


#moto run range:500--2500 us,  precision: 0.09°/1us,
#us= duty*20000/65535
#duyt=us*65535/20000
pwm.freq(50)                               #50hz=20000us duty times=20000/65535
DUTY0 = 1638                               #us= 500us,0°
DUTY45 = 3276                              #us= 1000us,45°
DUTY90 = 4915                              #us= 1500us,90°
DUTY100 = 5278                             #us= 1611us,100°
DUTY135 = 6554                             #us= 2000us,135°
DUTY150 = 7099                             #us= 2166us,150°
DUTY180 = 8192                             #us= 2500us,180°



def tick(timer):      
    global mode_ptr    
    global key1_cnt   
    global key1_press  
    global set_reset_flag
    global flag
    
    if key1.value()== 0:
        key1_cnt +=1
        if key1_cnt>2 and key1_press==0:
            key1_cnt = 0
            key1_press = 1
            set_reset_flag = 0
            flag = 1
            mode_ptr +=1           
            if mode_ptr>6:
                mode_ptr = 0                
                
    else:
        key1_cnt = 0    
        key1_press = 0


if __name__ == "__main__":    
    tim = Timer()
    tim.init(freq=50, mode=Timer.PERIODIC, callback=tick)
    mode_ptr = 0    
    key1_cnt=0    
    key1_press = 0
    flag = 0;
    set_reset_flag = 0
    while True:
         if set_reset_flag == 0:
             pwm.duty_u16(DUTY0)
             set_reset_flag = 1
             time.sleep(1)  
         else:
            if mode_ptr == 0:
                pwm.duty_u16(DUTY0)
                if flag:
                    print('0')
                    flag = 0
            
            
            if mode_ptr == 1:
                pwm.duty_u16(DUTY45)
                if flag:
                    print('45')
                    flag = 0
                    
            if mode_ptr == 2:
                pwm.duty_u16(DUTY90)
                if flag:
                    print('90')
                    flag = 0
                    
            if mode_ptr == 3:
                pwm.duty_u16(DUTY100)
                if flag:
                    print('100')
                    flag = 0
                    
            if mode_ptr == 4:
                pwm.duty_u16(DUTY135)
                if flag:
                    print('135')
                    flag = 0
                
            if mode_ptr == 5:
                pwm.duty_u16(DUTY150)
                if flag:
                    print('150')
                    flag = 0
                
                
            if mode_ptr == 6:
                pwm.duty_u16(DUTY180)
                if flag:
                    print('180')
                    flag = 0