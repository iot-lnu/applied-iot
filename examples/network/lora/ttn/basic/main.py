from network import LoRa
import socket
import time
import ubinascii
import struct

# Initialise LoRa in LORAWAN mode.
# Please pick the region that matches where you are using the device:
# Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

print("DevEUI: " + ubinascii.hexlify(lora.mac()).decode('utf-8').upper())

# create an OTAA authentication parameters

app_eui = ubinascii.unhexlify('70B3D57ED00308AF')
app_key = ubinascii.unhexlify('D7A33EA3982661191F69341907D05842')

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

#define which port with the socket bind
s.bind(2)

#send some data
s.send(bytes([0x01,0x02]))

s.setblocking(False)
# get any data received...
data = s.recv(64)
print(data)
