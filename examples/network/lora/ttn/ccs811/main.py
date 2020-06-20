import ccs_read
import lora
import struct
import time

lora.connect_lora()
from lora import s

def send_value():
    co2, voc = ccs_read.value()
    print('co2: ', co2)
    print('voc: ', voc)
    package = struct.pack('>h',int(co2)) + struct.pack('>h',int(voc))
    s.send(package)

while True:
    send_value()
    time.sleep(30)
