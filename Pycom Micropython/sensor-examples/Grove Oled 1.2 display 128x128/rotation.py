# rotate 180 degrees
# need to call show after rotating as rotating only sets the remapping bits on the remap and offset registers
# show repopulates the gddram in the new correct order
display.rotate(True)
display.show()

# rotate 0 degrees
display.write_cmd(ssd1327.SET_DISP_OFFSET) # 0xA2
display.write_cmd(128 - display.height)
display.write_cmd(ssd1327.SET_SEG_REMAP) # 0xA0
display.write_cmd(0x51)
display.show()

# rotate 0 degrees (flip horizontal)
display.write_cmd(ssd1327.SET_DISP_OFFSET) # 0xA2
display.write_cmd(128 - display.height)
display.write_cmd(ssd1327.SET_SEG_REMAP) # 0xA0
display.write_cmd(0x52)
display.show()

# rotate 180 degrees
display.write_cmd(ssd1327.SET_DISP_OFFSET) # 0xA2
display.write_cmd(display.height)
display.write_cmd(ssd1327.SET_SEG_REMAP) # 0xA0
display.write_cmd(0x42)
display.show()

# rotate 180 degrees (flip horizontal)
display.write_cmd(ssd1327.SET_DISP_OFFSET) # 0xA2
display.write_cmd(display.height)
display.write_cmd(ssd1327.SET_SEG_REMAP) # 0xA0
display.write_cmd(0x41)
display.show()

# rotate 0 degrees
display.rotate(False)
display.show()
