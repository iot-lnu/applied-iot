import time
from machine import ADC
from machine import Pin

# Pin setup
analogPin = ADC(27)
digitalPin = Pin(26, Pin.IN)

while True:
    analogValue = analogPin.read_u16()
    digitalValue = digitalPin.value()
    print("The magnetic strength is {}".format(analogValue))  # The stronger magnet the lower value it produce
    if digitalValue == True:
        print("Digital pin activated...")
    else:
        print("Digital pin inactive...")
    time.sleep(1)