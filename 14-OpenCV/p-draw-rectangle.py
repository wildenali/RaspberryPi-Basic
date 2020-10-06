import cv2

img = cv2.imread("myimage.jpg")


# draw rectangle on image, cv2.rectangle(<image>, (x0,y0), (xt,yt), (B, G, R), thickness)
# (x0,y0) : Vertex of the rectangle, 
# (xt,yt) : Vertex of the rectangle opposite (x0,y0) 

cv2.rectangle(img,
              (15,25),    # Vertex of the rectangle (top-left-corner rectangle)
              (200,150),  # Vertex of the rectangle opposite (bottom-right-corner rectangle)
              (0,0,255),  # rectangle color
              3)          # rectangle thickness

cv2.rectangle(img,
              (210,50),   # Vertex of the rectangle (top-left-corner rectangle)
              (270,270),  # Vertex of the rectangle opposite (bottom-right-corner rectangle)
              (0,200,255),# rectangle color
              -1)         # rectangle thickness, 
                          # jika di set -1, maka circle color akan digunakan untuk fill color

cv2.imshow("myimage.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()