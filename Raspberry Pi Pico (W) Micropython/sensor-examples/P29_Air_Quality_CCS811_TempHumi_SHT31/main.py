from machine import SoftI2C, Pin
import time
import sht31                        # https://github.com/kfricke/micropython-sht31
import CCS811                       # https://gist.github.com/jiemde

i2c = SoftI2C(scl=Pin(27), sda=Pin(26), freq =10000)

CCS811_ADDR = const(0x5A)                       # CCS811 Address
ccs = CCS811.CCS811(i2c=i2c, addr=CCS811_ADDR)  # CCS811 initialization
SHT31_ADDR = const(0x44)                        # SHT31 Address
sht = sht31.SHT31(i2c, addr=SHT31_ADDR)         # SHT31 initialization


while True:
    shtValue = sht.get_temp_humi()
    checkData = ccs.data_available()
    print(checkData)
    if checkData:
        ccs.put_envdata(humidity=shtValue[1],temp=shtValue[0])   # Compensate Temp/Humidity Error
        ccs.readSensorData()
        co2 = ccs.eCO2
        voc = ccs.tVOC
        print("Temperature is {}".format(shtValue[0]))
        print("Humidity is {}".format(shtValue[1]))
        print('CO2 level: {}{} '.format(str(co2), ' ppm  '), end='')
        print('tVOC level: {}'.format(str(voc)))
    time.sleep(2)