from mqtt import MQTTClient
import time
import ujson
import constants as CONST

def sub_cb(topic, msg):
   print(msg)


# MQTT Setup
client = MQTTClient(client_id,
                    CONST.UBIDOTS_MQTT_URL,
                    user=CONST.UBIDOTS_TOKEN,
                    password='',
                    port=CONST.UBIDOTS_MQTT_PORT)

client.set_callback(sub_cb)
client.connect()
print('connected')


my_topic = CONST.UBIDOTS_MQTT_TOPIC + "My_Device"

payload = {}
toggled = False

while True:
    payload['lights_on'] = 1 if toggled else 0
    payload['temperature'] = 25.44
    payload['humidity'] = 39.85
    payload['lights_on'] = 0
    
    json_payload = ujson.dumps(message)
    print(json_payload)

    client.publish(topic=my_topic, msg=json_payload)

    toggled = not toggled

    client.check_msg()
    time.sleep(3)
