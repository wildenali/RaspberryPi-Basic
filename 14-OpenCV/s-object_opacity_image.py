import cv2
import numpy as np

# Load image
img = cv2.imread('myimage.jpg')

# Initialize black image of same dimensions for drawing the rectangles
blk = np.zeros(img.shape, np.uint8)

# Draw rectangles
cv2.rectangle(blk, (100, 50), (300, 250), (255, 255, 255), -1)

# Generate result by blending both images (opacity of rectangle image is 0.25 = 25 %)
out = cv2.addWeighted(img, 1.0, blk, 0.25, 1)

cv2.imshow('Image', img)
cv2.imshow('Rects', blk)
cv2.imshow('Output', out)

cv2.waitKey(0)
cv2.destroyAllWindows()