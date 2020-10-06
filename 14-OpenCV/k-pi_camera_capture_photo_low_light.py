#load pi camera library 
from picamera.array import PiRGBArray
from picamera import PiCamera
from fractions import Fraction
import time
import cv2

# define PiCamera() object
camera = PiCamera(resolution=(640, 480), framerate=5)

# define raw capture object, to hold image array data 
# and wait for warming up
rawCapture = PiRGBArray(camera)
time.sleep(3)
 
#capture image
camera.capture(rawCapture, format="bgr")

# get array image from rawCapture object
img = rawCapture.array

#close camera
camera.close()

# save image
cv2.imwrite('picamera-photo_low_light.jpg', img)

#show image
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()