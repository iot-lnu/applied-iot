# MicroPython logo
display.fill(0)
x = (display.width - 69) // 2
y = (display.height - 69) // 2
display.fill_rect(x+0,  y+0,  69, 69, 15)
display.fill_rect(x+15, y+15, 3,  54, 0)
display.fill_rect(x+33, y+0,  3,  54, 0)
display.fill_rect(x+51, y+15, 3,  54, 0)
display.fill_rect(x+60, y+56, 4,  7,  0)
display.show()
