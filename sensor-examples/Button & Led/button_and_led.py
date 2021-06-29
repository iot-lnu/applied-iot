from machine import Pin
import time

while True:
    p_in = Pin('P13', mode=Pin.IN, pull=Pin.PULL_UP)
    print(p_in.value())
    time.sleep(0.3)
