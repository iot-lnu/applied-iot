# Example for CCS811 sensor

from machine import I2C
import time

i2c = I2C(0)                         # create on bus 0
i2c = I2C(0, I2C.MASTER)             # create and init as a master
i2c = I2C(0, pins=('P9','P10'))      # PIN assignments (P9=SDA, P10=SCL)
i2c.init(I2C.MASTER, baudrate=10000) # init as a master

# https://github.com/Notthemarsian/CCS811

import CCS811
ccs = CCS811.CCS811(i2c=i2c,addr=91)
time.sleep(1) # Just to get it some slack starting up ...


while True:
    ccs.data_ready() # Make a reading
    time.sleep(2)
    co2 = ccs.eCO2
    voc = ccs.tVOC
    if co2 > 10:
        print('CO2 level: ' + str(co2) + ' ppm')
        print('tVOC level: ' + str(voc))
