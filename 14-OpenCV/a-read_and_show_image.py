import cv2

# read image, same in matrix 
img = cv2.imread('myimage.jpg')

# show image
cv2.imshow('image',img)

#  hold image to show, exit whene signal close arise
cv2.waitKey(0)
cv2.destroyAllWindows()

# Run this file with `python3 a-read_and_show_image.py`