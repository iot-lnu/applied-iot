# my first project ..
import time
from machine import Pin
import _thread
from dht import DHT

# Type 0 = dht11
# Type 1 = dht22

th = DHT(Pin('P23', mode=Pin.OPEN_DRAIN), 1)
time.sleep(2)



while True:
    result = th.read()
    while not result.is_valid():
        time.sleep(.5)
        result = th.read()
    print('Temp:', result.temperature)
    print('RH:', result.humidity)
    pybytes.send_signal(1,result.temperature)
    pybytes.send_signal(2,result.humidity)

    time.sleep(5)
