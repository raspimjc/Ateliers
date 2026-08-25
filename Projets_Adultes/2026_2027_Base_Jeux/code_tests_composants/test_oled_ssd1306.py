"""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Raspberry Pi Pico SSD1306 OLED Display (MicroPython)     ┃
┃                                                          ┃
┃ A program to display Raspberry Pi logo, text, and a      ┃
┃ simple timer animation on an SSD1306 OLED display        ┃
┃ connected to a Raspberry Pi Pico.                        ┃
┃                                                          ┃
┃ Copyright (c) 2023 Anderson Costa                        ┃
┃ GitHub: github.com/arcostasi                             ┃
┃ License: MIT                                             ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf, sys
import utime

pix_res_x = 127
pix_res_y = 64

def init_i2c(scl_pin, sda_pin):
    # Initialize I2C device
    i2c_dev = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)
    '''
    i2c_addr = [hex(ii) for ii in i2c_dev.scan()]
    
    if not i2c_addr:
        print('No I2C Display Found')
        sys.exit()
    else:
        print("I2C Address      : {}".format(i2c_addr[0]))
        print("I2C Configuration: {}".format(i2c_dev))
    '''
    return i2c_dev

def display_logo_raspberry(oled):
    # Display the Raspberry Pi logo on the OLED
    buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|?\x00\x01\x86@\x80\x01\x01\x80\x80\x01\x11\x88\x80\x01\x05\xa0\x80\x00\x83\xc1\x00\x00C\xe3\x00\x00~\xfc\x00\x00L'\x00\x00\x9c\x11\x00\x00\xbf\xfd\x00\x00\xe1\x87\x00\x01\xc1\x83\x80\x02A\x82@\x02A\x82@\x02\xc1\xc2@\x02\xf6>\xc0\x01\xfc=\x80\x01\x18\x18\x80\x01\x88\x10\x80\x00\x8c!\x00\x00\x87\xf1\x00\x00\x7f\xf6\x00\x008\x1c\x00\x00\x0c \x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
    fb = framebuf.FrameBuffer(buffer, 32, 32, framebuf.MONO_HLSB)
    
    oled.fill(0)
    oled.blit(fb, 96, 0)
    oled.show()
    
def display_logo_micropython(oled):
    # Display the Micropython logo on the OLED
    buffer = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x10\x8a\n0\x10$\xc8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00x\xfe\xff?\xfe\xfd|\xfb\xf8\xfc\xff|\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xc0@\xe0\xe0\xe0\xc0\xc1c\x9f\xff\x0f\xce\xff\xff\xcf\xe3\xf0pp\xa0\xe0\xe0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xff\xfb\xe7\xdf\x8e\x9e\xfd\x95"$%\x00\xfe\xff\xff\xed\xdd\xce\xce\xff\xe7\xe7\xf7\xfb\xf9\xfep\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@6\x9bg7\xcfo\x9d\xdb?\xbbws\xf7\xfa\xfa\xf9\xf4\xfd\xf7\xf3\xf1\xfdsy\xbd;\xd9\x9do\xcc6g\x9b6@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x01\x04\x03\t\x06\x13\x0c&\x19\r\x1b\x1b\r\x19&\x0c\x13\x06\t\x03\x04\x01\x02\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
    fb = framebuf.FrameBuffer(buffer, 48, 48, framebuf.MVLSB)
    oled.fill(0)
    oled.blit(fb, 8, 0)
    oled.show()

def display_text(oled):
    # Display text on the OLED
    oled.text("Raspberry Pi", 5, 5)
    oled.text("Pico", 5, 15)
    oled.show()

def display_anima(oled):
    # Display a simple timer animation on the OLED
    start_time = utime.ticks_ms()

    while True:
        elapsed_time = (utime.ticks_diff(utime.ticks_ms(), start_time) // 1000) + 1
        
        # Clear the specific line by drawing a filled black rectangle
        oled.fill_rect(5, 40, oled.width - 5, 8, 0)

        oled.text("Julie:", 5, 30)
        oled.text(str(elapsed_time) + " sec", 5, 40)
        oled.show()
        utime.sleep_ms(1000)

#GIMP
#Image de départ en couleur avec definition > 128x64
#Image -> Mode -> Couleurs indexées -> Utiliser une palette noir et blanc (1bit)
#Image -> Echelle -> Taille de l'image -> max 128 pixels large et 64 pixels hauteur
#Couleurs -> Inverser (pour inverser le noir et le blanc)
# ou utiliser le pico pour inverser (oled.invert(1))
#Fichier -> Exporter sous -> .pbm (choisir formatage de type raw)
def display_pbm(oled):        
    #with open('upy-logo.pbm', 'rb' ) as f:
    with open('pikachu.pbm', 'rb' ) as f:
        f.readline() # Magic number    P4 for pbm (Portable Bitmap)
        f.readline() # Creator comment
        f.readline() # Dimensions
        data = bytearray(f.read())

    fbuf = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)
    oled.invert(1)
    oled.blit(fbuf, 0, 0)
    oled.show()

def display_pbm_2(oled):        
    with open('avatar2.pbm', 'rb' ) as f:
        f.readline() # Magic number    P4 for pbm (Portable Bitmap)
        f.readline() # Creator comment
        f.readline() # Dimensions
        data = bytearray(f.read())

    fbuf = framebuf.FrameBuffer(data, 64, 64, framebuf.MONO_HLSB)
    oled.invert(1)
    oled.blit(fbuf, 0, 0)
    oled.show()


def main():
    i2c_dev = init_i2c(scl_pin=19, sda_pin=18)
    oled = SSD1306_I2C(pix_res_x, pix_res_y, i2c_dev)
    display_logo_raspberry(oled)
    #display_logo_micropython(oled)
    display_text(oled)
    #display_anima(oled)
    #display_pbm(oled)
    #display_pbm_2(oled)


if __name__ == '__main__':
    main()
