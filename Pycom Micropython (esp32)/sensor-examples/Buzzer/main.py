# https://forum.pycom.io/topic/802/example-pwm-mariobros
# Based on http://wiki.micropython.org/Play-Tone
import time
from machine import Pin,  PWM

# define frequency for each tone
B0  = 31
C1  = 33
CS1 = 35
D1  = 37
DS1 = 39
E1  = 41
F1  = 44
FS1 = 46
G1  = 49
GS1 = 52
A1  = 55
AS1 = 58
B1  = 62
C2  = 65
CS2 = 69
D2  = 73
DS2 = 78
E2  = 82
F2  = 87
FS2 = 93
G2  = 98
GS2 = 104
A2  = 110
AS2 = 117
B2  = 123
C3  = 131
CS3 = 139
D3  = 147
DS3 = 156
E3  = 165
F3  = 175
FS3 = 185
G3  = 196
GS3 = 208
A3  = 220
AS3 = 233
B3  = 247
C4  = 262
CS4 = 277
D4  = 294
DS4 = 311
E4  = 330
F4  = 349
FS4 = 370
G4  = 392
GS4 = 415
A4  = 440
AS4 = 466
B4  = 494
C5  = 523
CS5 = 554
D5  = 587
DS5 = 622
E5  = 659
F5  = 698
FS5 = 740
G5  = 784
GS5 = 831
A5  = 880
AS5 = 932
B5  = 988
C6  = 1047
CS6 = 1109
D6  = 1175
DS6 = 1245
E6  = 1319
F6  = 1397
FS6 = 1480
G6  = 1568
GS6 = 1661
A6  = 1760
AS6 = 1865
B6  = 1976
C7  = 2093
CS7 = 2217
D7  = 2349
DS7 = 2489
E7  = 2637
F7  = 2794
FS7 = 2960
G7  = 3136
GS7 = 3322
A7  = 3520
AS7 = 3729
B7  = 3951
C8  = 4186
CS8 = 4435
D8  = 4699
DS8 = 4978

# set up pin PWM timer for output to buzzer or speaker
buz = Pin("P10") # Pin Y2 with timer 8 Channel 2
tim = PWM(0, frequency=300)
ch = tim.channel(2, duty_cycle=0.5, pin=buz)

# play all tone
note = [B0, C1, CS1, D1, DS1, E1, F1, FS1, G1, GS1, A1, AS1, B1, C2, CS2, D2, DS2, E2, F2, FS2, G2, GS2, A2, AS2, B2, C3, CS3, D3, DS3, E3, F3, FS3,
G3, GS3, A3, AS3, B3, C4, CS4, D4, DS4, E4, F4, FS4, G4, GS4, A4, AS4, B4, C5, CS5, D5, DS5, E5, F5, FS5, G5, GS5, A5, AS5, B5, C6, CS6, D6,
DS6, E6, F6, FS6, G6, GS6, A6, AS6, B6, C7, CS7, D7, DS7, E7, F7, FS7, G7, GS7, A7, AS7, B7, C8, CS8, D8, DS8]


#for i in note:
#    print(i)
#    tim=PWM(0, frequency=i)
#    ch.duty_cycle(0.30)
#    time.sleep(0.3)


mario = [E7, E7, 0, E7, 0, C7, E7, 0, G7, 0, 0, 0, G6, 0, 0, 0, C7, 0, 0, G6, 0, 0, E6, 0, 0, A6, 0, B6, 0, AS6, A6, 0, G6, E7, 0, G7, A7, 0, F7, G7, 0, E7, 0,C7, D7, B6, 0, 0, C7, 0, 0, G6, 0, 0, E6, 0, 0, A6, 0, B6, 0, AS6, A6, 0, G6, E7, 0, G7, A7, 0, F7, G7, 0, E7, 0,C7, D7, B6, 0, 0]

# play Mario Bros tone example
# source from here http://www.linuxcircle.com/2013/03/31/playing-mario-bros-tune-with-arduino-and-piezo-buzzer/
for i in mario:
    if i == 0:
        ch.duty_cycle(0)
    else:
        tim=PWM(0, frequency=i)  # change frequency for change tone
        ch.duty_cycle(0.50)
    time.sleep(0.150)
