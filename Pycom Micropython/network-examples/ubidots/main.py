from network import WLAN
import urequests as requests
import machine
import time

from machine import Pin
from dth import DHT # https://github.com/JurassicPork/DHT_PyCom

print("Start")

# Type 0 = dht11
# Type 1 = dht22
th = DHT(Pin('P23', mode=Pin.OPEN_DRAIN), 0) # DHT sensor is connected to port 23
time.sleep(2)  # wait 2 seconds


TOKEN = "TOKEN" # Put here your TOKEN from ubidots
DELAY = 60  # Delay in seconds

wlan = WLAN(mode=WLAN.STA)
wlan.antenna(WLAN.INT_ANT)

# Assign your Wi-Fi credentials
wlan.connect("SSID", auth=(WLAN.WPA2, "password"), timeout=5000)

# connectin to WiFi
while not wlan.isconnected ():
    print("connecting to WiFi...")
    machine.idle()
print("Connected to Wifi\n")

# Builds the json to send the request
def build_json(variable1, value1, variable2, value2, variable3, value3):
    try:
        lat = 56.853  # latitude
        lng = 14.824  # longtitude

        # data array creation
        data = {variable1: {"value": value1},
                variable2: {"value": value2, "context": {"lat": lat, "lng": lng}}, # value - main information, context - additional
                variable3: {"value": value3}}
        return data
    except:
        return None

# Sends the request. Please reference the REST API reference https://ubidots.com/docs/api/
def post_var(device, value1, value2, value3):
    try:
        url = "https://industrial.api.ubidots.com/"
        url = url + "api/v1.6/devices/" + device
        headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
        data = build_json("temperature", value1, "position", value2, "humidity", value3)
        if data is not None:
            print(data)
            req = requests.post(url=url, headers=headers, json=data) # include data as JSON object
            return req.json()
        else:
            pass
    except:
        pass

while True:
    print("infinite loop")

    result = th.read() # read the sensor
    while not result.is_valid():
        time.sleep(.5)
        result = th.read()

    print('Temp:', result.temperature)
    print('RH:', result.humidity)
    pybytes.send_signal(1,result.temperature) # optional, sends data to pybyes
    pybytes.send_signal(2,result.humidity) # optional, sends data to pybyes

    post_var("dev1", result.temperature, 1, result.humidity)  # send data to UBIDOTS
    time.sleep(DELAY)
