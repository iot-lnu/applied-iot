# Basic setup


## Hardware

## Software

Recommended IDE

atom.io
MS Visual Studio Code

Docker CE

## Setting up your local instances of IoT dashboard using Docker

Install Docker-CE on your computer.

Run the following commands:

### Start up a Node-Red instance on port 1880.

> docker run -d -p 1880:1880 --name node-red nodered/node-red

[https://nodered.org/docs/getting-started/docker
](https://nodered.org/docs/getting-started/docker)

### Start up a Grafana instance on port 3000.

> docker run -d -p 3000:3000 grafana/grafana



And start InfluxDB on port 8086:

> docker run -d -p 8086:8086 \
      -v influxdb:/var/lib/influxdb \
      influxdb
