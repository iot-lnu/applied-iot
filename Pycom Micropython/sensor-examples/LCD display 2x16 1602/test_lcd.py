'''
    I2C LCD1602 demo
    Author: shaoziyang
    Date:   2018.2
    http://www.micropython.org.cn

    =======================================

    Modified by: Sotirios Tsivras
    1. Save the LCD1602.py file to your lib folder
    2. Connect sda with P11,  scl with P12 and gnd to gnd
    3. Connect VCC to Vin (it needs 5V)

'''
from machine import I2C, Pin
from lib.LCD1602 import LCD1602
import time

sda = 'P11'
scl = 'P12'

i2c = I2C(1, pins=(sda, scl))

LCD = LCD1602(i2c)

LCD.puts("Applied IoT LNU")
n = 0
while n<5:
    LCD.backlight(1)
    LCD.puts(n, 1, 1)
    n += 1
    time.sleep(2)
    LCD.backlight(0)
    time.sleep(3)
LCD.clear()
