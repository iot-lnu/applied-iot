from machine import PWM
from time import sleep

pwm = PWM(0,frequency=50)  # use PWM timer 0, with a frequency of 50Hz
pwm_c = pwm.channel(0,pin='P8', duty_cycle=1)

while True:
    pwm_c.duty_cycle(0.097)
    sleep(1)
    pwm_c.duty_cycle(0.043)
    sleep(1)
    pwm_c.duty_cycle(0.097)

