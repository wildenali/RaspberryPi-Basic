import RPi.GPIO as GPIO
import time

pin_button = 17
pin_led = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin_led, GPIO.OUT)

while True:
    GPIO.output(pin_led, False)
    status_button = GPIO.input(pin_button)

    if status_button == False:
        GPIO.output(pin_led, True)
        print("Tombol ditekan")
        time.sleep(1)