import RPi.GPIO as GPIO
import time

pin_buzzer = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_buzzer, GPIO.OUT)

def buzz(pitch, duration):
    period = 1.0 / pitch
    delay = period / 2
    cycles = int(duration * pitch)

    for i in range(cycles):
        GPIO.output(pin_buzzer, True)
        time.sleep(delay)
        GPIO.output(pin_buzzer, False)
        time.sleep(delay)

while True:
    pitch_s = raw_input("Masukkan pitch (200 to 2000): ")
    pitch = float(pitch_s)
    duration_s = raw_input("Masukkan durasi (detik): ")
    duration = float(duration_s)
    buzz(pitch, duration)
    