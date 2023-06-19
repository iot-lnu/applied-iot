import time                   # Allows use of time.sleep() for delays
from mqtt import MQTTClient   # For use of MQTT protocol to talk to Adafruit IO
import machine                # Interfaces with hardware components
import micropython            # Needed to run any MicroPython code
import random                 # Random number generator
from machine import Pin       # Define pin
import config                 # Contain all keys used here
import wifiConnection         # Contains functions to connect/disconnect from WiFi 
import ujson                  # Creating JSON object for MQTT & Telegraf
import sys                    # Using sys to print Exception reasons
import wifiConnection         # Using for WiFi connection


# Build jason format for MQTT 
def build_json(variable_1, value_1):
    try:
        data = {variable_1: value_1}
        retValue = ujson.dumps(data)
        return retValue
    except:
        return None

# Sensing message to MQTT server
def send_topic(topicObject, topicName):
    print(topicObject)
    try:
        client.publish(topic=topicName, msg=topicObject)
        print("DONE")
    except Exception as e:
        print("FAILED")
        # We must add error hadling here if WiFi being unavailable here


# WiFi Connection
try:
    ip = wifiConnection.connect()
except KeyboardInterrupt:
    print("Keyboard interrupt")

# Connecting to MQTT server
try:
    client = MQTTClient(client_id=config.MQTT_CLIENT_ID, server=config.MQTT_SERVER, port=config.MQTT_PORT, user=config.MQTT_USER, password=config.MQTT_KEY)
    time.sleep(0.1)
    client.connect()
    print("Connected to %s" % (config.MQTT_SERVER))
except Exception as error:
    sys.print_exception(error, sys.stderr)
    print("Could not establish MQTT connection")
    wifiConnection.disconnect()
    print("Disconnected from WiFi.")

# Keyboard interrupt handler
def exceptionHandler(e):
    if e is KeyboardInterrupt:
        print("Keyboard interrupt")
    else:
        print("MQTT Brocker does not work or WiFi issues")

# Publishing a random value between 18 and 35 as "indoorTemp" to the MQTT broker 
while True:
    try:
        tempObj = build_json("indoorTemp", random.randint(18, 35))
        send_topic(tempObj, config.MQTT_TEMPERATURE_FEED)
        time.sleep(2)
    except Exception as e:
        exceptionHandler(e)
        break