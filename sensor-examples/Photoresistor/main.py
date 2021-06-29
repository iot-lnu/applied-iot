from machine import ADC
from machine import Pin
import time

LightSensorPin = 'P16' # sensor connected to P16. Valid pins are P13 to P20.

lightPin = Pin(LightSensorPin, mode=Pin.IN)  # set up pin mode to input
#
adc = ADC(bits=10)             # create an ADC object bits=10 means range 0-1024 the lower value the less light detected
apin = adc.channel(attn=ADC.ATTN_11DB, pin=LightSensorPin)   # create an analog pin on P16;  attn=ADC.ATTN_11DB measures voltage from 0.1 to 3.3v


while True:
    val = apin() # read an analog value
    print("Value", val)
    time.sleep(1)  # wait 1 sec
