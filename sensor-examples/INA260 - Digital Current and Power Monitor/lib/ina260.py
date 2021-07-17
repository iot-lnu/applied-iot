import struct
import constants as const


class INA260:

    def __init__(self, bus, address=0x40):
        self.bus = bus
        self.address = address

    def _read(self, reg):
        """
        Read a word from the device

        Parameters
        ---------
            reg: register address

        Returns
        ------
            list of bytes as characters for struct unpack
        """
        res = self.bus.readfrom_mem(self.address, reg, 2)
        return bytearray(res)

    def voltage(self):
        """
        Returns the bus voltage in Volts
        """
        voltage = struct.unpack('>H', self._read(const.REG_BUS_VOLTAGE))[0]
        voltage *= 0.00125  # 1.25mv/bit

        return voltage

    def current(self):
        """
        Returns the current in Amps
        """
        current = struct.unpack('>H', self._read(const.REG_CURRENT))[0]
        # Fix 2's complement
        if current & (1 << 15):
            current -= 65535

        current *= 0.00125  # 1.25mA/bit

        return current

    def power(self):
        """
        Returns the power calculated by the device in Watts

        This will probably be different to reading voltage and current
        and performing the calculation manually.
        """

        power = struct.unpack('>H', self._read(const.REG_POWER))[0]
        power *= 0.01  # 10mW/bit

        return power

    def manufacturer_id(self):
        """
        Returns the manufacturer ID - should always be 0x5449
        """
        man_id = struct.unpack('>H', self._read(const.REG_MANUFACTURER_ID))[0]
        return man_id

    def die_id(self):
        """
        Returns a tuple containing the die ID and revision - should be 0x227 and 0x0.
        """
        die_id = struct.unpack('>H', self._read(const.REG_DIE_ID))[0]
        return (die_id >> 4), (die_id & 0x000F)

    def __del__(self):
        self.bus.deinit()
