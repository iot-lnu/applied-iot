# hello world
# repeating 8px down, getting fainter each iteration
display.fill(0)
for y in range(0,12):
    display.text('Hello World', 0, y * 8, 15 - y)
display.show()
