import numpy as np
import cv2 as cv2
import math

def Saturation(position):
    blue = position[0]
    green = position[1]
    red = position[2]
    saturation = 1 - 3*(min(red,green,blue))/(red+green+blue)
    return saturation
def Intensity(position):
    blue = position[0]
    green = position[1]
    red = position[2]
    intensity = (red + green + blue)/3
    return intensity
def Hue(position):
    blue = position[0]
    green = position[1]
    red = position[2]
    theta = math.degrees(math.acos((((red-green)+(red-blue))/2)/((((red-green)**2)+((red-blue)*(green-blue)))**0.5)))
    if (blue<=green):
        hue = theta
    else:
        hue = 360-theta
    return hue
def HSItoRGB(positionH, positionS, positionI):
    blue = positionI * (1.0 - positionS)
    red = positionI * (1.0 + ( positionS * ( math.degrees(math.cos(positionH)))/(math.degrees(math.cos(60 - positionH))) ))
    final = blue + red
    return final





#Declarar imagenes
img1 = cv2.imread("x_wing.png",1)
img1 = np.asarray(img1,dtype=np.float32)/255.0
img2 = cv2.imread("sky.png",1)
img2 = np.asarray(img2,dtype=np.float32)/255.0

#dilatar para que las orillas se encuentren un poco mas gruesa
#kernel = np.ones((3,3),np.unit8)
#img1 = cv2.dilate(img1,kernel,iterations=1)



#Modelo HSI
saturation = np.zeros(img1.shape, dtype= np.float32)
intensity = np.zeros(img1.shape, dtype= np.float32)
hue = np.zeros(img1.shape, dtype= np.float32)

total = np.zeros(img1.shape, dtype= np.float32)

for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        saturation[i,j] = Saturation(img1[i,j])
        intensity[i,j] = Intensity(img1[i,j])
        hue[i,j] = Hue(img1[i,j])
        total[i,j] = HSItoRGB(hue[i,j],saturation[i,j],intensity[i,j])

#imagen resultante  

hue = hue/180.0
cv2.imshow('total',total)
cv2.waitKey(0)