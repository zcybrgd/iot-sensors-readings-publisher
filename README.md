# iot-sensors-readings-publisher
This repo contains python scripts that retrieves multiple sensors readings via a Raspberry Pi 4, and then publish the values into the adequate topics of the MQTT broker, which will later going to be retrieved into our VPS were our backend (the subscriber) is deployed

## Hierarchy of MQTT Topics

<location>/<pond_id>/<sensor_type>/<sensor_id> or <pond_id>/<sensor_type>/<sensor_id>

Exemple : azazga-coordinates/tank1/temperature/ruvviSensor /tank1/temperature/ruvviSensor 

## Set Up Raspberry Pi 4 as an MQTT publisher
now we are going to talk about the steps we proceeded to set up the raspberry pi 4 as an mqtt publisher
```bash
     sudo apt update
     sudo apt install python3-pip
     pip3 install paho-mqtt
```
These commands will install `paho-mqtt`, a Python library that enables MQTT functionality, allowing the Raspberry Pi to publish sensor data to an MQTT broker.

~~ to see later, a script that does it all so we don't have to do it manually

## Add MQTT configuration for a reading script
Now we have, let's say a script, that reads temperature values from the sensor, we need to add the code that can publish these values to the mqtt broker

```python
     import paho.mqtt.client as mqtt
     # MQTT Broker details
     MQTT_BROKER = "external-ip-adress-broker-host"
     MQTT_PORT = 1883  
     MQTT_TOPIC = "tank1/pond123/temperature/sensor456" # mqtt topic we want to publish in

     # Initialize MQTT Client
     client = mqtt.Client()
     client.connect(MQTT_BROKER, MQTT_PORT, 60)

     def send_to_mqtt(value): 
     client.publish(MQTT_TOPIC, value)
     print(f"Published {value} to MQTT topic {MQTT_TOPIC}")
```
This script establishes a connection to the MQTT broker, and the `send_to_mqtt()` function is used to publish sensor readings to the specified topic.

## Subscribing to MQTT Topics
Once the data is published by the Raspberry Pi, it can be retrieved by subscribing to the corresponding topic. To do this, we have to  subscribe to the topic using a service like `mosquitto_sub` or any MQTT client:

```bash 
     mosquitto_sub -h your-mqtt-broker-ip -t "tank1/pond123/temperature/sensor456"
```

This allows us to monitor the data published by the Raspberry Pi in real time from the main server.

## Running the script from a separate Ip adress
In our case, we ran the sensor reading and publishing script under a different ip address on the Raspberry Pi to allow detection from anywhere. This was made possible by configuring the MQTT broker to allow all users in the configuration file.

```bash
     python3 sensor_reading_script.py
```
The script successfully reads data from the sensors and publishes it to the MQTT broker, with the server subscribing to the respective topics to process the data.