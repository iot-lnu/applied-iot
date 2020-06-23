from machine import Pin
import time

p_in = Pin('P16', mode = Pin.IN)  # SENSOR BUTTON FORM ELEKTROKIT

while(1):
    val = p_in() # get value, 0 or 1
    if val == 1:
        print("NOT DETECTED!")
    else:
        print("DETECTED !")
    
    time.sleep(0.1)