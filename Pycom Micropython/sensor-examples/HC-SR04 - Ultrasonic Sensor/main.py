# https://core-electronics.com.au/tutorials/hc-sr04-ultrasonic-sensor-with-pycom-tutorial.html
import utime
import pycom
import machine
from machine import Pin

# initialise Ultrasonic Sensor pins
echo = Pin(Pin.exp_board.G7, mode=Pin.IN) # Lopy4 specific: Pin('P20', mode=Pin.IN)
trigger = Pin(Pin.exp_board.G8, mode=Pin.OUT) # Lopy4 specific Pin('P21', mode=Pin.IN)
trigger(0)

# Ultrasonic distance measurment
def distance_measure():
    # trigger pulse LOW for 2us (just in case)
    trigger(0)
    utime.sleep_us(2)
    # trigger HIGH for a 10us pulse
    trigger(1)
    utime.sleep_us(10)
    trigger(0)

    # wait for the rising edge of the echo then start timer
    while echo() == 0:
        pass
    start = utime.ticks_us()

    # wait for end of echo pulse then stop timer
    while echo() == 1:
        pass
    finish = utime.ticks_us()

    # pause for 20ms to prevent overlapping echos
    utime.sleep_ms(20)

    # calculate distance by using time difference between start and stop
    # speed of sound 340m/s or .034cm/us. Time * .034cm/us = Distance sound travelled there and back
    # divide by two for distance to object detected.
    distance = ((utime.ticks_diff(start, finish)) * .034)/2

    return distance * -1

while True:
    print(distance_measure())
