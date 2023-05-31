from machine import Pin
import time



# Pin setup
controlPin = Pin(27, Pin.OUT)
led = Pin("LED", Pin.OUT)

# Initialize pin
controlPin.value(0)
led.off()
time.sleep_us(5)

while True:
    controlPin.value(1)
    led.on()
    print("Device is on!")
    time.sleep(5)

    controlPin.value(0)
    led.off()
    print("Device is off!")
    time.sleep(5)