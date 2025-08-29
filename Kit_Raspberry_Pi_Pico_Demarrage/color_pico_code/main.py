from machine import Pin,Timer
import time
from ws2812b import ws2812b

num_leds = 144
pixels = ws2812b(num_leds, 0,0, delay=0)

#LED = VCC
p2 = Pin(1, Pin.IN, Pin.PULL_UP)             #OUT pin
#S0_out = GND                                 #2% output frequency
#S1_out = VCC
S2_out = machine.Pin(14, machine.Pin.OUT)
S3_out = machine.Pin(15, machine.Pin.OUT)

dat = 0
flag = 0
adj_en = 0
adj_num = 0
i = 0
    
dis_r = 0
dis_g = 0
dis_b = 0    
    
dat_v_r = 0
dat_v_g = 0
dat_v_b = 0
    
adj_v_r = 0
adj_v_g = 0
adj_v_b = 0
        
adj_temp_r = 0
adj_temp_g = 0
adj_temp_b = 0



def init_out(self):
    global dat
#    print("IRQ flags:",dat)
    dat+=1
    
    
def tick(timer):    
    global flag
    global i
    global adj_num
    global adj_en
    global dat
    
    
    global dis_r
    global dis_g
    global dis_b
    
    global dat_v_r
    global dat_v_g
    global dat_v_b
    
    global adj_v_r
    global adj_v_g
    global adj_v_b
        
    global adj_temp_r
    global adj_temp_g
    global adj_temp_b
        
    i+=1
    if i>=3:
        i=0
    if i==0:               #set the filter to red
        S2_out.value(0) 
        S3_out.value(0)
        dat_v_b = dat            #read blue value
        dat = 0
        if adj_en:
            dis_b = int(dat_v_b*adj_v_b/10.0)
            if dis_b >255:
                dis_b = 255
            print("Blue=\r\n",dis_b) 
        else: 
            adj_temp_b+=dat_v_b
        
    elif i==1:   #set the filter to green
        S2_out.value(1) 
        S3_out.value(1)        
        dat_v_r = dat              #read red value
        dat = 0    
        if adj_en:
            dis_r = int(dat_v_r*adj_v_r/10.0)
            if dis_r >255:
                dis_r = 255
            print("Red=\r\n",dis_r) 
        else: 
            adj_temp_r+=dat_v_r
            
    else:    #set the filter to blue
        S2_out.value(0)
        S3_out.value(1)
        dat_v_g = dat                 #read green value
        dat = 0
        if adj_en:
            dis_g = int(dat_v_g*adj_v_g/10.0)
            if dis_g >255:
                dis_g = 255
            print("Green=\r\n",dis_g) 
        else: 
            adj_temp_g+=dat_v_g
        
    if adj_en == 0:       
        if adj_num>=30:                                   # adj_num%3=0  
            adj_v_r=adj_temp_r/10.0
            adj_v_r=255.0/adj_v_r*10.0
            adj_v_g=adj_temp_g/10.0
            adj_v_g=255.0/adj_v_g*10.0
            adj_v_b=adj_temp_b/10.0
            adj_v_b=255.0/adj_v_b*10.0
            adj_en=1
            print("adj_rgb=%d-%d-%d\r\n",adj_v_r,adj_v_g,adj_v_b) 
        else:
            adj_num+=1

if __name__ == "__main__": 
    
    S2_out.value(0) 
    S3_out.value(0)
    p2.irq(handler=init_out, trigger=Pin.IRQ_FALLING)                     #IO Interrupts
    
    tim = Timer()
    tim.init(freq=20, mode=Timer.PERIODIC, callback=tick)                #Timer Interrupts = 50ms
    
    while True:       
        pixels.fill(dis_r,dis_g,dis_b)    
        pixels.show()
        time.sleep(0.5)
       