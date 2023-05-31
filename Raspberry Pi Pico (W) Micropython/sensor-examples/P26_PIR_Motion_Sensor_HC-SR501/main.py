from machine import Pin
import time

LED = Pin("LED", Pin.OUT)
PIR_sensor = Pin(27, Pin.IN, Pin.PULL_UP)
LED.off()
time.sleep(2)

while True:
   if PIR_sensor.value() == 1:
       print("Motion Detected! -> LED is now ON")
       LED.on()
       time.sleep(5)
   else:
       print("No motion detected -> LED is OFF")
       LED.off()
       time.sleep(1)