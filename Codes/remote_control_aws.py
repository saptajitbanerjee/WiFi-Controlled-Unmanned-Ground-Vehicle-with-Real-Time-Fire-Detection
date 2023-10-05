import paho.mqtt.client as mqtt
import json
import time

# Raspberry Pi GPIO Configurations
from gpiozero import Motor

flmotor = Motor(forward=9, backward=10)
frmotor = Motor(forward=11, backward=12)
blmotor = Motor(forward=16, backward=17)
brmotor = Motor(forward=13, backward=18)

Request = None

def left():
    #print('Left ...')
    flmotor.forward()
    frmotor.backward()
    #blmotor.backward()
    blmotor.forward()
    brmotor.backward()

def right():
    #print('Right ...')
    flmotor.backward()
    frmotor.forward()
    blmotor.backward()
    brmotor.forward()

def forward():
    #print('Forwarding ...')
    flmotor.forward()
    frmotor.forward()
    blmotor.forward()
    brmotor.forward()

def reverse():
    #print('Reversing ...')
    flmotor.backward()
    frmotor.backward()
    blmotor.backward()
    brmotor.backward()

def stop():
    #print('Stopping ...')
    flmotor.stop()
    frmotor.stop()
    blmotor.stop()
    brmotor.stop()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribe to the topic when connected to the broker
    client.subscribe("esp32/sub")  # Replace with the topic you want to subscribe to

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        print("Received message: ", payload)
        if "message" in payload:
            # Do something with the received data, e.g., control the LED
            message = payload["message"]
            print(message)
            if(message=="forward"):
                forward()
            if(message=="reverse"):
                reverse()
            if(message=="left"):
                left()
            if(message=="right"):
                right()
            if(message=="stop"):
                stop()
            # Your code to use the temperature and humidity data here, if needed
    except Exception as e:
        print("Error processing message:", e)

# Create a client instance
client = mqtt.Client()

# Set the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker (replace the broker address and port with your AWS IoT endpoint)
client.connect("ahqreojupl1kh-ats.iot.ap-south-1.amazonaws.com", 8883)  # Use the correct port (default is 8883 for MQTT over TLS)

# Set up the TLS certificates
client.tls_set(ca_certs="./AmazonRootCA1.pem",
               certfile="./device-certificate.pem.crt",
               keyfile="./private.pem.key")

# Start the loop to process MQTT messages
client.loop_start()

try:
    while True:
        # Your main loop code here, if needed
        time.sleep(1)

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
