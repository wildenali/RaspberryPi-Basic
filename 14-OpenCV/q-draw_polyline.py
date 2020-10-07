import cv2
import numpy as np

img = cv2.imread("myimage.jpg")

# create array polyline corner point (xt, yt) using numpy
pts = np.array([[100,50],
                [200,20],
                [250,200],
                [30,240]], np.int32)

# draw poliline on image, cv2.polyline(<image>, array_pts[], isClosed, (B, G, R), thickness)
cv2.polylines(img, 
              [pts],         # array polyline corner point ((x0,y0), (x1,y1), ... (xt,yt))
              True,          # if set True, polyline start and end point will be connected 
              (0,0,255),     # polyline color
              3)             # polyline thickness 

# draw fill for polygon cv2.fillPoly(<image>, array_pts[], (B, G, R))
cv2.fillPoly(img, 
            [pts],          # array polyline corner point ((x0,y0), (x1,y1), ... (xt,yt))
            (0,255,255))    # polyline color



cv2.imshow("myimage.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()