import cv2

# read video result from camera port 0
cap = cv2.VideoCapture(0)

# Check success
if not cap.isOpened():
	raise Exception("Could not open video device")

# Read picture. ret === True on success
ret, frame = cap.read()

# close device
cap.release()

# save image
cv2.imwrite('photo--usbwebcam.jpg', frame)

# show image
cv2.imshow("Capture Photo", frame)

# hold until intrupt keyboard 
cv2.waitKey(0)
cv2.destroyAllWindows()