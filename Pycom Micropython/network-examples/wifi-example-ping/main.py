from network import WLAN
import machine
from uping import ping
wlan = WLAN(mode=WLAN.STA)

nets = wlan.scan()
for net in nets:
    if net.ssid == 'mySSID':
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, 'myPassword'), timeout=5000)
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        break

ping("google.com")