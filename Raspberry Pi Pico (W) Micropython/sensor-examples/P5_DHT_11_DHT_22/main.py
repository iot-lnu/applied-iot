from machine import Pin
import utime as time
from dht import DHT11

while True:
    time.sleep(5)
    pin = Pin(27, Pin.OUT, Pin.PULL_DOWN)
    sensor = DHT11(pin)
    t  = (sensor.temperature)
    h = (sensor.humidity)
    print("Temperature: {}".format(sensor.temperature))
    print("Humidity: {}".format(sensor.humidity))
