from machine import Pin, Timer
from shared import event_manager
import dht

class SensorDHT22:
    def __init__(self, io):
        # instancie un DHT22
        self.__dht = dht.DHT22(Pin(io, Pin.OUT))
        # démarre un timer périodique pour prendre la mesure
        self.__tick_timer = Timer()
        self.__tick_timer.init(mode=Timer.PERIODIC, period=3000, callback=self.__tick)

    def __tick(self, timer):
        # effectue une mesure
        try:
            self.__dht.measure()
            temperature = self.__dht.temperature()  # en °C
            event_manager.publish({"from":"SensorDHT22", "event":"temperature", "payload":temperature})
            humidity = self.__dht.humidity()        # en %
            event_manager.publish({"from":"SensorDHT22", "event":"humidity", "payload":humidity})
            #print("Température: {:.1f}°C".format(temperature))
            #print("Humidité: {:.1f}%".format(humidity))
        except OSError as e:
            print("Erreur de lecture du capteur DHT22:", e)

