
# Tutorial 1: Basic setup

Today we'll walk you through the whole setup so you're up and running. 

You will:
* connect the device to the computer
* update the firmware of the device 
* Install an **IDE** on the computer
* upload an example code to the device

We'll continously update this walkthrough. **Is there anything missing or unclear, or you experience some issue? Please add a comment.** You do this by highlighting the text and then you can write a comment on the highlighted part. You need to log in/create account on hackMD first.

## 0. Prerequisites

* You've watched this brief walkthrough, at least to the firmware update part: https://www.youtube.com/watch?v=YjeQ934ar7Q (Note, you won't need to update **the expansion board firmware** if you've ordered a new one, only **the device firmware** potentially. If you got an old expansion board, please see [this guide](https://docs.pycom.io/updatefirmware/expansionboard/) on how to do it.)

**Materials**
* Pycom device (Lopy4 for most of you)
* Expansion board (3.0 or 3.1)
* USB cable
* Any computer


## 1. Connect hardware, update firmware
* [Getting started](https://docs.pycom.io/gettingstarted/)
    * [Update the firmware](https://docs.pycom.io/updatefirmware/device/)
        * Updating the firmware will make it easy to connect to Pybytes (the cloud platform that we will connect to later on) and will update your device to the latest version, but it's not essential - you can always do this later on.

**See [Issues per OS](https://hackmd.io/hMq4hSCJRIiwoeD2YKeILQ#Issues-per-OS) for specifics regarding firmware update on your OS (Operating system).**

### Issues per OS
#### Linux - Permission denied on /dev/ttyACM0
* You need to install `dialog` and `python-serial` package
* You might need to add your user the `dialout`  or `uucp` group
    * For Debian/Ubuntu based distos (a relog/reboot may be required)
        * `sudo usermod -a -G dialout $USER`
    * For Arch based distros (a relog/reboot may be required)
        * `sudo usermod -a -G uucp $USER`
    * Temporary fix
        * `sudo chmod a+rw /dev/ttyACM0`
#### macOS
After adding the `Pycom Firmware Update` app to your application folder, macOS might deny you to open the app (see figure below).
![](https://i.imgur.com/36P4mLY.png)
If this occurs, go to your Application folder (usually found in in the Finder sidebar) and right click the `Pycom Firmware Update` app and select "open".


#### Windows
The serial port is most likely the highest COM#, so if you've got a COM6 and it's the highest, it's probably there you'll connect to.

## 2. Setup on your computer
After you've connected your device to the expansion board, and connected via USB to your computer (and potentially updated your device firmware) it's time to setup your computer. 

(For a complete guide on how to Install and setup everything on **Windows** with VS Code follow this [step-by-step guide](https://hackmd.io/a1Nq_9kqR0CZBrYL1xNJDg).)

### Node.js

First you'll need to install **Node.js** on your computer (no matter what OS).
* Download installer from [here](https://nodejs.org).
* Or if you've got **Linux**/want to use a package manager: https://nodejs.org/en/download/package-manager/
**Ubuntu/debian**:
`sudo apt install nodejs`



### Integrated Development Environment
Then you'll choose an IDE; you've got **VS Code** or **Atom** to pick between, and then you'll install **Pymakr** on it. 

After that you'll connect Pymakr to the right serial port (where you inserted your USB).

#### VS Code
* [Step-by-step guide for Windows](https://hackmd.io/a1Nq_9kqR0CZBrYL1xNJDg)
* [Step-by-step guide for Linux/Ubuntu](https://hackmd.io/@lnu-iot/By-h1SRou)
* [Vscode installation](https://code.visualstudio.com/docs/setup/setup-overview)
* [Setup Pymakr for Vscode](https://docs.pycom.io/gettingstarted/software/vscode/)

#### Atom
* [Atom installation](https://flight-manual.atom.io/getting-started/sections/installing-atom/)
* [Setup Pymakr for Atom](https://docs.pycom.io/gettingstarted/software/atom/) 
    * **notes:** on step 2 it says install via `Atom > Preferences > Install` but it's via `file > settings > Install` or just press `Install a Package` on the welcome guide.



##### Known Issues
* Upon connecting your device, you might run into an issue where the connecting takes forever, see image below. This can be solved as described in [Issues per OS](#Issues-per-OS).
![](https://i.imgur.com/Namr9UN.png)
* If you have this error log when installing the pymakr plugin on Atom: 
![](https://i.imgur.com/aqprql8.png)
You'll have to do the following using [this (Visual Studio)](https://docs.microsoft.com/en-us/visualstudio/install/install-visual-studio?view=vs-2019#step-3---install-the-visual-studio-installer) and [this (Python) link ](https://www.python.org/downloads/release/python-395/):
In the error log you can see that it reads ***"You need to install the latest version of Python"***. First install Python (**OBS you'll have to check the box saying Add to PATH**) and then `Visual Studio` with the `Desktop development with C++` workload. ![](https://i.imgur.com/sew6ieZ.png)
Then maybe restart your computer and the installation of the pymakr plugin will go smoothly.
If you're interested you may read more about the issue here: [link](https://github.com/pycom/pymakr-atom/issues/249)


## 3. Make LED blink
You've already installed Pymakr in your IDE, and you've established a connection to the port.

It's time to write some code!

1. Create a new folder if you already aren't in a blank folder.
2. add a new folder called `lib`
3. Add a new file called: `main.py` outside of the `lib` folder
4. Paste this in `main.py`:
```python=
import pycom # "pycom" will be an error in your
# IDE because it's not on your computer, but on 
# the device
import time

pycom.heartbeat(False)

while True: #Forever loop
    pycom.rgbled(0xFF0000)  # Red
    time.sleep(1) #sleep for 1 second

    pycom.rgbled(0xFF3300)  # Orange
    time.sleep_ms(1000) #sleep for 1000 ms

    pycom.rgbled(0x00FF00)  # Green
    time.sleep(1)
```
5. Press "upload".
6. Wait...
7. Your device should now blink in different colours!






Feel free to play around with other colours (get hex-code [here](https://htmlcolorcodes.com/color-picker/)) and `sleep()` parameters. 







