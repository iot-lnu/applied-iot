from machine import Pin
import time

def pin_handler(arg):
    print("got an interrupt in pin %s" % (arg.id()))
    time.sleep(0.1)

p_in = Pin('P10', mode=Pin.IN, pull=Pin.PULL_UP)
p_in.callback(Pin.IRQ_LOW_LEVEL, pin_handler)
