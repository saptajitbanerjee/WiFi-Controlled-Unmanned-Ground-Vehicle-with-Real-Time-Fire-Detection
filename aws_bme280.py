import time
import paho.mqtt.client as mqtt
import ssl
import json

import bme280
import smbus2

import _thread
import math

def on_connect(client, userdata, flags, rc):
    print("Connected to AWS IoT: " + str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.tls_set(ca_certs='./AmazonRootCA1.pem', certfile='./device-certificate.pem.crt', keyfile='./private.pem.key', tls_version=ssl.PROTOCOL_SSLv23)
client.tls_insecure_set(True)
client.connect("ahqreojupl1kh-ats.iot.ap-south-1.amazonaws.com", 8883, 5)

port = 1
address = 0x76 # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)

def publishData(txt):
    print(txt)
    while (True):
        bme280_data = bme280.sample(bus,address)
        humidity  = bme280_data.humidity
        temperature = bme280_data.temperature
        pressure = bme280_data.pressure
        altitude = 44330 * (1.0 - math.pow(pressure / 1013.25, 0.1903))
        print('Temperature: {0:0.1f} C'.format(temperature))
        print('Humidity:    {0:0.1f} %'.format(humidity))
        print('Pressure:    {0:0.1f} hPa'.format(pressure))
        print('Altitude:    {0:0.1f} m'.format(altitude))
        client.publish("esp32/pub", payload=json.dumps({"temperature": temperature,"humidity":humidity,"pressure":pressure,"altitude":altitude}), qos=1, retain=False)
        time.sleep(60)

_thread.start_new_thread(publishData,("Spin-up new Thread...",))

client.loop_forever()