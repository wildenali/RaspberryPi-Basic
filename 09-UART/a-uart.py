import serial
from time import sleep

# https://www.electronicwings.com/raspberry-pi/raspberry-pi-uart-communication-using-python-and-c

ser = serial.Serial("/dev/ttyS0", 9600) # Open port with baudrate

while True:
    received_data = ser.read()
    sleep(0.03)
    data_left = ser.inWaiting()     # check for remaining byte
    received_data += ser.read(data_left)
    print(received_data)
    ser.write(received_data)