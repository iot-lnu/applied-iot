from network import WLAN
import ubinascii
import constants as CONST
import machine

# WiFi Setup
client_id = ubinascii.hexlify(machine.unique_id())
print(client_id)
wlan = WLAN(mode=WLAN.STA)
wlan.connect(CONST.WIFI_SSID, auth=(WLAN.WPA2, CONST.WIFI_PASS), timeout=5000)

while not wlan.isconnected():
    machine.idle()
print('Connected to WiFi\n')
