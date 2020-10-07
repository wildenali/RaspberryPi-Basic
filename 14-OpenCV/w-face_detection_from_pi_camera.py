import numpy as np
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

# load model
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

# activate camera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 5    # coba ganti jadi 30 atau berapa aja

rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(3)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    img = frame.array
    
    # convert frame to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # detect face
    # .detectMultisclae(<image>, scaleFactor, minNeighbours)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        # draw rectangle on detected face
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('img',img)
    
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
 
    if key == ord("q"):
           break

cv2.destroyAllWindows()
camera.close()