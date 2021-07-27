# optical illusion - are the lines crooked?
display.fill(15)
sq = 12    # square size
seq = 100  # this magic number gives repititions of sequence 0,1,2,1... repeat
for y in range(0, display.height, sq+1):
    offset = int(round(((seq & 3) / 3) * sq))
    seq >>= 2
    if seq == 0:
        seq = 100
    for x in range(0, display.width, sq*2):
        display.fill_rect(x + offset, y, sq, sq, 0)
    display.hline(0, y + sq, display.width, 6)
display.show()
