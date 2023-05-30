# random pixels (slow)
# note: urandom not available on all devices
import uos
for i in range(0,256):
    x = uos.urandom(1)[0] // 2
    y = uos.urandom(1)[0] // 2
    display.pixel(x,y,15)
    display.show()
