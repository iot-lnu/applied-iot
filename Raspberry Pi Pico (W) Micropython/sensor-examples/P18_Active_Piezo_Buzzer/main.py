from machine import Pin
import time
 
buzzer = Pin(27, Pin.OUT)
 
while True:
    buzzer.value(1)
    print("Buzzer active...")
    time.sleep(1)
    buzzer.value(0)
    print("Buzzer inactive...")
    time.sleep(1)