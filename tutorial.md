# Basic setup


## Hardware





## Software

**Recommended IDE's**

[atom.io](https://atom.io/) _or_ [MS Visual Studio Code](https://code.visualstudio.com/)



## Setting up your local instances of IoT dashboard using Docker

Install [Docker](https://docs.docker.com/get-docker/) on your computer.

#### Start up a Node-Red instance on port 1880.

`docker run -d -p 1880:1880 --name node-red nodered/node-red`

[Node-Red getting started with Docker
](https://nodered.org/docs/getting-started/docker)

#### Start up a Grafana instance on port 3000.

`docker run -d -p 3000:3000 grafana/grafana`

#### And start InfluxDB on port 8086:

`docker run -d -p 8086:8086 \
      -v influxdb:/var/lib/influxdb \ 
      influxdb`

## Platforms


[Pybytes](https://pybytes.pycom.io/)


[Adafriut IO](https://io.adafruit.com/frahlg/dashboards/welcome-dashboard)

[Cayenne MyDevices](https://cayenne.mydevices.com)


[Blynk IoT](https://github.com/vshymanskyy/blynk-library-python)
Libraries for MicroPython exist.

[Ubidots (STEM edition)](https://ubidots.com/stem/). Seems to have good support for Pycom.

[Thingsboard](https://thingsboard.io/), can be run locally with [Docker](https://thingsboard.io/docs/user-guide/install/docker/).

[Thingsspeak](https://thingsspeak.com), Matlabs cloud

Not tested, seems to be free.
https://iottweet.com/

Freeboard. Used to be free, not anymore?
https://freeboard.io/

Then we have the three big players...

AWS IoT Graph
Azure IoT central
Google Clout IoT core


[MQTT brokers](https://mntolia.com/10-free-public-private-mqtt-brokers-for-testing-prototyping/), if needed for testing. No need of starting one on your own computer.



