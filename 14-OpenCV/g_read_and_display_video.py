import cv2

# load video
cap = cv2.VideoCapture('video.mp4')

# iterate for each frame in video
while(cap.isOpened()):
    
    # get image on each frame
    ret, frame = cap.read()
    if ret == True:
        # show image
        cv2.imshow('Frame',frame)
        
        # close using 'q' 
        if cv2.waitKey(25) & 0xFF == ord('q'):
              break
    else: 
        break

#close video
cap.release()
cv2.destroyAllWindows()