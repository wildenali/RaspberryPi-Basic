import RPi.GPIO as GPIO
import time

pin_button = 17
pin_led = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin_led, GPIO.OUT)

status_led = False
status_button_old = True

while True:
    status_button_new = GPIO.input(pin_button)

    if status_button_new == False and status_button_old == True :
        print("Tombol ditekan")
        status_led = not status_led
        time.sleep(0.2)
    
    status_button_old = status_button_new
    GPIO.output(pin_led, status_led)