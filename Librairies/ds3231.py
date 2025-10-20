from machine import I2C
import time

class DS3231:
    ADDRESS = 0x68

    def __init__(self, i2c: I2C):
        self.i2c = i2c

    def bcd2dec(self, bcd):
        return (bcd // 16) * 10 + (bcd % 16)

    def dec2bcd(self, dec):
        return (dec // 10) * 16 + (dec % 10)

    def get_time(self):
        # Lit les registres 0x00 à 0x06 : secondes, minutes, heures, jour de la semaine, jour du mois, mois, année
        data = self.i2c.readfrom_mem(self.ADDRESS, 0x00, 7)
        sec = self.bcd2dec(data[0] & 0x7F)
        minute = self.bcd2dec(data[1])
        hour = self.bcd2dec(data[2] & 0x3F)  # format 24h
        wday = self.bcd2dec(data[3])
        day = self.bcd2dec(data[4])
        month = self.bcd2dec(data[5] & 0x1F)
        year = self.bcd2dec(data[6]) + 2000
        return (year, month, day, wday, hour, minute, sec)

    def set_time(self, year, month, day, wday, hour, minute, sec):
        # Convertit en BCD puis écrit dans les registres
        yy = year - 2000
        buf = bytearray(7)
        buf[0] = self.dec2bcd(sec)
        buf[1] = self.dec2bcd(minute)
        buf[2] = self.dec2bcd(hour)
        buf[3] = self.dec2bcd(wday)
        buf[4] = self.dec2bcd(day)
        buf[5] = self.dec2bcd(month)
        buf[6] = self.dec2bcd(yy)
        self.i2c.writeto_mem(self.ADDRESS, 0x00, buf)

    def set_alarm_in(self, delay_seconds):
        """Programme une alarme dans X secondes"""
        #print("Program alarme dans {:04d} secondes".format(delay_seconds))
        _, _, _, _, h, m, s = self.get_time()
        total = (h * 3600 + m * 60 + s + delay_seconds) % 86400
        nh = total // 3600
        nm = (total % 3600) // 60
        ns = total % 60

        data = bytearray([
            self.dec2bcd(ns) & 0x7F,
            self.dec2bcd(nm) & 0x7F,
            self.dec2bcd(nh) & 0x7F,
            0x80   # ignorer jour/date
        ])
        self.i2c.writeto_mem(self.ADDRESS, 0x07, data)

        # Active INTCN + A1IE
        ctrl = self.i2c.readfrom_mem(self.ADDRESS, 0x0E, 1)[0]
        ctrl |= 0b00000101
        self.i2c.writeto_mem(self.ADDRESS, 0x0E, bytes([ctrl]))

        # Efface drapeau d’alarme précédent
        self.i2c.writeto_mem(self.ADDRESS, 0x0F, b'\x00')


    def clear_alarm_flag(self):
        status = self.i2c.readfrom_mem(self.ADDRESS, 0x0F, 1)[0]
        status &= ~0b00000001
        self.i2c.writeto_mem(self.ADDRESS, 0x0F, bytes([status]))
