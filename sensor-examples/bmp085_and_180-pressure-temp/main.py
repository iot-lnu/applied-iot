# Example for CCS811 and BME280 sensor Sparkfun
from machine import I2C
import time
from bmp085 import BMP180
# Using the library. https://github.com/robert-hh/BMP085_BMP180



i2c = I2C(0)                         # create on bus 0
i2c = I2C(0, I2C.MASTER)             # create and init as a master
i2c = I2C(0, pins=('P9','P10'))      # PIN assignments (P9=SDA, P10=SCL)
i2c.init(I2C.MASTER, baudrate=115200) # init as a master

bmp = BMP180(i2c)

print('Temperature', bmp.temperature)
print('Pressure', bmp.pressure)
