import cv2
import numpy as np

imgOG = cv2.imread('Lincoln_from_penny.png',0)
kernel1 = np.ones((3,3),np.uint8)
 
erosion = cv2.erode(imgOG,kernel1,iterations = 1)
border = imgOG - erosion

cv2.imshow('Imagen Original',imgOG)
cv2.imshow('Borde',border)
cv2.waitKey(0)