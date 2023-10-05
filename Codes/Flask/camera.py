import cv2
import torch
import numpy as np

import smtplib
from datetime import datetime


fire_detected = False

def send_mail():
    recipientEmail = "saptajitbanerjee2002@gmail.com"
    try:
        smtpUser='jcomponentrasberrypibot@gmail.com'
        smtpPass='uisibypxedttsfsz'
        toAdd='saptajitbanerjee2002@gmail.com'
        fromAdd = smtpUser
        subject='WARNING! FIRE Detected!'
        header='To:'+toAdd+'\n'+'From:'+fromAdd+'\n'+'Subject:'+subject
        now = datetime.now()
        body='Fire has been detected at time: '+now.strftime("%m/%d/%Y, %H:%M:%S")
        print(header+'\n'+body)
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(smtpUser,smtpPass)
        print("Login Successful")
        s.sendmail(fromAdd,toAdd,header+'\n\n'+body)
        s.quit()
    except Exception as e:
        print(e)

model = torch.hub.load('/Yolov5-Fire-Detection/yolov5', 'custom', path='/Yolov5-Fire-Detection/models/best.pt', source='local') # Load The Model
#model = torch.hub.load('/Yolov5-Fire-Detection/yolov5', 'custom', path='/Yolov5-Fire-Detection/yolov5/yolov5s.pt', source='local') # Load The Model
#model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True, force_reload=True)
#model.eval()
model.conf = 0.30  # confidence threshold (0-1)

#model.iou = 0.5  # NMS IoU threshold (0-1)

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        #self.video = cv2.VideoCapture("https://rpi-stream.s3.ap-south-1.amazonaws.com/latest_frame.jpeg")
        #self.video = cv2.VideoCapture("http://192.168.94.45:8000/stream.mjpg")
        self.video = cv2.VideoCapture("https://raspberrypi-camera.at.remote.it:33000/stream.mjpg")
        ##self.video = cv2.VideoCapture("https://x5oiuzfs.connect.remote.it/stream.mjpg")
        #self.video = cv2.VideoCapture(0)
#        self.video = cv2.resize(self.video,(840,640))
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        global fire_detected
        success, image = self.video.read()
        
        if not success:
            print("Failed to read frame from the camera or video file.")
            return None  # Return None when there's an issue reading the frame
        
        results = model(image)
        a = np.squeeze(results.render())
        detected_objects = results.pred[0]
        
        """class_names = model.names
        num_detections = detected_objects.shape[0]
        if num_detections > 0:
            print(f"Detected {num_detections} object(s):")
            for detection in detected_objects:
                class_id = int(detection[5])  # Convert class ID to integer
                class_name = class_names[class_id]
                print(f"Class: {class_name}")
        else:
            print("No objects detected.")
        """
        if len(detected_objects) > 0 and not fire_detected:
            # Fire detected and email not sent yet
            send_mail()
            fire_detected = True
        #elif len(detected_objects) == 0:
            #fire_detected = False  # Reset the flag if no fire is detected

        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()