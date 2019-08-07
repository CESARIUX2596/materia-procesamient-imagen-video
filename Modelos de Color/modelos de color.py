import matplotlib.pyplot as plt
from scipy import misc
import numpy as np
import cv2 as cv2
import math



f = cv2.imread("strawberries_coffee_full_color.png",1)
f = np.asarray(f,dtype=np.float32)/255.0

bgrBlue, bfrGreen, bgrRed  = cv2.split(f)

#theta = math.acos((((bgrRed-bfrGreen)+(bgrRed-bgrBlue))/2)/((((bgrRed-bfrGreen)**2)+((bgrRed-bgrBlue)*(bfrGreen-bgrBlue)))**0.5))
#Cyan
Cyan = red - 1
#Magenta
Magenta = green - 1
#Yellow
Yellow = blue - 1

#Hue

#Saturation
#for i in range (f.shape[0]):
#    for j in range(f.shape[1]):
        

#Intensity
#Intensity = (bgrRed + bfrGreen + bgrBlue)/3


#CMY

cv2.imshow('Yellow',bgrBlue)
cv2.waitKey(0)
#plt.imshow(Magenta)
#plt.show()

#RGB

#plt.imshow(red)
#plt.show()
#plt.imshow(blue)
#plt.show()
#plt.imshow(green)
#plt.show()

#HSI
#plt.imshow(Hue)
#plt.show()
#plt.imshow(Saturation)
#plt.show()
#plt.imshow(Intensity, cmap='gray')
#cv2.imshow('Saturation', Intensity)
#cv2.imshow('Intensity', Intensity)
#cv2.waitKey(0)