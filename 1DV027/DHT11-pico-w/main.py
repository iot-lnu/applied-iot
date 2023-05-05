from machine import Pin, I2C
import utime as time
from dht import DHT11, InvalidChecksum

# The GPIO number is 13 which is equal to the pin number 17
pin = Pin(13, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(pin)

while True:
    time.sleep(2)
    try:
        t = (sensor.temperature)
        time.sleep(2)
        h = (sensor.humidity)
    except:
        print("An exception occurred")  
        continue  
    print("Temperature: {}".format(sensor.temperature))
    print("Humidity: {}".format(sensor.humidity))

