from machine import I2C
import utime
import sys
from lib.lidar import LIDAR

# TF-Luna has the default slave_address 0x10
LIDAR_ADDRESS = 0x10

i2c_0 = I2C(0, mode=I2C.MASTER, baudrate=400000, pins=('P7', 'P8'))
utime.sleep_ms(50)

slaves = i2c_0.scan()
if LIDAR_ADDRESS not in slaves:
    print('Bus error: Please check LIDAR wiring')
    sys.exit()


lidar = LIDAR(i2c_0, LIDAR_ADDRESS)
print(lidar.version())

# Output limit when out of range
# Output only when between 20cm and 150cm (Up to 800cm)
lidar.set_min_max(20, 150)

lidar.set_frequency(250)

while True:
    print(lidar.distance())
    utime.sleep_ms(10)
