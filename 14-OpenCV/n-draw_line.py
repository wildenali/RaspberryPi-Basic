import cv2

img = cv2.imread("myimage.jpg")

# draw line on image, cv2.line(<image>, (x0,y0), (xt,yt), (B, G, R), thickness)

#  horizontal line
cv2.line(img,
         (20,300),                  # start line position (x0,y0)
         (200,300),                 # end line position (xt,yt)
         (50,0,255),                # line color (B, G, R)
         3) 

# diagonal line
cv2.line(img,
         (0,0),                     # start line position (x0,y0)
         (150,150),                 # end line position (xt,yt)
         (255,0,255),               # line color (B, G, R)
         6)                         # line thickness

# vertical line
cv2.line(img,
         (230, 20),                 # start line position (x0,y0)
         (230, 300),                # end line position (xt,yt)
         (25,255,0),                # line color (B, G, R)
         9) 

cv2.imshow("myimage.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()