import pycom

pycom.heartbeat(False)


def off: pycom.rgbled(0x0000)
def green: pycom.rgbled(0x007f00) # green for recieved
def blue: pycom.rgbled(0x2186B9) # blue for sending
