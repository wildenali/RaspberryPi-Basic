import cv2

img = cv2.imread("myimage.jpg")

cv2.putText(img,
            "openCV Write Text On Image",
            (50, 80),                       # text position (x0, y0)
            cv2.FONT_HERSHEY_SIMPLEX,       # font
            0.7,                            # font scale
            (0, 255, 0),                    # color (B, G, R)
            2)                              # thickness

cv2.imshow("myimage.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()