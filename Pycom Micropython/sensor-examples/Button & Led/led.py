import time
from machine import Pin
led = Pin('P12', Pin.OUT, pull = Pin.PULL_DOWN)

while True:
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)
