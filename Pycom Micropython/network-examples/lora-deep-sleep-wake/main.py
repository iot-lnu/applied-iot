from network import LoRa
import socket
import time
import ubinascii
import pycom

import machine



pycom.heartbeat(False)

# Initialise LoRa in LORAWAN mode.
# Please pick the region that matches where you are using the device:
# Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
#lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.US915)

if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')
    lora.nvram_restore()


else:
    print('power on or hard reset')
    # Join LoRaWAN with OTAA

    # create an OTAA authentication parameters

    app_eui = ubinascii.unhexlify('70B3D57ED002E9E3') ## app key
    app_key = ubinascii.unhexlify('E6F70B3181C289B09B0307E5C7F6CAC4')

    # join a network using OTAA (Over the Air Activation)
    lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

    while not lora.has_joined():
        pycom.rgbled(0x7f7f00)
        print('Not yet joined...')
        time.sleep(1)
        pycom.rgbled(0x000000)
        time.sleep(3)

    print("Joined network")
    pycom.rgbled(0x00FF00) #green
    time.sleep(1)
    pycom.rgbled(0x000000) #off




# create socket to be used for LoRa communication
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
# configure data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 0)
# make the socket blocking
# (waits for the data to be sent and for the 2 receive windows to expire)

while True:
    s.setblocking(True)
    pycom.rgbled(0x445CFD)
    # send some data
    print(time.time())
    t1 = time.time()
    s.send(bytes([0x57, 0x75, 0x74]))
    print('Sent in: ', time.time()-t1, ' seconds')
    pycom.rgbled(0x000000)

    # make the socket non-blocking
    # (because if there's no data received it will block forever...)
    s.setblocking(False)

    # get any data received (if any...)
    data = s.recv(64)
    print('Downlink: ' + str(data))

    if data == b'\x01':
        pycom.rgbled(0x00FF00) #green
        time.sleep(1)
        pycom.rgbled(0x000000) #off
        time.sleep(0.5)
        pycom.rgbled(0x00FF00) #green
        time.sleep(1)
        pycom.rgbled(0x000000)
    #time.sleep(30)
    lora.nvram_save()
    machine.deepsleep(10*1000)
