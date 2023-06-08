from machine import Pin
import utime as time
from dht import DHT11
import struct 

pin = Pin(27, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(pin)

while True:
    time.sleep(5)

    t  = (sensor.temperature)
    h = (sensor.humidity)
    
    print("Temperature: {}".format(t))
    print("Humidity: {}".format(h))
