# https://www.programmersought.com/article/91954603004/
import time
from machine import Pin

Pin_All = [Pin(p, Pin.OUT) for p in ['P19', 'P20', 'P21', 'P22']]

# Speed ​​(ms) The larger the value, the slower the speed, the minimum value is 1.8ms
speed = 2

STEPER_ROUND = 512  # Rotation cycle (360 degrees)
ANGLE_PER_ROUND = STEPER_ROUND / 360  # Rotation 1 degree cycle
print('ANGLE_PER_ROUND:', ANGLE_PER_ROUND)


def SteperWriteData(data):
    count = 0
    for i in data:
        Pin_All[count].value(i)
        count += 1


def SteperFrontTurn():
    global speed

    SteperWriteData([1, 1, 0, 0])
    time.sleep_ms(speed)

    SteperWriteData([0, 1, 1, 0])
    time.sleep_ms(speed)

    SteperWriteData([0, 0, 1, 1])
    time.sleep_ms(speed)

    SteperWriteData([1, 0, 0, 1])
    time.sleep_ms(speed)


def SteperBackTurn():
    global speed

    SteperWriteData([1, 1, 0, 0])
    time.sleep_ms(speed)

    SteperWriteData([1, 0, 0, 1])
    time.sleep_ms(speed)

    SteperWriteData([0, 0, 1, 1])
    time.sleep_ms(speed)

    SteperWriteData([0, 1, 1, 0])
    time.sleep_ms(speed)


def SteperStop():
    SteperWriteData([0, 0, 0, 0])


def SteperRun(angle):
    global ANGLE_PER_ROUND

    val = ANGLE_PER_ROUND * abs(angle)
    if (angle > 0):
        for i in range(0, val):
            SteperFrontTurn()
    else:
        for i in range(0, val):
            SteperBackTurn()
    angle = 0
    SteperStop()


if __name__ == '__main__':
    SteperRun(360)
    # SteperRun(-180)
