from machine import I2C
from lib.ina260 import INA260
import time

sda = 'P9'
scl = 'P10'

bus = I2C(0, mode=I2C.MASTER, baudrate=100000, pins=(sda, scl))
stuff = bus.scan()

time.sleep_ms(50)

c = INA260(bus)

print("Bus voltage:", c.voltage(), "V")
print("Bus current:", c.current(), "A")
print("Bus power:", c.power(), "W")
