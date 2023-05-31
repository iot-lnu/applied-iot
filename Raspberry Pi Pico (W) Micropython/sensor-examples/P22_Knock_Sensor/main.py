from machine import Pin
import time

knockPin = Pin(27, Pin.IN)

while True:
    if knockPin.value() == 1:
        print("No Knocking...")
    else:
        print("Knock Detected...")
    time.sleep_ms(500)