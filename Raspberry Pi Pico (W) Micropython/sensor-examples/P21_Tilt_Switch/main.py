from machine import Pin
import time

tiltPin = Pin(27, Pin.IN)

while True:
    if tiltPin.value() == 1:
        print("Switch ON...")
    else:
        print("Switch OFF...")
    time.sleep_ms(500) 