# Simple ping example between two LoRa nodes, same code can be used
# on both nodes. They are sending a Ping and if recieved they will blink Green
# when sending the Led is Blue.

from network import LoRa
import socket
import time
import pycom

pycom.heartbeat(False)
pycom.rgbled(0x0000)


lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

print('Sending a ping!')

s.send('Ping')




while True:
    if s.recv(64) == b'Ping':
        pycom.rgbled(0x007f00) # green for recieved
        time.sleep(5)
        pycom.rgbled(0x0000) # off
        print('Ping recieved!')
    time.sleep(5)
    pycom.rgbled(0x2186B9) # blue for sending
    s.send('Ping')
    time.sleep(1)
    pycom.rgbled(0x0000) # off
    time.sleep(0.1)
