from ADXL345 import ADXL345
from machine import I2C
# configure the I2C bus
i2c = I2C(0, I2C.MASTER, baudrate=100000)
scans = i2c.scan() # returns list of slave addresses
print(scans)

obj = ADXL345(i2c)

print(obj.xValue, obj.yValue, obj.zValue,)
