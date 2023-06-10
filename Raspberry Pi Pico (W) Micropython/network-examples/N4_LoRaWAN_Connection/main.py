from machine import Pin
from machine import UART
import binascii
import time
from LoRaWAN import lora
import struct

decoded_data = ""
led = Pin(25, Pin.OUT)
ser = UART(0, 115200)  # use RPI PICO GP0 and GP1

# https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/datasheet/unit/lorawan/ASR650X%20AT%20Command%20Introduction-20190605.pdf


lora = lora(ser)

lora.init()

lora.configure("70B3D57ED005CAFE",
               "1111111111111122",
               "E4BB99BBB37EE09BFEE8EC50FD4F263C")


lora.startJoin()
print("Start Join.....")
while not lora.checkJoinStatus():
  time.sleep(0.1)
print("Join success.....")


s = struct.pack(">hh", 1, 2)
s = binascii.hexlify(s).decode("utf-8")

while True:
  lora.sendMsg(1, 1, s)
  print("Sent message...")
  time.sleep(10)

  response = lora.receiveMsg()

  if (response != ""):
    print("Received: ", end=": ")
    print(response)
