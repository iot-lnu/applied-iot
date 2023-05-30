from machine import Pin
import time

halleffect = Pin('P15', mode=Pin.IN)

while True:
    value = halleffect()
    print(value)
    time.sleep_ms(100)
