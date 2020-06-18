#import CayenneLPP
import i2c_read
import lora
import struct
import time
import read_dht

lora.connect_lora()
from lora import s

# // byte 0,1 are for co2. No need of signed, and range of sensor is 400-8192.
# var co2 = (bytes[0] << 8) | bytes[1];
# // byte 2,3 are for VOC. range 0-1187de
# var voc = (bytes[2] << 8) | bytes[3];
# // byte 4,5 pressure in hPa
# var bmp_pressure = (bytes[4] << 8) | bytes[5];
# // byte 7 temp from bmp
# var bmp_temp = bytes[3];
# // byte 8 temp from dht
# var dht_temp = (bytes[2] << 8) | bytes[3];
# // byte 9 RH from dht
# var dht_RH = (bytes[2] << 8) | bytes[3];



def send_value():
    co2, voc, bmp_P, bmp_T = i2c_read.value()
    dht_T, dht_RH = read_dht.value()
    print('co2: ', co2) # two bytes
    print('voc: ', voc) # two bytes
    print('bmp P: ', bmp_P) # range of BMP180 300 as min and 1100 as max 800 range, 0,02hPa acc. Atm pressure.
    print('bmp temp: ', bmp_T) # -40  +85 range. 125 total range. one byte
    print('dht temp: ', dht_T) # one byte
    print('dht RH: ', dht_RH) # one byte
    package = (struct.pack('>H',int(co2) ) +
               struct.pack('>H',int(voc) ) +
               struct.pack('>H',int( (bmp_P-300) *(65536 / 800) ) ) +
               struct.pack('>B',int( (bmp_T+40)* (256/125) ) ) +
               struct.pack('>B',int( (dht_T+40)* (256/125) ) ) +
               struct.pack('>B',int( (dht_RH)* (256/100) ) )
               )
    s.send(package)

while True:
    send_value()
    time.sleep(30)
