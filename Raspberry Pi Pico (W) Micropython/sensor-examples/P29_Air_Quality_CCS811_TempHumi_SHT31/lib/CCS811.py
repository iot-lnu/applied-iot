"""
CCS811 Air Quality Sensor Example Code
Author: Jiemde ( jiemde@live.be)
Sensiot
Date: November 2017
License: This code is public domain
Based on Sparkfuns Example code written by Nathan Seidle
Read the TVOC and CO2 values from the LGAQS HT11 module ( CCS811 + Si7021 )
A new sensor requires at 48-burn in. Once burned in a sensor requires
20 minutes of run in before readings are considered good.
Tested on WiPY2
"""

from machine import I2C
import time

# default address
CCS811_ADDR = const(0x5B)

# Commands
CCS811_STATUS = const(0x00)
CCS811_MEAS_MODE = const(0x01)
CCS811_ALG_RESULT_DATA = const(0x02)
CCS811_RAW_DATA = const(0x03)
CCS811_ENV_DATA = const(0x05)
CCS811_NTC = const(0x06)
CCS811_THRESHOLDS = const(0x10)
CCS811_BASELINE = const(0x11)
CCS811_HW_ID = const(0x20)
CCS811_HW_VERSION = const(0x21)
CCS811_FW_BOOT_VERSION = const(0x23)
CCS811_FW_APP_VERSION = const(0x24)
CCS811_ERROR_ID = const(0xE0)
CCS811_APP_START = const(0xF4)
CCS811_SW_RESET = const(0xFF)

# CCS811_REF_RESISTOR = const(100000)

class CCS811(object):
    """ CCS811 gas sensor driver. """

    def __init__(self, i2c=None, addr=CCS811_ADDR):
        self.i2c = i2c
        self.addr = addr
        self.tVOC = 0
        self.CO2 = 0

        # Check if sensor is vailable at i2c bus address
        devices = i2c.scan()
        if self.addr not in devices:
            raise ValueError('CCS811 not found. Please check wiring. Pull nWake to ground.')
        """########################################################################
        # See figure 22 in datasheet: Bootloader Register Map
        # Check HW_ID register (0x20) - correct value 0x81
        hardware_id = self.i2c.readfrom_mem(self.addr, CCS811_HW_ID, 1)
        if (hardware_id[0] != 0x81):
            raise ValueError('Wrong Hardware ID.')
        # Check Status Register (0x00) to see if valid application present-
        status = self.i2c.readfrom_mem(self.addr, CCS811_STATUS, 1)
        # See figure 12 in datasheet: Status register: Bit 4: App valid
        if not (status[0] >> 4) & 0x01:
            raise ValueError('Application not valid.')
        #######################################################################"""
        self.setup()

    def print_error(self):
        """Error code. """

        error = self.i2c.readfrom_mem(self.addr, CCS811_ERROR_ID, 1)
        message = 'Error: '

        if (error[0] >> 5) & 1:
            message += 'HeaterSupply '
        elif (error[0] >> 4) & 1:
            message += 'HeaterFault '
        elif (error[0] >> 3) & 1:
            message += 'MaxResistance '
        elif (error[0] >> 2) & 1:
            message += 'MeasModeInvalid '
        elif (error[0] >> 1) & 1:
            message += 'ReadRegInvalid '
        elif (error[0] >> 0) & 1:
            message += 'MsgInvalid '

        print(message)


    def configure_ccs811(self):

        # Check that the HW id is correct
        hardware_id = self.i2c.readfrom_mem(self.addr, CCS811_HW_ID, 1)
        # print(hardware_id)
        # See figure 22 in datasheet: Bootloader Register Map
        # Check HW_ID register (0x20) - correct value 0x81
        if (hardware_id [0] != 0x81):
            # print ("error!")
            raise ValueError('Wrong Hardware ID. Please check wiring. Pull nWake to ground.')

        if self.check_for_error():
            self.print_error()
            raise ValueError('Error at Startup.')

        if not self.app_valid():
            raise ValueError('Error: App not valid')

        # Application start. Write with no data to App_Start (0xF4)
        #self.i2c.writeto(self.addr, CCS811_APP_START)
        self.i2c.writeto(self.addr, bytearray([0xF4]))

        if self.check_for_error():
            self.print_error()
            raise ValueError('Error at AppStart.')

        # Set drive mode 1 - see Figure 13 in datasheet: Measure Mode Register (0x01)
        self.set_drive_mode(1)

        if self.check_for_error():
            self.print_error()
            raise ValueError('Error at setDriveMode.')

    def setup(self):

        print('Starting CCS811 Read')
        self.configure_ccs811()

        result = self.get_base_line()

        # print("baseline for this sensor: ")
        if result < 0x100:
            print('0')
        if result < 0x10:
            print('0')
        print('baseline for this sensor =   ', result)

    def get_base_line(self):

        b = self.i2c.readfrom_mem(self.addr, CCS811_BASELINE, 2)
        baselineMSB = b[0]
        baselineLSB = b[1]
        baseline = (baselineMSB << 8) | baselineLSB
        return baseline

    def check_for_error(self):
        value = self.i2c.readfrom_mem(self.addr, CCS811_STATUS, 1)
        # print('Value_error', value)
        # print(value[0] )

        v = ((value[0] >> 0) & 1)
        # print('V error = ', v)
        return ((value[0] >> 0) & 1)

    def app_valid(self):
        # Check Status Register (0x00) to see if valid application present-
        value = self.i2c.readfrom_mem(self.addr, CCS811_STATUS, 1)
        # print('Value', value)
        # print(value[0])

        # See figure 12 in datasheet: Status register: Bit 4: App valid
        v = ((value[0] >> 4) & 1)
        # print('V valid = ', v)
        return ((value[0] >> 4) & 1)

    # Set drive mode 1 - see Figure 13 in datasheet: Measure Mode Register (0x01)
    def set_drive_mode(self, mode):
        if mode > 4:
            mode = 4

            #   Clean_reg
        self.i2c.writeto_mem(self.addr, 0x01, bytearray([0b00011000]))
        """
        self.i2c.writeto_mem(self.addr, CCS811_MEAS_MODE, 0x00)
        time.sleep(1)

        setting = self.i2c.readfrom(self.addr, CCS811_MEAS_MODE)
        # print('Setting_start =  ', setting, setting[0])

        buf1 = setting[0] & (~(0b10000111 << 4))
        buf2 = buf1 | (mode << 4)

        self.i2c.writeto_mem(self.addr, CCS811_MEAS_MODE, bytes([buf2]))
        # i2c.writeto_mem(device, CCS811_MEAS_MODE, 0x10)"""
        time.sleep(2)


    def data_available(self):

        value = self.i2c.readfrom_mem(self.addr, CCS811_STATUS, 1)
        retValue = (value[0] >> 3) & 0x01
        # print('Ret value is: ', retValue)
        return retValue
        #return value[0] << 3

    def readSensorData(self):
        if self.data_available():
            register = self.i2c.readfrom_mem(self.addr, 0x02, 4)
            co2HB = register[0]
            co2LB = register[1]
            tVOCHB = register[2]
            tVOCLB = register[3]
            self.eCO2 = ((co2HB << 8) | co2LB)
            self.tVOC = ((tVOCHB << 8) | tVOCLB)

    def readeCO2(self):
        """ Equivalent Carbone Dioxide in parts per millions. Clipped to 400 to 8192ppm."""

        self.setup()

        if self.data_available():

            d = self.i2c.readfrom_mem(self.addr, CCS811_ALG_RESULT_DATA, 4)

            co2MSB = d[0]
            co2LSB = d[1]

            return ((co2MSB << 8) | co2LSB)

        elif self.check_for_error():
                self.print_error()


    def readtVOC(self):
        """ Total Volatile Organic Compound in parts per billion. """

        self.setup()

        if self.data_available():

            d = self.i2c.readfrom_mem(self.addr, CCS811_ALG_RESULT_DATA, 4)

            tvocMSB = d[2]
            tvocLSB = d[3]

            return ((tvocMSB << 8) | tvocLSB)

        elif self.check_for_error():
                self.print_error()

    def reset(self):
        """ Initiate a software reset. """

        seq = bytearray([0x11, 0xE5, 0x72, 0x8A])
        self.i2c.writeto_mem(self.addr, CCS811_SW_RESET, seq)

    ############################################################################
    # COPIED FROM P24 --- MUST TEST WITH TEMP AND HUMIDITY
    def put_envdata(self,humidity,temp):
        envregister = bytearray([0x00,0x00,0x00,0x00])
        envregister[0] = int(humidity) << 1
        t = int(temp//1)
        tf = temp % 1
        t_H = (t+25) << 9
        t_L = int(tf*512)
        t_comb = t_H | t_L
        envregister[2] = t_comb >> 8
        envregister[3] = t_comb & 0xFF
        self.i2c.writeto_mem(self.addr, CCS811_ENV_DATA, envregister)
        #return envregister

    # def set_environmental_data(self, hum, temp):
    #     """ use of temperature and humidity when computing eCO2 and TVOC values """
    #     # Humidity in %
    #     # T° in Celsius
    #     hum = int(humidity) << 1
    #     temp = 30.5
    #     buf = byterray([hum_perc, temp])
    #     self.i2c.writeto_mem(self.addr, CCS811_ENV_DATA, buf)
