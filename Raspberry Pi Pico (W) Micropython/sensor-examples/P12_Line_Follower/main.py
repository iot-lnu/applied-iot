import time
from machine import Pin

# Set the led and sensor pin 
led = Pin("LED", Pin.OUT)
sensor = Pin(27, Pin.IN)

state = True

while True:
    state = sensor.value()
    if state == False:
        led.on()
        print("Following the line...")
    else:
        led.off()
        print("Out of the line...")
    time.sleep_ms(20)