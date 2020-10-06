import cv2

img = cv2.imread('myimage.jpg')

# define center of image
h, w, c = img.shape
center = (w // 2, h // 2)

# get matrix otation M
M = cv2.getRotationMatrix2D(center, -45, 1.0)

# create rotated image
rotated = cv2.warpAffine(img, M, (w, h))

cv2.imshow("OpenCV Rotation", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()