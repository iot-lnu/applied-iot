from machine import Pin
import time
'''
One of usage of this sensor is in printers to indicate if there is paper or we need to put a paper in the tray.
'''
interruptPin = Pin(27, Pin.IN)

while True:
    if interruptPin.value() == 1:
        print("Paper inserted...")
    else:
        print("No paper...")
    time.sleep_ms(500) 