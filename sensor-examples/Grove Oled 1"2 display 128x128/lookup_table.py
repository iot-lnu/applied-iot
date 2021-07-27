# greyscale lookup
display.fill(0)
for r in range(0, 16):
	display.fill_rect(0, r*6, 96, 6, r)
display.show()

# more dark shades
display.lookup([0,2,3,4,5,6,7,8,10,13,16,19,22,25,28])

# more light shades
display.lookup([0,2,5,8,11,14,16,19,22,23,24,25,26,27,28])

# steps
display.lookup([0,2,3,6,7,10,11,14,15,19,20,23,24,27,28])

# even more dark shades
display.lookup([0,2,3,4,5,6,7,8,9,10,11,12,13,20,28])

# revert to default linear scale
display.write_cmd(0xB9)
