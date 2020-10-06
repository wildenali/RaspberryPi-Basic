import cv2

img = cv2.imread("myimage.jpg")


# circle outline
cv2.circle(img,
           (65, 65),         # circle center position (x_center,y_center)
           55,               # circle radius (pixel)
           (0,255,150),      # circle color
           5)                # outline circle thicknes

# circle fill
cv2.circle(img,
           (65, 250),         # circle center position (x_center,y_center)
           55,                # circle radius (pixel)
           (0,50,250),        # circle color
           -1)                # outline circle thicknes, 
                             # jika di set -1, maka circle color akan digunakan untuk fill color


# draw circle in same location (fill & outline)
# circle outline
cv2.circle(img,
           (250,250),        # circle center position (x_center,y_center)
           55,               # circle radius (pixel)
           (0,255,0),        # circle color
           3)                # outline circle thicknes

# circle fill
cv2.circle(img,
           (250,250),         # circle center position (x_center,y_center)
           55,               # circle radius (pixel)
           (0,255,255),      # circle color
           -1)               # outline circle thicknes, 
                             # jika di set -1, maka circle color akan digunakan untuk fill color


    
cv2.imshow("myimage.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()