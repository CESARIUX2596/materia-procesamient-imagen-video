import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv2
import math

def Horizontal(d, img):
    kernel_motion_blur = np.zeros((d,d))
    kernel_motion_blur[int((d-1)/2),:] = np.ones(d)
    kernel_motion_blur = kernel_motion_blur / d
    out =  cv2.filter2D(img, -1, kernel_motion_blur)
    return out

def Vertical(d, img):
    kernel_motion_blur = np.zeros((d,d))
    kernel_motion_blur[:,int((d-1)/2)] = np.ones(d)
    kernel_motion_blur = kernel_motion_blur / d
    out =  cv2.filter2D(img, -1, kernel_motion_blur)
    return out

def Diagonal(d, img):
    kernel_motion_blur = np.zeros((d,d))
    np.fill_diagonal(kernel_motion_blur,1)
    kernel_motion_blur = kernel_motion_blur / d
    out =  cv2.filter2D(img, -1, kernel_motion_blur)
    return out


def Radial(d, img):
    kernel_motion_blur = np.zeros((d,d))
    kernel_motion_blur[:,int((d-1)/2)] = np.ones(d)
    kernel_motion_blur = kernel_motion_blur / d
    val = np.sqrt(((img.shape[0]/1.0)**2)+((img.shape[1]/1.0)**2))
    polarImg = cv2.linearPolar(img,(img.shape[0]/2.0, img.shape[1]/2.0), val, cv2.WARP_FILL_OUTLIERS)
    polarImg = polarImg.astype(np.uint8)
    out =  cv2.filter2D(polarImg, -1, kernel_motion_blur)
    out = cv2.linearPolar(out, (img.shape[0]/2.0, img.shape[1]/2.0), val, cv2.WARP_INVERSE_MAP)
    return out

def Zoom(d, img):
    kernel_motion_blur = np.zeros((d,d))
    kernel_motion_blur[int((d-1)/2),:] = np.ones(d)
    kernel_motion_blur = kernel_motion_blur / d
    val = np.sqrt(((img.shape[0]/1.0)**2)+((img.shape[1]/1.0)**2))
    polarImg = cv2.linearPolar(img,(img.shape[0]/2.0, img.shape[1]/2.0), val, cv2.WARP_FILL_OUTLIERS)
    polarImg = polarImg.astype(np.uint8)
    out =  cv2.filter2D(polarImg, -1, kernel_motion_blur)
    out = cv2.linearPolar(out, (img.shape[0]/2.0, img.shape[1]/2.0), val, cv2.WARP_INVERSE_MAP)
    return out

def ApplyBlur(method, d, img):
    if method == 1:
        out = Horizontal(d,img)
        return out
    elif method == 2:
        out = Vertical(d,img)
        return out
    elif method == 3:
        out = Diagonal(d,img)
    elif method == 4:
        out = Radial(d, img)
        return out
    elif method == 5:
        out = Zoom(d, img)
        return out
    else:
        print("Methoth " + method + " doesn't exist.")
        pass

#img1 = cv2.imread('img1.png',1)
#img2 = cv2.imread('img2.png',1)
#img3 = cv2.imread('img3.png',1)
#img4 = cv2.imread('img4.png',1)

print("Methods: \n [1] Horizontal \n [2] Vertical \n [3] Diagonal \n [4] Radial \n [5] Zoom \n ")
method = int(input("Select a method: "))
d = int(input("Degradation intensity: "))
print("Predefined images: \nimg1.png \nimg2.png \nimg3.png")
selectImg = input("name or path for image: ")
img = cv2.imread(selectImg,1)

output = ApplyBlur(method, d, img)

cv2.imwrite('Resultado_EJC_5.png', output)
print("done")