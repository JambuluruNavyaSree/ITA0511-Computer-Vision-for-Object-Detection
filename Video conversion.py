import cv2
import numpy as np
cap = cv2.VideoCapture("C:/Users/Kulasekar/Videos/King_Of_Kotha_(2023)_Telugu_720p.mkv")
if (cap.isOpened()== False):
    print("Error opening video file")
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(250) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
