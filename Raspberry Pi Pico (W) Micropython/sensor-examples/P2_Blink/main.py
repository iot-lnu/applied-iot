import time
from machine import Pin

# Set the led pin 
led = Pin("LED", Pin.OUT)


while True:
    led.toggle()
    ''' Alternative to toggle() is either changing the value() or using on() & off() methods '''
    #led.value(1)
    #led.on()
    time.sleep(2)       # Delay for 2 seconds
    #led.value(0)
    #led.off()