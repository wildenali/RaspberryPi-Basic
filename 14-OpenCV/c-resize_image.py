import cv2

img = cv2.imread('myimage.jpg')

# resize image (new_widht, new_height)
img_resize = cv2.resize(img, (320, 240))  

# show image 
cv2.imshow('image resize',img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()