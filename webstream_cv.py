# Part 01 using opencv access webcam and transmit the video in HTML
import cv2
import  pyshine as ps #  pip3 install pyshine==0.0.9
import numpy as np
import threading
from datetime import datetime

#import sys
#import os

#sys.path.append("DHT/Adafruit_Python_DHT/examples")
##import google-auth.json
#print(DHT_PIN)


PAGE="""\
    <html>
    <head>
    <style>
    h1{font-weightLbold;font-family:Verdana;color:white;font-size:25px;margin-bottom:10px}
    body{background-color:lightblue}
    img{border:white solid 5px}
    #text{color:white;font-family:Verdana;font-weight:bold;font-size:20px}
    </style>
    <title>Raspberry Pi - Surveillance Camera</title>
    </head>
    <body>
    <center><h1>Raspberry Pi - Surveillance Camera</h1></center>
    <center><img src="stream.mjpg" width="960" height="560"></center>
    </body>
    </html>
"""

def main():
    StreamProps = ps.StreamProps
    StreamProps.set_Page(StreamProps,PAGE)
    address = ('192.168.225.45',8000) # Enter your IP address 
    try:
        StreamProps.set_Mode(StreamProps,'cv2')
        capture = cv2.VideoCapture(0)
        #detect_fire_function(capture);
        capture.set(cv2.CAP_PROP_BUFFERSIZE,4)
        capture.set(cv2.CAP_PROP_FRAME_WIDTH,960)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT,560)
        capture.set(cv2.CAP_PROP_FPS,12)
        StreamProps.set_Capture(StreamProps,capture)
        StreamProps.set_Quality(StreamProps,90)
        server = ps.Streamer(address,StreamProps)
        print('Server started at','http://'+address[0]+':'+str(address[1]))
        server.serve_forever()
    except KeyboardInterrupt:
        capture.release()
        server.socket.close()
        
if __name__=='__main__':
    main()