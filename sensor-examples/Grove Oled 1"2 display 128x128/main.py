import ssd1327


# or using Hardware I2C
from machine import I2C, Pin
i2c = I2C(0) # TinyPICO sda=19, scl=18

#display = ssd1327.WS_OLED_128X128(i2c)  # Grove OLED Display
display = ssd1327.SH1107_I2C(128, 128, i2c)  # WaveShare, Zio Qwiic

display.text('Hello World', 20, 20, 255)
display.show()

display.fill(0)
for y in range(0,12):
    display.text('Hello World', 0, y * 8, 15 - y)
display.show()
