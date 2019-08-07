import cv2
import numpy as np

img = cv2.imread('donuts.png',0)
kernel1 = np.ones((3,3),np.uint8)
kernel2 = np.ones((2,2),np.uint8)
kernelopen = np.ones((2,2),np.uint8)
kernelclose = np.ones((4,3),np.uint8)

erosion = cv2.erode(img,kernel1,iterations = 1)
dilation = cv2.dilate(img,kernel2,iterations = 1)
closing = cv2.erode(dilation,kernelclose,iterations = 1)
result = 255 - closing
cv2.imshow('OG',img)
cv2.imshow('result',result)
cv2.imwrite('im3.png',result)
cv2.waitKey(0)