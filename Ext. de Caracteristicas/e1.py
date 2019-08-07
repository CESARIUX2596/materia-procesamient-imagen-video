import numpy as np
import cv2 as cv2

d = 3
kernel = np.ones((d,d))
kernel = -kernel
kernel[1][1] = 8

#kernel_morph =  np.ones((2,3))
img = cv2.imread('turbine.png',0)
#convolution
out = cv2.filter2D(img, -1, kernel) 
#dilate = cv2.dilate(out,kernel_morph,iterations = 1)

#out = cv2.morphologyEx(out, cv2.MORPH_OPEN, kernel_morph)

out = cv2.medianBlur(out,3)

(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(out)
image = out.copy()

cv2.circle(image, maxLoc, 10, (255, 0, 0), 2)
cv2.imshow('out',image)
cv2.waitKey(0)