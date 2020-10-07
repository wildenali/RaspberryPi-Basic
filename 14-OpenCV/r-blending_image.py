import cv2 as cv2

# read two image (different size)
img1 = cv2.imread('picamera-photo.jpg')
img2 = cv2.imread('myimage.jpg')

# check image size
h1, w1, c1 = img1.shape
h2, w2, c2 = img2.shape
height_ratio = h1/h2

# resize and crop second image until img2.shape = img1.shape
img2 = cv2.resize(img2, (0,0), fy=height_ratio, fx=1)[:,:w1]


# blend image using cv2.addWeight(<image_1>, alpha, <image_2>, beta, gamma)
alpha = 0.5
beta = (1.0 - alpha)
blend = cv2.addWeighted(img1, alpha, img2, beta, 0.0)


cv2.imshow('blend.jpg', blend)

cv2.waitKey(0)
cv2.destroyAllWindows()