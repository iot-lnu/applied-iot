from machine import Pin
import time

led = Pin("LED", Pin.OUT)       # Set led pin as outpu
push_button = Pin(27, Pin.IN)   # Set push button pin as input (It is connected to PULL_UP resistor
                                # and the default value is without pushing it is True)

while True:
    button_state = push_button.value()      # Get button state

    if button_state == False:   # If push_button pressed
      led.on()                  # Led will turn ON
    else:                       # If push_button not pressed
      led.off()                 # Led will turn OFF
