# draw some lines using framebuf

# from top left
display.fill(0)
x1 = 0
y1 = 0
y2 = display.height - 1
for x2 in range(0, display.width + 1, 8):
    display.line(x1, y1, x2, y2, 15)
    display.show()
x2 = display.width - 1
for y2 in range(0, display.height + 1, 8):
    display.line(x1, y1, x2, y2, 15)
    display.show()

# from top right
display.fill(0)
x1 = display.width - 1
y1 = 0
y2 = display.height - 1
for x2 in range(0, display.width + 1, 8):
    display.line(x1, y1, x2, y2, 15)
    display.show()
x2 = 0
for y2 in range(0, display.height + 1, 8):
    display.line(x1, y1, x2, y2, 15)
    display.show()

# from bottom left
display.fill(0)
x1 = 0
y1 = display.height - 1
y2 = 0
for x2 in range(0, display.width + 1, 8):
    display.line(x1, y1, x2, y2, 15)
    display.show()
x2 = display.width - 1
for y2 in range(0, display.height + 1, 8):
    display.line(x1, y1, x2, y2, 15)
    display.show()

# from bottom right
display.fill(0)
x1 = display.width - 1
y1 = display.height - 1
y2 = 0
for x2 in range(0, display.width + 1, 8):
    display.line(x1, y1, x2, y2, 15)
    display.show()
x2 = 0
for y2 in range(0, display.height + 1, 8):
    display.line(x1, y1, x2, y2, 15)
    display.show()
