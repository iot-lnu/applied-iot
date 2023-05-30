# scroll the framebuf down 16px
# note: does not wrap around
display.fill(0)
for i in range(10):
    display.text('line {}'.format(i), 0, i*8, 15)
display.show()
display.scroll(0,16) # framebuf.scroll
display.show()
