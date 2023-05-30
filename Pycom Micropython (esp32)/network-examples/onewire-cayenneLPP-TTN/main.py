from network import LoRa
import socket
import time
import ubinascii
import cayenneLPP
from machine import Pin
from onewire import DS18X20
from onewire import OneWire

#DS18B20 data line connected to pin P10
ow = OneWire(Pin('P10'))
temp = DS18X20(ow)

# Initialise LoRa in LORAWAN mode.
# Please pick the region that matches where you are using the device:
# Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

print("DevEUI: " + ubinascii.hexlify(lora.mac()).decode('utf-8').upper())

# create an OTAA authentication parameters

### App ID: lnu-iot-workshop
### device name: sensor01


app_eui = ubinascii.unhexlify('70B3D57ED0022279') ## app key
app_key = ubinascii.unhexlify('54B318775807C8ED3A33E323EB867E6F')


# join a network using OTAA (Over the Air Activation)
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

while not lora.has_joined():
    print('Not yet joined...')
    time.sleep(3)

print("Joined network")

# create socket to be used for LoRa communication
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
# configure data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
# make the socket blocking
# (waits for the data to be sent and for the 2 receive windows to expire)
s.setblocking(True)


lpp = cayenneLPP.CayenneLPP(size = 100, sock = s)

while True:

    temp.start_conversion()
    time.sleep(1)
    t_ = temp.read_temp_async()
    print(temp.read_temp_async())
    time.sleep(1)
    #if t_ not type(int): lpp.add_temperature(t_)
    print("DS18b20 temperature: " + str(t_))
    lpp.send(reset_payload = True)
    time.sleep(5)
