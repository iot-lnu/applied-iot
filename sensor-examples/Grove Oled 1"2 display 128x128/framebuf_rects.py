# rects using framebuf
display.fill(0)
for i in range(0, 15):
    j = 6 * i
    display.fill_rect(j, j, 12, 12, i)
    display.rect(90 - (j), j, 12, 12, i)
display.show()
