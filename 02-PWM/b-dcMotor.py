import RPi.GPIO as GPIO
from time import sleep

pwmMotorAPin = 12
pwmMotorBPin = 13
pwmMotorCPin = 18
pwmMotorDPin = 19

# GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwmMotorAPin, GPIO.OUT)
GPIO.setup(pwmMotorBPin, GPIO.OUT)
GPIO.setup(pwmMotorCPin, GPIO.OUT)
GPIO.setup(pwmMotorDPin, GPIO.OUT)

pwmMotorA = GPIO.PWM(pwmMotorAPin, 1000)
pwmMotorB = GPIO.PWM(pwmMotorBPin, 1000)
pwmMotorC = GPIO.PWM(pwmMotorCPin, 1000)
pwmMotorD = GPIO.PWM(pwmMotorDPin, 1000)

def setup():
  pwmMotorA.start(0)
  pwmMotorB.start(0)
  pwmMotorC.start(0)
  pwmMotorD.start(0)

def loop():
  i = 0
  while True:
    pwmMotorA.ChangeDutyCycle(i)
    pwmMotorB.ChangeDutyCycle(100-i)
    pwmMotorC.ChangeDutyCycle(i)
    pwmMotorD.ChangeDutyCycle(100-i)
    i+=1
    sleep(0.1)  # 0.1 detik
    print(i)

def endprogram():
  pwmMotorA.stop()
  pwmMotorB.stop()
  pwmMotorC.stop()
  pwmMotorD.stop()
  GPIO.cleanup()

if __name__ == '__main__':
  setup()
  try:
    loop()
  except KeyboardInterrupt:
    print("Keyboard Interrupt Detected")
    endprogram()
  except ValueError:
    print("Value Error")
    endprogram()