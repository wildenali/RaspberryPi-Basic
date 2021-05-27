import RPi.GPIO as GPIO

led_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

pwm_led = GPIO.PWM(led_pin, 1000)    # 1000 Hz adalah freq
pwm_led.start(100)

while True:
    duty_s = raw_input(" Masukan nilai kecerahan (0 sampai 100): ")
    duty = int(duty_s)      # duty cycle dari 0% sampai 100%
    pwm_led.ChangeDutyCycle(duty)
