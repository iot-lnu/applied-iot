from machine import ADC, Pin
import time

# Pin setups
ldr = ADC(Pin(27))
led = Pin("LED", Pin.OUT)

while True:
    light = ldr.read_u16()
    darkness = round(light / 65535 * 100, 2)
    if darkness >= 70:
        print("Darkness is {}%, LED turned on".format(darkness))
        led.on()
    else:
        print("It is enough light, no need to turn the LED on")
        led.off()
    time.sleep(1)