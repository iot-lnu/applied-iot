from machine import Pin,UART
import time


uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))
uart.init(bits=8, parity=None, stop=2)
led = Pin("LED", Pin.OUT)

while True:
    data_send = uart.write(b"a")

    if uart.any():
        data_recieved = uart.read()
        print ("received", str(data_recieved), "sent", data_send )
        if data_recieved== b"b":
            led.toggle()
    time.sleep(1)
    
    
    '''
    from machine import Pin,UART
import time


uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))
uart.init(bits=8, parity=None, stop=2)
led = Pin("LED", Pin.OUT)

while True:
    data_send = uart.write(b"b")

    if uart.any():
        data_recieved = uart.read()
        print ("received", str(data_recieved), "sent", data_send )
        if data_recieved== b"a":
            led.toggle()
    time.sleep(1)
    
    '''