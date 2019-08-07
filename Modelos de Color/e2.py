import numpy as np
import cv2 as cv2
import math

#f = cv2.imread("lena_saturada.png",1)

f = cv2.imread("lena_ruido.png",1)
f = np.asarray(f,dtype=np.float32)/255.0

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
#RGB Channels
#red
red = f.copy()
red[:, :, 1]=0
red[:, :, 0]=0
#blue
blue = f.copy()
blue[:, :, 1]=0
blue[:, :, 2]=0
#green
green = f.copy()
green[:, :, 0]=0
green[:, :, 2]=0

#CMY
cyan = np.ones(f.shape, dtype= np.float32) - red
magenta = np.ones(f.shape, dtype= np.float32) - green
yellow  =np.ones(f.shape, dtype= np.float32) - blue

#BGR
bgrBlue, bfrGreen, bgrRed  = cv2.split(f)

#HSI
#intensity


#saturation
saturation = np.ones(f.shape, dtype= np.float32)
intensity = np.ones(f.shape, dtype= np.float32)
hue = np.zeros(f.shape, dtype= np.float32)
#print(hue)
for i in range(f.shape[0]):
    for j in range(f.shape[1]):
        saturation[i,j] = Saturation(f[i,j])
        intensity[i,j] = Intensity(f[i,j])
        hue[i,j] = Hue(f[i,j])

hue = hue/180.0
cv2.imshow('intensity',intensity)
cv2.imshow('saturation',saturation)
cv2.imshow('hue',hue)
cv2.imshow('Blue',blue)
cv2.imshow('Green',green)
cv2.imshow('Red',red)
cv2.waitKey(0)