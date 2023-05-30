from network import WLAN
import machine
wlan = WLAN(mode=WLAN.STA)

import keys

nets = wlan.scan()
for net in nets:
    if net.ssid == keys.ssid:
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, keys.wifi_pass), timeout=5000)
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        break
