from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

#setup
camera = PiCamera(resolution=(640, 480), framerate=5)

# prepare saved video
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('output.mp4', fourcc, 5.0, (640,480))

rawCapture = PiRGBArray(camera)
 
time.sleep(5)
 
#iterate for each frame in camera stream 
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=False):

    #show image
    image = frame.array
    cv2.imshow("Frame", image)
    
    # save frame into video out
    out.write(image)
    
    #clean current array data in rawCapture object
    rawCapture.truncate(0)
 
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.close()
out.release()
cv2.destroyAllWindows()