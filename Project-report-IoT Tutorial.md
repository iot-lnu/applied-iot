# Project report - IoT Tutorial

---
**Table of Contents**

[TOC]



---


## How to write your tutorial

We have chosen to streamline your assignment as a tutorial, written in the Markdown language using a standard template (below). The main reason behind this is to make it as simple as possible, still flexible and easy to share between all classmates and other peers on the internet.

```
Information want's to be free - let's keep everything open, shall we?
```

1. Open an account at [hackmd.io](https://hackmd.io). Preferably, use your student credentials as username.
2. Write your tutorial using the template **Template** found below. 
3. - [ ] Checkboxes needs to be fulfilled!
4. Publish your tutorial, as seen in Fig. 1
5. Upload your tutourial according to instructions on the learning platform.
6. Be awesome!

![Fig_tutorial](https://i.imgur.com/tuqrijr.png "Tutorial" =300x)
Figure 1, published tutorial

The report/tutorial can be written either in English or Swedish.

## Some examples for inspiration

[GPS Car tracker with notification](https://www.instructables.com/id/GPS-Car-Tracker-With-SMS-Notification-and-Thingspe/)
[Blynk style button](https://www.instructables.com/id/Arduino-Tutorial-BLYNK-Style-Button-and-ESP-01-Rel/)
[IoT weather station](https://www.hackster.io/rijk_meurs/iot-weather-station-4c29c6)
[Mini IoT weather station](https://www.hackster.io/FunguyPro/how-to-make-an-mini-iot-weather-station-58252d)
[Distance sensor](https://community.mydevices.com/t/nodemcu-esp8266-hc-sr04/2872)


---
---
---


# Template

## Tutorial on how to build a temperature and humidity sensor

Give a short and brief overview of what your project is about.

What needs to be included:

- [ ] Title
- [ ] Your name and student credentials (xx666x)
- [ ] Short project overview
- [ ] How much time it might take to do (approximation)



### Objective

Describe why you have chosen to build this specific device. What purpose does it serve? What do you want to do with the data, and what new insights do you think it will give?

- [ ] Why you chose the project
- [ ] What purpose does it serve
- [ ] What insights you think it will give


### Material

Explain all material that is needed. All sensors, where you bought them and their specifications. Please also provide pictures of what you have bought and what you are using.

- [ ] List of material
- [ ] What the different things (sensors, wires, controllers) do - short specifications
- [ ] Where you bought them and how much they cost


> Example:
>| IoT Thing | For this         |
>| --------- | ---------------- |
>| Perhaps   | a table          |
>| is a      | jolly good idea? |
>
>In this project I have chosen to work with the Pycom LoPy4 device as seen in Fig. 1, it's a neat little device programmed by MicroPython and has several bands of connectivity. The device has many digital and analog input and outputs and is well suited for an IoT project.
>
>![LoPy!](https://pycom.io/wp-content/uploads/2018/08/lopySide-1.png =360x)
Fig. 1. LoPy4 with headers. Pycom.io


### Computer setup

How is the device programmed. Which IDE are you using. Describe all steps from flashing the firmware, installing plugins in your favorite editor. How flashing is done on MicroPython.

- [ ] Chosen IDE
- [ ] How the code is uploaded
- [ ] Steps that you needed to do for your computer. Installation of Node.js, extra drivers, etc.


### Putting everything together

How is all the electronics connected? Describe all the wiring, good if you can show a circuit diagram. Be specific on how to connect everything, and what to think of in terms of resistors, current and voltage. Is this only for a development setup or could it be used in production?

- [ ] Circuit diagram (can be hand drawn)
- [ ] *Electrical calculations


### Platform

Describe your choice of platform. If you have tried different platforms it can be good to provide a comparison.

Is your platform based on a local installation or a cloud? Do you plan to use a paid subscription or a free? Describe the different alternatives on going forward if you want to scale your idea.

- [ ] Describe platform in terms of functionality
- [ ] *Explain and elaborate what made you choose this platform 


### The code

Import your code here, and don't forget to explain what you have done!


```gherkin=

import this

def my_cool_function():
    print('not much here')

s.send(package)

# Explain your code!

```



### Transmitting the data / connectivity

How is the data transmitted to the internet? Describe the package format. All the different steps that are needed in getting the data to your end point. Explain both the code and choice of wireless protocols


- [ ] How often is the data sent? 
- [ ] Which wireless protocols did you use (WiFi, LoRa, etc ...)?
- [ ] Which transport protocols were used (MQTT, webhook, etc ...)
- [ ] *Explain how much data is sent every day.
- [ ] *Elaborate on the designb choices. That is how your choices affect the device range and battery consumption


### Presenting the data

Describe the presentation part. How is the dashboard built? How long is the data preserved in the database?

- [ ] Provide visual examples on how the dashboard looks. Pictures needed.
- [ ] How often is data saved in the database
- [ ] *Explain your choice of database.
- [ ] *Automation/triggers of the data


### Finalizing the design

Show the final results of your project. Give your final thoughts on how you think the project went. What could have been done in an other way, or even better? Pictures are nice!

- [ ] Show final results of the project
- [ ] Pictures
- [ ] *Video presentation



---
