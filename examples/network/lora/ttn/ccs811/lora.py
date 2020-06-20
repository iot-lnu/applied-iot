from network import LoRa
import socket
import time
import ubinascii
import keys
import pycom
pycom.heartbeat(False)

# Initialise LoRa in LORAWAN mode.
# Please pick the region that matches where you are using the device:
# Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

print("DevEUI: " + ubinascii.hexlify(lora.mac()).decode('utf-8').upper())

# create an OTAA authentication parameters

app_eui = ubinascii.unhexlify(keys.APP_EUI) ## app key
app_key = ubinascii.unhexlify(keys.APP_KEY)

def connect_lora():
    # join a network using OTAA (Over the Air Activation)
    lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
    while not lora.has_joined():
        print('Not yet joined...')
        pycom.rgbled(0xcc00ff)
        time.sleep(3)
        pycom.rgbled(0x000000)
        time.sleep(0.5)

    print("Joined network")
    for n in range(3):
        pycom.rgbled(0x2bff00)
        time.sleep(1)
        pycom.rgbled(0x000000)
        time.sleep(0.5)

    # create a LoRa socket
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

    # set the LoRaWAN data rate
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
