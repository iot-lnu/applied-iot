from machine import Pin
import time

vibratePin = Pin(27, Pin.IN)

while True:
    if vibratePin.value() == 1:
        print("No vibration...")
    else:
        print("Vibration detected...")
    time.sleep_ms(500) 