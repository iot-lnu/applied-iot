import time
from lib.bme import BME

sda = 'P7'
scl = 'P8'

bme = BME((sda, scl), calibration_time=5)

while True:
    # Get air condition values
    temp, humidity, pressure, air_quality = bme.get_values()

    # Print all
    print('Temperature:', temp, '°C')
    print('Humidity:', humidity, '%')
    print('pressure:', pressure, 'hPa')
    print('air_quality:', air_quality, 'IAQ')
    print()

    time.sleep(1)
