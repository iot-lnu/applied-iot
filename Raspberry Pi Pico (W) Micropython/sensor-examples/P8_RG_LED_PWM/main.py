from machine import Pin, PWM
import time

LED_Pin_Red = 27
LED_Pin_Green = 26
red_pwm_pin = PWM(Pin(LED_Pin_Red, mode=Pin.OUT)) 
green_pwm_pin = PWM(Pin(LED_Pin_Green, mode=Pin.OUT)) 

# Settings
red_pwm_pin.freq(1_000)
green_pwm_pin.freq(1_000)

while True:
    for duty in range(0,65_536, 5):
        red_pwm_pin.duty_u16(duty)
    for duty in range(65_536,0, -5):
        red_pwm_pin.duty_u16(duty)
    for duty in range(0,65_536, 5):
        green_pwm_pin.duty_u16(duty)
    for duty in range(65_536,0, -5):
        green_pwm_pin.duty_u16(duty)