import ssd1327

from machine import I2C, Pin
i2c = I2C(0)

display = ssd1327.SH1107_I2C(128, 128, i2c)

display.text('Hello World', 20, 20, 255)
display.show()

display.fill(0)
for y in range(0,12):
    display.text('Hello World', 0, y * 8, 15 - y)
display.show()
