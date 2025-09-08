#Native libs
import network
import time

#Third Party
from umqtt.robust import MQTTClient

# Internal libs
import constants

class Mqtt:
    def __init__(self, base_topic='bob'):
        self.base_topic = base_topic
        self.__connectToNetwork()
        self.mqtt_client = self.__connectToMqtt()
        self.mqtt_client.set_callback(self.__subCallback)
        self.mqtt_client.subscribe(f"{self.base_topic}/cmd")


    def publish(self, topic, value):
        '''Sends data to the broker'''
        self.mqtt_client.publish(f"{self.base_topic}/{topic}", value)
        print("Publish Done")

    def __connectToNetwork(self):
        # Pass in string arguments for ssid and password

        # Just making our internet connection
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(constants.INTERNET_NAME, constants.INTERNET_PASSWORD)

        # Wait for connect or fail
        max_wait = 10
        while max_wait > 0:
          if wlan.status() < 0 or wlan.status() >= 3:
            break
          max_wait -= 1
          print('waiting for connection...')
          time.sleep(1)
        # Handle connection error
        if wlan.status() != 3:
           print(wlan.status())
           raise RuntimeError('network connection failed')
        else:
          print('connected')
          print(wlan.status())
          status = wlan.ifconfig()
          print(status)
          
    def __connectToMqtt(self) :          
        '''Connects to Broker'''
        # Client ID can be anything
        client = MQTTClient(
            client_id=constants.CLIENT_ID,
            server=constants.SERVER_HOSTNAME,
            port=1883,
            user=constants.USER,
            password=constants.PASSWORD,
            keepalive=7200,
            ssl=False,
            #ssl_params={'server_hostname': constants.SERVER_HOSTNAME}
        )
        client.connect()
        return client
    
    def __subCallback( topic, msg ):
        print(f"receive from {topic}: {msg}")
        
        
if __name__ == "__main__":
    # code de test
    mqtt = Mqtt("titan")
    count = 0
    while True:
        mqtt.publish('counter', f"test _message {count}")
        count += 1

        time.sleep(3)
