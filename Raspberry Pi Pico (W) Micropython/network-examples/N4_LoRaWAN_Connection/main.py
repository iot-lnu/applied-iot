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


"""
DevEUI - 64 bit end-device identifier, EUI-64 (unique)
DevAddr - 32 bit device address (non-unique)
AppEUI - 64 bit application identifier, EUI-64 (unique)
"""
DEV_EUI = "6081F9EC955F46DF"
APP_EUI = "6081F97E7C42DE68"
APP_KEY = "F389764D6E193CB281FF32703244F97C"


lora.configure(DEV_EUI, APP_EUI, APP_KEY)


lora.startJoin()
print("Start Join.....")
while not lora.checkJoinStatus():
  time.sleep(0.1)
print("Join success!")


# https://docs.micropython.org/en/latest/library/struct.html

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