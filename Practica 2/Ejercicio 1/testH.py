import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv2
import math

def Diagonal(d, img):
    kernel_motion_blur = np.zeros((d,d))
    np.fill_diagonal(kernel_motion_blur, 1)
    kernel_motion_blur = kernel_motion_blur / d
    out =  cv2.filter2D(img, -1, kernel_motion_blur)
    return out

img1 = cv2.imread('img1.png',1)
d = 15
out = Diagonal(d,img1)
cv2.imwrite('out.png', out)
cv2.waitKey(0)