import cv2
import numpy as np

img = cv2.imread('donuts.png',0)
kernel = np.ones((22,22),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(img,kernel,iterations = 1)
cv2.imshow('erosion',erosion)
cv2.imshow('dilatacion',dilation)
cv2.waitKey(0)