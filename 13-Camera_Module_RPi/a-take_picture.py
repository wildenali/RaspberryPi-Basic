import picamera
from time import sleep

# Create object for PiCamera class
camera = picamera.PiCamera()

# set resolution
camera.resolution = (1024, 768)
camera.brightness = 60
camera.start_preview()

# add text on image
camera.annotate_text = "Hiloow"
sleep(5)

# store image
camera.capture('/home/pi/image1.jpeg')
camera.stop_preview()