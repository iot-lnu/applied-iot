from dht import DHT
from machine import Pin
import time

# Type 0 = dht11
# Type 1 = dht22

th = DHT(Pin('P23', mode=Pin.OPEN_DRAIN), 1)
time.sleep(2)

def value():
    result = th.read()
    print('reading ...')
    if result.is_valid():
        return(result.temperature,result.humidity)
