import picamera
from time import sleep

camera = picamera.PiCamera()
camera.resolution = (640, 480)

print()

# start recording using pi camera
camera.start_recording("video1.h264")

# wait for video to record
camera.wait_recording(20)

# stop recording
camera.stop_recording()
camera.close()

print("Video recording stopped")