import network
import urequests as requests
import machine
from machine import Pin
from time import sleep
import random
import keys
import wifiConnection

DELAY = 5  # Delay in seconds between posts

# Builds the json to send the request
def build_json(variable, value):
    try:
        data = {variable: {"value": value}}
        return data
    except:
        return None

# Random number generator
def random_integer(upper_bound):
    return random.getrandbits(32) % upper_bound

# Sending data to Ubidots Restful Webserice
def sendData(device, variable, value):
    try:
        url = "https://industrial.api.ubidots.com/"
        url = url + "api/v1.6/devices/" + device
        headers = {"X-Auth-Token": keys.TOKEN, "Content-Type": "application/json"}
        data = build_json(variable, value)

        if data is not None:
            print(data)
            req = requests.post(url=url, headers=headers, json=data)
            return req.json()
        else:
            pass
    except:
        pass

# WiFi connection
wifiConnection.connect()

# Your device send a random value between 0 and 100 every five second to
# Ubidots
while True:
    value = random_integer(100)
    returnValue = sendData(keys.DEVICE_LABEL, keys.VARIABLE_LABEL, value)
    sleep(DELAY)

# WiFi disconnection
wifiConnection.disconnect()