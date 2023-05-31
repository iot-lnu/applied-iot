from machine import Pin
import time

# Set the pin for reed switch
Reed_switch = Pin(27, Pin.IN)

while True:
    if Reed_switch.value() == 1:
        print("Magnet Detected...")
        time.sleep(1) 