from PicoAutonomousRobotics import KitronikPicoRobotBuggy
import time

class Ultrason:

    def __init__(self, kprBuggy):
        self.kpr = kprBuggy
        self.kpr.setMeasurementsTo("meter")

    def distance_mm(self):
        """
        Get the distance in milimeters without floating point operations.
        """
        mm = self.kpr.getDistance()*10
        return mm

    def distance_cm(self):
        """
        Get the distance in centimeters with floating point operations.
        It returns a float
        """
        cms = self.kpr.getDistance()
        return cms


if __name__ == '__main__':
    print('test classe ultrason')
    kprb = KitronikPicoRobotBuggy()
    sensor = Ultrason(kprb)
    while True:
        distance = sensor.distance_cm()
        print('Distance:', "{0:2.2f}".format(distance), 'cm')
        time.sleep(1)