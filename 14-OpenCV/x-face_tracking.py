from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import sys
import imutils
from adafruit_servokit import ServoKit

#define servo object
srv = ServoKit(channels=16)

# Get user supplied values
cascPath = 'haarcascades/haarcascade_frontalface_default.xml'

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)


def pan(pan_degre) :
    srv.servo[0].angle = pan_degre

def tilt(tilt_degre) :
    srv.servo[1].angle = tilt_degre
    
# Frame Size. Smaller is faster, but less accurate.
# Wide and short is better, since moving your head
FRAME_W = 160
FRAME_H = 120

# Default Pan/Tilt for the camera in degrees.
# Camera range is from -90 to 90
cam_pan = 90
cam_tilt = 90

# Turn the camera to the default position
pan(cam_pan)
tilt(cam_tilt)

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (FRAME_W, FRAME_H)
camera.framerate = 5
rawCapture = PiRGBArray(camera)


# allow the camera to warmup
time.sleep(3)
lastTime = time.time()*1000.0

# capture frames from the camera
for image in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
    frame = image.array
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    # .detectMultisclae(<image>, scaleFactor, minNeighbours, minSize, flags)
    faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.05,
                minNeighbors=5,
                minSize=(20, 20),
                flags = cv2.CASCADE_SCALE_IMAGE
    )
    #print (time.time()*1000.0-lastTime)
    #print (" Found {0} faces!".format(len(faces)))
    lastTime = time.time()*1000.0
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


        # Correct relative to center of image
        turn_x  = float(-(x + w/2 - (FRAME_W/2)))
        turn_y  = float(y + h/2 - (FRAME_H/2))

        # Convert to percentage offset
        turn_x  /= float(FRAME_W/2)
        turn_y  /= float(FRAME_H/2)

        # Scale offset to degrees
        turn_x   *= 10 # VFOV
        turn_y   *= 10 # HFOV
        #print (turn_x)
        #print (turn_y)
        cam_pan  += turn_x
        cam_tilt += turn_y


        # Clamp Pan/Tilt to 0 to 180 degrees
        cam_pan = max(0,min(180,cam_pan))
        cam_tilt = max(0,min(180,cam_tilt))

        # Update the servos
        pan(int(cam_pan))
        tilt(int(cam_tilt))
        cv2.putText(frame, "Pan : " + str(int(cam_pan)) + " tilt: " + str(int(cam_tilt)), (20,20), 	cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), 1)
        #print ("pan :" + str(int(cam_pan - 90)), "tilt : " + str(int(cam_tilt)))

        #break

    # show the frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
 
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

cv2.destroyAllWindows()
camera.close()