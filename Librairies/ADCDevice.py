########################################################################
# Filename    : ADCDevice.py
# Description : Freenove ADC Module library.
# Author      : www.freenove.com
# modification: 2020/04/21
########################################################################
from machine import I2C
#import smbus
class SMBus(I2C):
    """ Provides an 'SMBus' module which supports some of the py-smbus
        i2c methods, as well as being a subclass of machine.I2C

        Hopefully this will allow you to run code that was targeted at
        py-smbus unmodified on micropython.

	    Use it like you would the machine.I2C class:

            import usmbus.SMBus

            bus = SMBus(1, pins=('G15','G10'), baudrate=100000)
            bus.read_byte_data(addr, register)
            ... etc
	"""

    def read_byte_data(self, addr, register):
        """ Read a single byte from register of device at addr
            Returns a single byte """
        return self.readfrom_mem(addr, register, 1)[0]

    def read_i2c_block_data(self, addr, register, length):
        """ Read a block of length from register of device at addr
            Returns a bytes object filled with whatever was read """
        return self.readfrom_mem(addr, register, length)

    def write_byte_data(self, addr, register, data):
        """ Write a single byte from buffer `data` to register of device at addr
            Returns None """
        # writeto_mem() expects something it can treat as a buffer
        if isinstance(data, int):
            data = bytes([data])
        return self.writeto_mem(addr, register, data)

    def write_i2c_block_data(self, addr, register, data):
        """ Write multiple bytes of data to register of device at addr
            Returns None """
        # writeto_mem() expects something it can treat as a buffer
        if isinstance(data, int):
            data = bytes([data])
        return self.writeto_mem(addr, register, data)

    # The follwing haven't been implemented, but could be.
    def read_byte(self, *args, **kwargs):
        """ Not yet implemented """
        raise RuntimeError("Not yet implemented")

    def write_byte(self, *args, **kwargs):
        """ Not yet implemented """
        raise RuntimeError("Not yet implemented")

    def read_word_data(self, *args, **kwargs):
        """ Not yet implemented """
        raise RuntimeError("Not yet implemented")

    def write_word_data(self, *args, **kwargs):
        """ Not yet implemented """
        raise RuntimeError("Not yet implemented")
        
class ADCDevice(object):
    def __init__(self,addr):
        self.cmd = 0
        self.address = addr
        self.bus=SMBus(1)
        print("ADCDevice init")
        
    def detectI2C(self,addr):
        try:
            #self.bus.write_byte(addr,0)  #LAURENCE => bypass
            print("Found device in address 0x%x"%(addr))
            return True
        except:
            print("Not found device in address 0x%x"%(addr))
            return False
            
    def close(self):
        self.bus.close()
        
class PCF8591(ADCDevice):
    def __init__(self,addr):
        super(PCF8591, self).__init__(addr)
        self.cmd = 0x40     # The default command for PCF8591 is 0x40.
        self.address = addr # 0x48 is the default i2c address for PCF8591 Module.
        
    def analogRead(self, chn): # PCF8591 has 4 ADC input pins, chn:0,1,2,3
        value = self.bus.read_byte_data(self.address, self.cmd+chn)
        value = self.bus.read_byte_data(self.address, self.cmd+chn)
        return value
    
    def analogWrite(self,value): # write DAC value
        self.bus.write_byte_data(address,cmd,value)	

class ADS7830(ADCDevice):
    def __init__(self,addr):
        super(ADS7830, self).__init__(addr)
        self.cmd = 0x84
        self.address = addr # 0x4b is the default i2c address for ADS7830 Module.   
        
    def analogRead(self, chn): # ADS7830 has 8 ADC input pins, chn:0,1,2,3,4,5,6,7
        value = self.bus.read_byte_data(self.address, self.cmd|(((chn<<2 | chn>>1)&0x07)<<4))
        return value
