
# Sending data..

import struct

value = 42

# < little endian
# > big endian
# h short integer (2 bytes) +-32768
# H unsigned integer (2 bytes) 0-65536
# b or B . 0-255 or -128 -> 128 ..


struct.pack('<H',value)




s.send(package)
