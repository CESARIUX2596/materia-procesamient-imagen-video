from scipy import misc
import matplotlib.pyplot as plt
import plotly.plotly as py
import numpy as np
import cv2 as cv2

f =  misc.imread("lena.png",0)
f = np.asarray(f,dtype=np.float32)/255.0

sigma = 0.25
n = np.random.normal(0,sigma,f.shape)

g = f + n

cv2.imshow('Degradado',g)
cv2.waitKey(0)