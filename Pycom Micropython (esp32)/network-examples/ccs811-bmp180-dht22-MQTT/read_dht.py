from dth import DTH
from machine import Pin
import time

# Type 0 = dht11
# Type 1 = dht22



def value():
    th = DTH(Pin('P23', mode=Pin.OPEN_DRAIN), 1)
    time.sleep(3)
    result = th.read()
    # print('Temp:', result.temperature)
    # print('RH:', result.humidity)
    if result.is_valid():
        return(result.temperature,result.humidity)
