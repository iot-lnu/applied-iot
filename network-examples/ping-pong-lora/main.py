from network import LoRa
import socket
import time
import pycom

# Node A

lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

pycom.heartbeat(False)
pycom.rgbled(0xff00)

i = 0
while True:
    pycom.rgbled(0x7f0000) # red
    s.send('Ping')
    print('Ping {}'.format(i))
    i= i+1
    time.sleep(1)
    pycom.rgbled(0x007f00) # green
    time.sleep(5)
