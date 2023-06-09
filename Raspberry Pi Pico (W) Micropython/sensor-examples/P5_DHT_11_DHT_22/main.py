import dht
import machine
import time

tempSensor = dht.DHT11(machine.Pin(27))     # DHT11 Constructor 
# tempSensor = dht.DHT22(machine.Pin(27))   # DHT22 Constructor

while True:
    try:
        tempSensor.measure()
        temperature = tempSensor.temperature()
        humidity = tempSensor.humidity()
        print("Temperature is {} degrees Celsius and Humidity is {}%".format(temperature, humidity))
    except Exception as error:
        print("Exception occurred", error)
    time.sleep(2)