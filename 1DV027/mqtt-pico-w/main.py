import time
import ubinascii
from umqttsimple import MQTTClient
import machine
import random



# Default  MQTT_BROKER to connect to
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
MQTT_BROKER = "io.adafruit.com"
PORT = 1883
ADAFRUIT_USERNAME = "nedamaleki"
ADAFRUIT_PASSWORD = "aio_qDKx7367kQvU9VgcSxtCiKQcSEBe"
SUBSCRIBE_TOPIC = b"led"
PUBLISH_TOPIC = b"nedamaleki/f/pet3"

# Setup built in PICO LED as Output
led = machine.Pin("LED",machine.Pin.OUT)

# Publish MQTT messages after every set timeout
last_publish = time.time()
publish_interval = 5 #5 seconds

# Received messages from subscriptions will be delivered to this callback
def sub_cb(topic, msg):
    print((topic, msg))
    if msg.decode() == "ON":
        led.value(1)
    else:
        led.value(0)


def reset():
    print("Resetting...")
    time.sleep(5)
    machine.reset()
    
# Generate dummy random temperature readings    
def get_temperature_reading():
    return random.randint(20, 50)
    
def main():
    print(f"Begin connection with MQTT Broker :: {MQTT_BROKER}")
    mqttClient = MQTTClient(CLIENT_ID, MQTT_BROKER, PORT, ADAFRUIT_USERNAME, ADAFRUIT_PASSWORD, keepalive=60)
    #mqttClient.set_callback(sub_cb) # whenever a new message comes (to picoW), print the topic and message
    mqttClient.connect()
    # mqttClient.subscribe(SUBSCRIBE_TOPIC)
    print(f"Connected to MQTT  Broker :: {MQTT_BROKER}, and waiting for callback function to be called!")
    while True:
            # Non-blocking wait for message
            # mqttClient.check_msg()
            global last_publish
            if (time.time() - last_publish) >= publish_interval:
                random_temp = get_temperature_reading()
                mqttClient.publish(PUBLISH_TOPIC, str(random_temp).encode())
                last_publish = time.time()
                print("Sent stuff...")
            time.sleep(1)


if __name__ == "__main__":
    while True:
        try:
            main()
        except OSError as e:
            print("Error: " + str(e))
            reset()