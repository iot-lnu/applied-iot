# Link: https://randomnerdtutorials.com/micropython-bme280-esp32-esp8266/

from machine import Pin, SoftI2C
from time import sleep
import bme280

# ESP32 - Pin assignment
i2c = SoftI2C(scl=Pin(27), sda=Pin(26), freq=10000)


while True:
  bme = bme280.BME280(i2c=i2c)
  temp = bme.temperature
  hum = bme.humidity
  pres = bme.pressure
  # uncomment for temperature in Fahrenheit
  #temp = (bme.read_temperature()/100) * (9/5) + 32
  #temp = str(round(temp, 2)) + 'F'
  print('Temperature: ', temp)
  print('Humidity: ', hum)
  print('Pressure: ', pres, '\n')

  sleep(5)