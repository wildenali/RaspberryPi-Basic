import cv2

img = cv2.imread('myimage.jpg')

def percent_resize(ratio, image):
    h, w, c = image.shape
    return int(ratio*h), int(ratio*w)

# resize image 
h_new, w_new = percent_resize(0.5, img)
img_resize = cv2.resize(img, (w_new, h_new))  

# show image
cv2.imshow('image resize',img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()