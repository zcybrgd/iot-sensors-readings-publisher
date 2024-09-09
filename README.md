# iot-sensors-readings-publisher
This repo contains python scripts that retrieves multiple sensors readings via a Raspberry Pi 4, and then publish the values into the adequate topics of the MQTT broker, which will later going to be retrieved into our VPS were our backend (the subscriber) is deployed

## Hierarchy of MQTT Topics

<location>/<pond_id>/<sensor_type>/<sensor_id> or <pond_id>/<sensor_type>/<sensor_id>

exemple : azazga-coordinates/tank1/temperature/ruvviSensor /tank1/temperature/ruvviSensor 

## Set Up Raspberry Pi 4 as an MQTT publisher
now we are going to talk about the steps we proceeded to set up the raspberry pi 4 as an mqtt publisher
```bash
     sudo apt update
     sudo apt install python3-pip
     pip3 install paho-mqtt
```
~~ to see later, a script that does it all so we don't have to do it manually

## Add MQTT configuration for a reading script
now we have let's say a script that reads temperature values from the sensor, we need to add the code that can publish these values to the mqtt broker

```python
     import paho.mqtt.client as mqtt
     # Broker details
     MQTT_BROKER = "external-ip-adress-broker-host"
     MQTT_PORT = 1883  
     MQTT_TOPIC = "tank1/pond123/temperature/sensor456" # mqtt topic we want to publish in
```
