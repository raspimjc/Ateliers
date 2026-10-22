from machine import Pin, PWM
from shared import event_manager

class Servo:

    def __init__(self, pin):
        self.__servo_pwm_freq = 50
        self.__min_u16_duty = 1640 - 2 # offset for correction
        self.__max_u16_duty = 7864 - 0  # offset for correction
        self.min_angle = 0
        self.max_angle = 180
        self.current_angle = 0.001
        self.__initialise(pin)


    def update_settings(self, servo_pwm_freq, min_u16_duty, max_u16_duty, min_angle, max_angle, pin):
        self.__servo_pwm_freq = servo_pwm_freq
        self.__min_u16_duty = min_u16_duty
        self.__max_u16_duty = max_u16_duty
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.__initialise(pin)

    def get_current_angle(self):
        return self.current_angle

    def get_min_angle(self):
        return self.min_angle

    def get_max_angle(self):
        return self.max_angle

    def move(self, angle):
        # round to 2 decimal places, so we have a chance of reducing unwanted servo adjustments
        angle = round(angle, 2)
        # do we need to move?
        if angle == self.current_angle:
            return
        self.current_angle = angle
        # calculate the new duty cycle and move the motor
        duty_u16 = self.__angle_to_u16_duty(angle)
        self.__motor.duty_u16(duty_u16)

    def increment(self, angle):
        if (self.current_angle+angle) >= self.max_angle:
            self.move(self.max_angle)
            # emet un evenement max atteint
            event_manager.publish({"from":"Servo", "event":"servo_maximum", "payload":self.max_angle})
        else:
            self.move(self.current_angle+angle)

    def decrement(self, angle):
        if (self.current_angle-angle) <= self.min_angle:
            self.move(self.min_angle)
            # emet un evenement max atteint
            event_manager.publish({"from":"Servo", "event":"servo_minimum", "payload":self.min_angle})
        else:
            self.move(self.current_angle-angle)

    def __angle_to_u16_duty(self, angle):
        return int((angle - self.min_angle) * self.__angle_conversion_factor) + self.__min_u16_duty


    def __initialise(self, pin):
        self.current_angle = -0.001
        self.__angle_conversion_factor = (self.__max_u16_duty - self.__min_u16_duty) / (self.max_angle - self.min_angle)
        self.__motor = PWM(Pin(pin))
        self.__motor.freq(self.__servo_pwm_freq)