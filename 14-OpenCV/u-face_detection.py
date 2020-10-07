import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

img = cv2.imread('blackpinkjennie.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# .detectMultiscale(<image>, scaleFactor, minNeighbours)
face = face_cascade.detectMultiScale(gray, 1.3, 5)

print(face)

for (x, y, w, h) in face:
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
    

cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()