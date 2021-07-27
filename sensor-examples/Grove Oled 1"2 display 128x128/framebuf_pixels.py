# corner pixels
display.fill(0)
maxw = display.width - 1
maxh = display.height - 1
display.pixel(0, 0, 15)  # TL
display.pixel(0, maxh, 15)  # TR
display.pixel(maxw, maxh, 15)  # BR
display.pixel(maxw, 0, 15)  # BL
display.show()


# diagonal line pixel by pixel (the slow way)
display.fill(0)
w = display.width
for i in range(0, w):
    display.pixel(i, i, 15)
    display.pixel(w - i, i, 15)
display.show()
