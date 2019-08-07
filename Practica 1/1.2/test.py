import matplotlib.pyplot as plt
from scipy import misc
from tkinter import *
import numpy as np
import cv2

img1 = cv2.imread("rick.png", 1)
x,y,z = (img1.shape)
img2= np.zeros((x,y,3))

n1= 1
n3 = 3

for i in range(0,x,n3):
    for j in range(0,y, n3):
        for k in range (z):
            v_min= 255
            v_max= 0
            for l in range (n3):
                for m in range (n3):
                    try:
                        if (img1[i+l,j+m,k] < v_min):
                            v_min = img1[i+l,j+m,k]
                        if (img1[i+l,j+m,k] > v_min):
                            v_max = img1[i+l,j+m,k]
                    except Exception as e:
                        pass
            for n in range (n3):
                for o in range (n3):
                    try:
                        img2[i+n,j+o,k] = v_max
                    except Exception as e:
                        pass





cv2.imwrite('out.png',img2)
img3 = cv2.imread('out.png', )
cv2.imshow('out',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
