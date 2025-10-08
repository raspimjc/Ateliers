#https://www.upesy.fr/blogs/tutorials/esp32-servo-motor-sg90-on-micropython?shpxid=d722b87e-355c-4a59-8798-63847a3164e8

from machine import Pin, PWM
import time

class Servo:
    # these defaults work for the standard TowerPro SG90
    __servo_pwm_freq = 50
    __min_u10_duty = 2500 # offset for correction
    __max_u10_duty = 8050  # offset for correction
    min_angle = 0
    max_angle = 180
    current_angle = 0.001


    def __init__(self, pin):
        self.__initialise(pin)


    def update_settings(self, servo_pwm_freq, min_u10_duty, max_u10_duty, min_angle, max_angle, pin):
        self.__servo_pwm_freq = servo_pwm_freq
        self.__min_u10_duty = min_u10_duty
        self.__max_u10_duty = max_u10_duty
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.__initialise(pin)


    def move(self, angle):
        #print(angle)
        # round to 2 decimal places, so we have a chance of reducing unwanted servo adjustments
        angle = round(angle, 2)
        # do we need to move?
        if angle == self.current_angle:
            return
        self.current_angle = angle
        # calculate the new duty cycle and move the motor
        duty_u10 = self.__angle_to_u10_duty(angle)
        self.__motor.duty_u16(duty_u10)

    def __angle_to_u10_duty(self, angle):
        return int((angle - self.min_angle) * self.__angle_conversion_factor) + self.__min_u10_duty


    def __initialise(self, pin):
        self.current_angle = -0.001
        self.__angle_conversion_factor = (self.__max_u10_duty - self.__min_u10_duty) / (self.max_angle - self.min_angle)
        self.__motor = PWM(Pin(pin))
        self.__motor.freq(self.__servo_pwm_freq)
        
if __name__ == '__main__':
    motor=Servo(pin=7) # A changer selon la broche utilisée
    motor.move(0) # tourne le servo à 0°
    time.sleep(0.3)
    motor.move(90) # tourne le servo à 90°
    time.sleep(0.3)
    motor.move(180) # tourne le servo à 180°
    time.sleep(0.3)
    motor.move(90) # tourne le servo à 90°
    time.sleep(0.3)
    motor.move(0) # tourne le servo à 0°
    time.sleep(0.3)
