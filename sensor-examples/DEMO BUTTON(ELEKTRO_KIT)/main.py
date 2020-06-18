
from machine import Pin
import time

p_in = Pin('P10', mode = Pin.IN)  # SENSOR BUTTON FORM ELEKTROKIT
# p_in = Pin('P10', mode=Pin.IN, pull=Pin.PULL_UP)  # A REGULAR BUTTON PULLED UP  

while(1):
    val = p_in() # get value, 0 or 1
    if val == 1:
        print("NOT PRESSED !")
    else:
        print("PRESSED !")
    
    time.sleep(1)