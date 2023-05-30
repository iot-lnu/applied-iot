# 15 shades of grey
display.fill(0)
for r in range(0, 16):
    display.fill_rect(0, r*6, 96, 6, r)
display.show()
