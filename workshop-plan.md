# Workshop plan
###### tags: `planning`

## Introducing ourselves
* Ruslan
* Amer
* Osama

## Available IDE 
 * [Visual Studio Code] (https://code.visualstudio.com/)
 * [Atom] (https://atom.io/)
 * Question - What do you use/prefer

## Installing pymakr Addons
 * [VS Code] https://docs.pycom.io/pymakr/installation/vscode/
 * [Atom] - https://docs.pycom.io/pymakr/installation/atom/

## Connecting device
 * [Hardware setup](https://docs.pycom.io/gettingstarted/connection/lopy4/)
 * Windows 8, 10
All our products will work out of the box for Windows 8/10/+.
 * [Windows 7 Drivers](https://docs.pycom.io/gettingstarted/installation/drivers)
 * [Linux users - permisions](https://docs.pycom.io/gettingstarted/installation/drivers)
     ```bash
     ls -l /dev/ttyACM0
     ```
* macOS
On macOS you shouldn’t need to do anything special to get our device to work.



* [Connect LoPy to Extension Board](https://docs.pycom.io/gettingstarted/connection/lopy4/) 
 * Connect device via USB

## Hardware upgrade

[Update Firmware, Pycom](https://docs.pycom.io/gettingstarted/installation/firmwaretool/)

## Problems solving and Questions
 * Any problems so far? 

## Hello World Application
```python
print(“Hello World)”

```

## Blink Application 

import pycom
import time
pycom.heartbeat(False)

```python

while True:
    pycom.rgbled(0xFF0000)  # Red
    time.sleep(1)
    pycom.rgbled(0xFF00FF)  # MAGNETTA
    time.sleep(1)
    pycom.rgbled(0x0000FF)  # Blue
    time.sleep(1)
```


## Problems solving and Questions
 * Any problems so far? 


## If time permits
Connecting Electrokit sensors



