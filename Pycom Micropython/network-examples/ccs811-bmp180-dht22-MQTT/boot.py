# boot.py -- run on boot-up
from network import WLAN
import machine
import json
wlan = WLAN(mode=WLAN.STA)

with open('config.json') as f:
    config = json.load(f)

nets = wlan.scan()
for net in nets:
    if net.ssid == config['ssid']:
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, config['ssid_pass']), timeout=5000)
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        break
