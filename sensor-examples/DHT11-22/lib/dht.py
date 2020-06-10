import time
from machine import enable_irq, disable_irq

class DHTResult:
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
        return self.error_code == DHTResult.ERR_NO_ERROR


class DHT:
    'DHT sensor (dht11, dht21,dht22) reader class for Pycom'

    #  __pin = Pin('P3', mode=Pin.OPEN_DRAIN)
    __dhttype = 0

    def __init__(self, pin, sensor=0):
        self.__pin = pin
        self.__dhttype = sensor
        self.__pin(1)
        time.sleep(1.0)

    def read(self):
        # time.sleep(1)

        # send initial high
        # self.__send_and_sleep(1, 0.025)

        # pull down to low
        self.__send_and_sleep(0, 0.019)

        # collect data into an array
        data = self.__collect_input()
        # print(data)
        # parse lengths of all data pull up periods
        pull_up_lengths = self.__parse_data_pull_up_lengths(data)
        # if bit count mismatch, return error (4 byte data + 1 byte checksum)
        # print(pull_up_lengths)
        # print(len(pull_up_lengths))
        if len(pull_up_lengths) != 40:
            return DHTResult(DHTResult.ERR_MISSING_DATA, 0, 0)

        # calculate bits from lengths of the pull up periods
        bits = self.__calculate_bits(pull_up_lengths)

        # we have the bits, calculate bytes
        the_bytes = self.__bits_to_bytes(bits)
        # print(the_bytes)
        # calculate checksum and check
        checksum = self.__calculate_checksum(the_bytes)
        if the_bytes[4] != checksum:
            return DHTResult(DHTResult.ERR_CRC, 0, 0)

        # ok, we have valid data, return it
        [int_rh, dec_rh, int_t, dec_t, csum] = the_bytes
        if self.__dhttype == 0:  # dht11
            rh = int_rh  # dht11 20% ~ 90%
            t = int_t 	# dht11 0..50°C
        else:			# dht21,dht22
            rh = ((int_rh * 256) + dec_rh)/10
            t = (((int_t & 0x7F) * 256) + dec_t)/10
            if (int_t & 0x80) > 0:
                t *= -1
        return DHTResult(DHTResult.ERR_NO_ERROR, t, rh)

    def __send_and_sleep(self, output, mysleep):
        self.__pin(output)
        time.sleep(mysleep)

    def __collect_input(self):
        # collect the data while unchanged found
        unchanged_count = 0
        # this is used to determine where is the end of the data
        max_unchanged_count = 100
        last = -1
        data = []
        m = bytearray(800)  # needs long sample size to grab all the bits from the DHT # noqa
        irqf = disable_irq()
        self.__pin(1)
        for i in range(len(m)):
            m[i] = self.__pin()  # sample input and store value
        enable_irq(irqf)
        for i in range(len(m)):
            current = m[i]
            data.append(current)
            if last != current:
                unchanged_count = 0
                last = current
            else:
                unchanged_count += 1
                if unchanged_count > max_unchanged_count:
                    break
        # print(data)
        return data

    def __parse_data_pull_up_lengths(self, data):
        STATE_INIT_PULL_DOWN = 1
        STATE_INIT_PULL_UP = 2
        STATE_DATA_FIRST_PULL_DOWN = 3
        STATE_DATA_PULL_UP = 4
        STATE_DATA_PULL_DOWN = 5

        state = STATE_INIT_PULL_UP

        lengths = []  # will contain the lengths of data pull up periods
        current_length = 0  # will contain the length of the previous period

        for i in range(len(data)):

            current = data[i]
            current_length += 1

            if state == STATE_INIT_PULL_DOWN:
                if current == 0:
                    # ok, we got the initial pull down
                    state = STATE_INIT_PULL_UP
                    continue
                else:
                    continue
            if state == STATE_INIT_PULL_UP:
                if current == 1:
                    # ok, we got the initial pull up
                    state = STATE_DATA_FIRST_PULL_DOWN
                    continue
                else:
                    continue
            if state == STATE_DATA_FIRST_PULL_DOWN:
                if current == 0:
                    # we have the initial pull down,
                    # the next will be the data pull up
                    state = STATE_DATA_PULL_UP
                    continue
                else:
                    continue
            if state == STATE_DATA_PULL_UP:
                if current == 1:
                    # data pulled up, the length of this pull up
                    # will determine whether it is 0 or 1
                    current_length = 0
                    state = STATE_DATA_PULL_DOWN
                    continue
                else:
                    continue
            if state == STATE_DATA_PULL_DOWN:
                if current == 0:
                    # pulled down, we store the length of
                    # the previous pull up period
                    lengths.append(current_length)
                    state = STATE_DATA_PULL_UP
                    continue
                else:
                    continue

        return lengths

    def __calculate_bits(self, pull_up_lengths):
        # find shortest and longest period
        shortest_pull_up = 1000
        longest_pull_up = 0

        for i in range(0, len(pull_up_lengths)):
            length = pull_up_lengths[i]
            if length < shortest_pull_up:
                shortest_pull_up = length
            if length > longest_pull_up:
                longest_pull_up = length

        # use the halfway to determine whether the period it is long or short
        halfway = shortest_pull_up + (longest_pull_up - shortest_pull_up) / 2
        bits = []

        for i in range(0, len(pull_up_lengths)):
            bit = False
            if pull_up_lengths[i] > halfway:
                bit = True
            bits.append(bit)

        return bits

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
        # print(the_bytes)
        return the_bytes

    def __calculate_checksum(self, the_bytes):
        return the_bytes[0] + the_bytes[1] + the_bytes[2] + the_bytes[3] & 255
