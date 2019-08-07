import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from scipy import signal

img1 = cv.imread('abc.png',0)
img2 = cv.imread('A.png',0 )

f = np.asarray(img1, dtype="float32")/255.0
h = np.asarray(img2, dtype="float32")/255.0


corr = signal.correlate2d(f, h, boundary='symm', mode='same')


#plt.plot(corr)
#plt.contourf(corr)
#plt.show()

y, x = np.unravel_index(np.argmax(corr), corr.shape)

bw = 50
bh = 50

#f2 = cv.cvtColor(f, cv.COLOR_GRAY28GR)
f2 = cv.cvtColor(f, cv.COLOR_GRAY2RGB)
cv.rectangle(f2,(x-bw, y - bh), (x+bw, y + bh),(0,0,255),3)
cv.imshow('Detection' ,f2)
cv.waitKey(0)

