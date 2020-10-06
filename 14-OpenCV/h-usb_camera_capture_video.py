import cv2

# read video from device port 0
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

# prepare saved video
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('output.mp4', fourcc, 5.0, (640,480))

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)
    
    # save frame into video out
    out.write(frame)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()