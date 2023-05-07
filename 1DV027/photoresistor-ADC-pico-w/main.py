from machine import ADC, Pin
from time import sleep

photoPIN = 26  #The ADC pin of Pico W

def readLight(photoGP):
    photoRes = ADC(Pin(26))
    light = photoRes.read_u16() #16 bits which means 2 bytes. The range of 2 bytes is from 0 to 65535.
    #light = round(light/65535*100,2)  # show the result in percentage
    return light
    

while True:
    print("light: " + str(readLight(photoPIN)) )
    sleep(1) # set a delay between readings