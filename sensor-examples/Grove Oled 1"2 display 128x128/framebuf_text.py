# some text
display.fill(0)
display.text('Seeed Studio',0,0,15)
display.text('Grove OLED',0,10,5)
display.text('SSD1327',0,20,15)
display.text('96x96 with',0,30,5)
display.text('15 shades of',0,40,15)
display.text('grey using',0,50,5)
display.text('GS4_HMSB',0,60,15)
display.text('MicroPython',0,70,5)
display.text('v1.14',0,80,15)
display.show()


# greyscale ascii
display.fill(0)
for i in range(32,128):
    j = (i - 32)
    x = (j % 12) << 3
    y = (j // 12) << 3
    display.text(chr(i), x, y, 1 + (i % 15))
display.show()
