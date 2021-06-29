from machine import Pin
import time

tilt = Pin('P15', mode=Pin.IN, pull=Pin.PULL_DOWN)
# Read value by running tilt()
while True:
    value = tilt()
    print(value)
    time.sleep_ms(300)
