import machine
import onewire
import ds18x20
import time
 
oneWire_pin = machine.Pin(27)   # DS18x20 connected to pin 27
# Initailize pin with Dallas Semiconductor temperature sensor DS18X20 
oneWire_sensor = ds18x20.DS18X20(onewire.OneWire(oneWire_pin))

# Scan and print the address of all sensors connected to pin 27 
sensors = oneWire_sensor.scan()
print('Found devices: ', sensors)
 
while True:
    oneWire_sensor.convert_temp()
    time.sleep_ms(750)

    for sensor in sensors:
        print("Sensor address is: {}".format(sensor))
        print("Temperature is {} degrees Celsius".format(oneWire_sensor.read_temp(sensor)))
    time.sleep(2)