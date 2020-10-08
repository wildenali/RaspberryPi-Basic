import cv2
import base64
import zmq
import numpy as np
import picamera
from picamera.array import PiRGBArray

# https://www.youtube.com/watch?v=ANUnJp7P_8A

IP = '192.168.3.11'

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 20
rawCapture = PiRGBArray(camera, size=(640, 480))

# bagian ini supaya web browser lain yg jaringannya sama bisa akses camera juga
context = zmq.Context() # atau coba context() dengan c kesil, kalau gagal
footage_socket = context.socket(zmq.PAIR)
footage_socket.connect('tcp://%s:5555'%IP)
print(IP)

# ini posisi untuk menetukan daerah lower dan upper untuk deteksi garisnya
linePos_1 = 380     # di posisi ke 380 pixel
linePos_2 = 430     # di posisi ke 430 pixel

# Setting warna yg mau di detect, 255 -> putih, 0 -> hitam
lineColorSet = 255

# capture camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    frame_image = frame.array

    frame_findline = cv2.cvtColor(frame_image, cv2.COLOR_BGR2GRAY)
    retval, frame_findline = cv2.threshold(frame_findline, 0, 255, cv2.THRESH_OTSU)
    frame_findline = cv2.erode(frame_findline, None, iterations=6)      # erode the noise in the picture
    colorPos_1 = frame_findline[linePos_1]
    colorPos_2 = frame_findline[linePos_2]

    try:
        lineColorCount_Pos1 = np.sum(colorPos_1 == lineColorSet)
        lineColorCount_Pos2 = np.sum(colorPos_2 == lineColorSet)

        lineIndex_Pos1 = np.where(colorPos_1 == lineColorSet)
        lineIndex_Pos2 = np.where(colorPos_2 == lineColorSet)

        if lineColorCount_Pos1 == 0:
            lineColorCount_Pos1 = 1
        if lineColorCount_Pos2 == 0:
            lineColorCount_Pos2 = 1
        
        left_Pos1 = lineIndex_Pos1[0][lineColorCount_Pos1 - 1]
        right_Pos1 = lineIndex_Pos1[0][0]
        center_Pos1 = int((left_Pos1 + right_Pos1) / 2)

        left_Pos2 = lineIndex_Pos2[0][lineColorCount_Pos2 - 1]
        right_Pos2 = lineIndex_Pos2[0][0]
        center_Pos2 = int((left_Pos2 + right_Pos2) / 2)
        
        center = int((center_Pos1 + center_Pos2) / 2)

    except:
        center = None
        pass
    
    print(center)

    try:
        cv2.line(frame_image, (left_Pos1, (linePos_1 + 30)), (left_Pos1, (linePos_1 - 30)), (255, 128, 64), 1)
        cv2.line(frame_image, (right_Pos1, (linePos_1 + 30)), (right_Pos1, (linePos_1 - 30)), (64, 128, 255), 1)
        cv2.line(frame_image, (0, linePos_1), (640, linePos_1), (255, 128, 64), 1)

        cv2.line(frame_image, (left_Pos2, (linePos_2 + 30)), (left_Pos2, (linePos_2 - 30)), (255, 128, 64), 1)
        cv2.line(frame_image, (right_Pos2, (linePos_2 + 30)), (right_Pos2, (linePos_2 - 30)), (64, 128, 255), 1)
        cv2.line(frame_image, (0, linePos_2), (640, linePos_2), (255, 128, 64), 1)

        cv2.line(frame_image, ((center - 20), int((linePos_1 + linePos_2)/2)), ((center + 20), int((linePos_1 + linePos_2)/2)), (0, 0, 0), 1)
        cv2.line(frame_image, ((center), int((linePos_1 + linePos_2)/2+20)), ((center), int((linePos_1 + linePos_2)/2-20)), (0, 0, 0), 1)
        
    except:
        pass

    encode, buffer = cv2.imencode('.jpg', frame_image)
    jpg_as_text = base64.b64encode(buffer)
    footage_socket.send(jpg_as_text)
    rawCapture.truncate(0)