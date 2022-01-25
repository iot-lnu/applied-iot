from network import LoRa
import socket
import time
import pycom

# Node B

lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

pycom.heartbeat(False)

i = 0
while True:
    if s.recv(64) == b'Ping':
        s.send('Pong')
        print('Pong {}'.format(i))
        i = i+1
        pycom.rgbled(0x007f00) # green
    time.sleep(5)
    pycom.rgbled(0x7f0000)
    time.sleep(1)
