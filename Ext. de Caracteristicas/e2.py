import numpy as np
import cv2 as cv2

img = cv2.imread('wirebond_mask.png',0)

d = 3
kernel_horizontal = np.ones((d,d))
kernel_horizontal = -kernel_horizontal
kernel_horizontal[0][1] = 2
kernel_horizontal[1][1] = 2
kernel_horizontal[2][1] = 2

kernel_vertical = np.ones((d,d))
kernel_vertical = -kernel_vertical
kernel_vertical[1][0] = 2
kernel_vertical[1][1] = 2
kernel_vertical[1][2] = 2

kernel_diag_pos = np.ones((d,d))
kernel_diag_pos = -kernel_diag_pos
kernel_diag_pos[0][2] = 2
kernel_diag_pos[1][1] = 2
kernel_diag_pos[2][0] = 2

kernel_diag_neg = np.ones((d,d))
kernel_diag_neg = -kernel_diag_neg
kernel_diag_neg[0][0] = 2
kernel_diag_neg[1][1] = 2
kernel_diag_neg[2][2] = 2

out1 = cv2.filter2D(img, -1, kernel_vertical) 
out2 = cv2.filter2D(img, -1, kernel_horizontal) 
out3 = cv2.filter2D(img, -1, kernel_diag_pos) 
out4 = cv2.filter2D(img, -1, kernel_diag_neg) 

cv2.imshow('kernel_vertical',out1)
cv2.imshow('kernel_horizontal',out2)
cv2.imshow('kernel_diag_pos',out3)
cv2.imshow('kernel_diag_neg',out4)
cv2.waitKey(0)