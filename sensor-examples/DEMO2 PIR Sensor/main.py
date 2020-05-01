
from machine import Pin
import time
from machine import Timer

#config
motionDetected = 1
noMotionDetected = 0
hold_time_sec = 0.1
pir = Pin('P4',mode=Pin.IN)

chrono = Timer.Chrono()
chrono.start()

print("Starting Detection")
while True:
    if pir()==motionDetected:
        print(chrono.read(), "Motion Detected!")
    # print(pir())

    if pir()==noMotionDetected:
        pass

    time.sleep(hold_time_sec)
