from machine import Pin
import time

# TO-DO

Tilt = Pin('P15', Pin.IN, pull=Pin.PULL_DOWN)
while True:
    print(Tilt.value())
    time.sleep_ms(100)
