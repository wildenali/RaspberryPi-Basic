import RPi.GPIO as GPIO
import time

def my_callback(channel):
    print('You passed the button')

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(18, GPIO.FALLING, callback=my_callback)

i = 0

while True:
    i = i + 1
    print(i)
    time.sleep(1)