# Source https://github.com/pimoroni/bme680-python
import time
from machine import Pin
from lib.bme680 import BME680
import lib.bme680 as bme680
from lib.i2c import I2CAdapter
from machine import I2C


class BME:

    def __init__(self, pins=('P9', 'P10'), calibration_time=500):
        i2c_dev = I2CAdapter(1, pins=pins, baudrate=100000)
        self.sensor = BME680(i2c_device=i2c_dev)
        self.sensor.set_humidity_oversample(bme680.OS_2X)
        self.sensor.set_pressure_oversample(bme680.OS_4X)
        self.sensor.set_temperature_oversample(bme680.OS_8X)
        self.sensor.set_filter(bme680.FILTER_SIZE_3)
        self.sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)

        self.sensor.set_gas_heater_temperature(320)
        self.sensor.set_gas_heater_duration(150)
        self.sensor.select_gas_heater_profile(0)

        self._warm_up(calibration_time)

    def _warm_up(self, calibration_time):
        start_time = time.time()
        curr_time = time.time()
        burn_in_time = calibration_time  # CHANGE THIS BACK DAIVD
        burn_in_data = []
        print('Collecting gas resistance burn-in data for', calibration_time // 60
        , 'mins and', calibration_time %60, 'seconds')
        while curr_time - start_time < burn_in_time:
            curr_time = time.time()
            if self.sensor.get_sensor_data() and self.sensor.data.heat_stable:
                gas = self.sensor.data.gas_resistance
                burn_in_data.append(gas)
                print('Gas: {0} Ohms'.format(gas))
                time.sleep(1)
        self.gas_baseline = sum(burn_in_data[-50:]) / 50.0
        # Set the humidity baseline to 40%, an optimal indoor humidity.
        self.hum_baseline = 40.0
        # This sets the balance between humidity and gas reading in the
        # calculation of air_quality_score (25:75, humidity:gas)
        self.hum_weighting = 0.25

    def get_values(self):
        if self.sensor.get_sensor_data() and self.sensor.data.heat_stable:
            gas = self.sensor.data.gas_resistance
            gas_offset = self.gas_baseline - gas

            hum = self.sensor.data.humidity
            hum_offset = hum - self.hum_baseline

            # Calculate hum_score as the distance from the hum_baseline.
            if hum_offset > 0:
                hum_score = (100 - self.hum_baseline - hum_offset)
                hum_score /= (100 - self.hum_baseline)
                hum_score *= (self.hum_weighting * 100)

            else:
                hum_score = (self.hum_baseline + hum_offset)
                hum_score /= self.hum_baseline
                hum_score *= (self.hum_weighting * 100)

            # Calculate gas_score as the distance from the gas_baseline.
            if gas_offset > 0:
                gas_score = (gas / self.gas_baseline)
                gas_score *= (100 - (self.hum_weighting * 100))

            else:
                gas_score = 100 - (self.hum_weighting * 100)

            # Calculate air_quality_score.
            air_quality_score = hum_score + gas_score

            return self.sensor.data.temperature, hum, self.sensor.data.pressure, air_quality_score
