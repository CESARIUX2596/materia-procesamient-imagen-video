import numpy as np
import cv2

cap = cv2.VideoCapture('output.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()
    frame = frame[70:540,:1080]
    fgmask = fgbg.apply(frame)
    cv2.imshow('frame',fgmask)
    cv2.imshow('fgmask',frame)
    

    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    

cap.release()
cv2.destroyAllWindows()