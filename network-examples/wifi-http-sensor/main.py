import read_dht
import pycom
import urequests
import time
from machine import deepsleep
import keys

url = keys.url
bearer = '?authorization=' + keys.bearer

def send_data():
    try:
        dht_T, dht_RH = read_dht.value()
        print('sending data ...',dht_T,dht_RH)
        urequests.post(url+bearer,json={"dht_T":dht_T, "dht_RH":dht_RH})
    except (OSError, NameError, ValueError, TypeError):
        pass

send_data()
#deepsleep(300*1000)
