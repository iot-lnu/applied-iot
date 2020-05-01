
from machine import Pin
import time

import utime
from machine import Timer

#config
trig = Pin('P10', mode=Pin.OUT)
echo = Pin('P11', mode=Pin.IN)

print("Starting Program")
while True:

    start = utime.ticks_us()
    end = utime.ticks_us()
    offset = utime.ticks_diff(start, end)

    trig.value(1) # sending sound
    utime.sleep_us(10) # making sound for 10 microsec
    trig.value(0) # stop making sound
    start = utime.ticks_us()

    

    while not echo():
        pass


    end = utime.ticks_us()



    #The value returned by these functions may wrap around at any time, so directly subtracting them is not supported.
    # ticks_diff() should be used instead.
    # “old” value should actually precede “new” value in time, or result is undefined.

    difference = utime.ticks_diff(start, end) # measuring travel time

    print("start: ", start)
    print("end : ", end)
    print("travel time : ", difference-offset) # 

    # Calc the duration of the recieved pulse, divide the result by
    # 2 (round-trip) and divide it by 29 (the speed of sound is
    # 340 m/s and that is 29 us/cm).
    
    dist_in_cm = (difference-offset)/2/29  # DEALING WITH OFFSET
    if dist_in_cm <0 : 
        dist_in_cm = 0

    print("distance(cm): ", dist_in_cm)

    utime.sleep(2) # wait half a second before the next measuring
