import time
import pycom
from machine import enable_irq, disable_irq,  Pin

class DTHResult:
    'DHT sensor result returned by DHT.read() method'

    ERR_NO_ERROR = 0
    ERR_MISSING_DATA = 1
    ERR_CRC = 2

    error_code = ERR_NO_ERROR
    temperature = -1
    humidity = -1

    def __init__(self, error_code, temperature, humidity):
        self.error_code = error_code
        self.temperature = temperature
        self.humidity = humidity

    def is_valid(self):
        return self.error_code == DTHResult.ERR_NO_ERROR


class DTH:
    'DHT sensor (dht11, dht21,dht22) reader class for Pycom'

    #__pin = Pin('P3', mode=Pin.OPEN_DRAIN)
    __dhttype = 0

    def __init__(self, pin, sensor=0):
        self.__pin = Pin(pin, mode=Pin.OPEN_DRAIN)
        self.__dhttype = sensor
        self.__pin(1)
        time.sleep(1.0)

    def read(self):
        # pull down to low
        self.__send_and_sleep(0, 0.019)
        data = pycom.pulses_get(self.__pin,100)
        self.__pin.init(Pin.OPEN_DRAIN)
        self.__pin(1)
        #print(data)
        bits = []
        for a,b in data:
        	if a ==1 and 18 <= b <= 28:
        		bits.append(0)
        	if a ==1 and 65 <= b <= 75:
        		bits.append(1)
        #print("longueur bits : %d " % len(bits))
        if len(bits) != 40:
            return DTHResult(DTHResult.ERR_MISSING_DATA, 0, 0)
        #print(bits)
        # we have the bits, calculate bytes
        the_bytes = self.__bits_to_bytes(bits)
        # calculate checksum and check
        checksum = self.__calculate_checksum(the_bytes)
        if the_bytes[4] != checksum:
            return DTHResult(DTHResult.ERR_CRC, 0, 0)
        # ok, we have valid data, return it
        [int_rh, dec_rh, int_t, dec_t, csum] = the_bytes
        if self.__dhttype==0:		#dht11
            rh = int_rh 		#dht11 20% ~ 90%
            t = int_t 	#dht11 0..50°C
        else:			#dht21,dht22
            rh = ((int_rh * 256) + dec_rh)/10
            t = (((int_t & 0x7F) * 256) + dec_t)/10
            if (int_t & 0x80) > 0:
                t *= -1
        return DTHResult(DTHResult.ERR_NO_ERROR, t, rh)


    def __send_and_sleep(self, output, mysleep):
        self.__pin(output)
        time.sleep(mysleep)

    def __bits_to_bytes(self, bits):
        the_bytes = []
        byte = 0

        for i in range(0, len(bits)):
            byte = byte << 1
            if (bits[i]):
                byte = byte | 1
            else:
                byte = byte | 0
            if ((i + 1) % 8 == 0):
                the_bytes.append(byte)
                byte = 0
        #print(the_bytes)
        return the_bytes

    def __calculate_checksum(self, the_bytes):
        return the_bytes[0] + the_bytes[1] + the_bytes[2] + the_bytes[3] & 255
