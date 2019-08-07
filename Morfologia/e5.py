import cv2
import numpy as np

img = cv2.imread('fingerprint.png',0)
kernel1 = np.ones((3,3),np.uint8)
kernel2 = np.ones((2,2),np.uint8)
kernelopen = np.ones((2,2),np.uint8)
kernelclose = np.ones((4,3),np.uint8)

erosion = cv2.erode(img,kernel1,iterations = 1)
dilation = cv2.dilate(img,kernel2,iterations = 1)
closing = cv2.erode(dilation,kernelclose,iterations = 1)
opening = cv2.dilate(erosion,kernelopen,iterations = 1)
im1 = cv2.dilate(opening,kernel2,iterations = 1)
im2 = cv2.erode(im1,kernel2,iterations = 1)
cv2.imshow('im1',im1)
cv2.imshow('im2',im2)
cv2.waitKey(0)