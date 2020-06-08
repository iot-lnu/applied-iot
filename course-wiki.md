# Course Wiki

The course wiki for 1DT305 Tillämpad IoT.


## Helper staff

The following students are available for technical support during the course.

- Viktor Lundgren @ Slack, vl222hu@student.lnu.se




## Common problems during setup

### Windows
1. Updating Expansin board
    * Some people have troubles updating firmware on Windows. The problem can vary but common suggestions are the followng:
        * update a board without a pycom device attached to it
        * there are two modes a device can be in DFU bootloader (update mode)	Application firmware (normal mode). Update it only when it is in update mode. To get into the update mode you need to push ***S1***  button before powering the device.Then power it up and wait 1 second after. You will have only a couple of seconds in this mode after that the device will return into ***normal mode***
        * try to understand the instructions on [Update Firmware page](https://docs.pycom.io/pytrackpysense/installation/firmware/) rather then blindly follow it. There are some things you may be willing to know in advance. Besides some steps can be not that obvious 
        * [Another related troubleshooting link](https://forum.pycom.io/topic/3148/expansion-board-v3-0-doesn-t-go-in-dfu-mode) 
    * If you have troubles updating or just prefer not to risk if it seems too complicated you most likely can skip updating as the device still be working fine. 




### Mac



### Linux

1. Permission problems
    * Devices usually appears as /dev/ttyACM0 files. To make it work you need to get full permisions to the file. Although setting the permisions manually will work it is naive and clumsy way of solving the problem and we don't recomend it. The correct way of solving is adding a user to a group which has permisions to the file. For Debian/Ubuntu base distributions it is usually ***dialout*** group. 
```bash
    ls -l /dev/ttyACM0 # Command to check current permissons
```


