# tf-luna
A simple micropython i2c library for TF-Luna LiDAR Module.

**Repo-status**: See [Implemented functions](#implemented-functions)

## Getting started

To enable i2c, connect pin 5 to GND, see [Datasheet](https://www.robotshop.com/media/files/content/b/ben/pdf/tf-luna-8m-lidar-distance-sensor-instructions-manual.pdf)

To run main.py, connect RXD/SDA to P7 and TXD/SCL to P8


| Pin & Function        | Description        |
| --------------------- | ------------------ |
| 1 VCC                 | Vin (5V)           |     
| 2 RXD/SDA             | Receiving/Data     |
| 3 TXD/SCL             | Transmitting/Clock |     
| 4 GND                 | GND                |     
| 5 Configuration Input | Ground: I2C mode <br />/3.3V: Serial port <br />Communications mode |     
| 6 Multiplexing output | Default: on/off mode output<br />I2C mode: Data availability<br />signal on but not switching value mode     |     


## Implemented functions
* Distance
* Chip temperature
* Signal Amplitude
* Set Min/Max range
* Reboot
* Reset to factory defaults
* Change sampling rate / freq

## To-Do
* Trigger mode
* Change slave address
* Tick
* Error
* UART
