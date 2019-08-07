import cv2
import numpy as np

import sys
from scipy import signal

from scipy import linalg
import numpy as np

def sobel(length):
    size = length*2 + 1
    kernelx = np.zeros((size,size))
    kernely = np.zeros((size,size))
    for i in range(-length,length+1):
        for j in range(-length,length+1):
            div = -(i*i + j*j)
            if div != 0 :
                kernelx[i+length,j+length] = i / div
                kernely[i+length,j+length] = j / div
    return kernelx, kernely

def prewitt(length):
    size = length*2 + 1
    kernelx = np.zeros((size,size))
    kernely = np.zeros((size,size))
    for i in range(-length,length+1):
        for j in range(-length,length+1):
            kernely[i+length,j+length] = i
            kernelx[i+length,j+length] = -j
    return kernelx, kernely

def robert(length):
    size = length*2
    kernelx = np.zeros((size,size))
    kernely = np.zeros((size,size))
    for i in range(0,size):
        if length > (i+1/2):
            x = -1
        else:
            x = 1
        kernelx[i,i] = x
        kernely[-(i+1),i] = x
    return kernelx, kernely

def canny(shape,g, gx, gy):
    #theta
    theta = np.abs(np.round((np.arctan2(gy, gx))*(180.0/np.pi)))
    #non maximum suppresion
    nonMAXsup= g.copy()
    for i in range(shape[0]):
        for j in range(shape[1]):
            #Suppress pixels at the image edge
            if i == 0 or i == img.shape[0]-1 or j == 0 or j == img.shape[1] - 1:
                nonMAXsup[i, j] = 0
                continue
            gdir = theta[i, j] % 180
            if gdir == 0: #E-W (horizontal)
                if g[i, j] <= g[i, j-1] or g[i, j] <= g[i, j+1]:
                    nonMAXsup[i, j] = 0
            if gdir > 0 and gdir < 90: #NE-SW
                if g[i, j] <= g[i-1, j+1] or g[i, j] <= g[i+1, j-1]:
                        nonMAXsup[i, j] = 0
            if gdir == 90: #N-S (vertical)
                if g[i, j] <= g[i-1, j] or g[i, j] <= g[i+1, j]:
                        nonMAXsup[i, j] = 0
            if gdir > 90 and gdir < 180: #NW-SE
                if g[i, j] <= g[i-1, j-1] or g[i, j] <= g[i+1, j+1]:
                        nonMAXsup[i, j] = 0
                        
    #threshold
    high = nonMAXsup.max()*(0.12)
    low = nonMAXsup.max()*(0.06)
    #Double threshold
    strongEdges = (nonMAXsup > high)
    #Strong has value 2, weak has value 1
    thresholdedEdges = np.array(strongEdges, dtype=np.uint8) + (nonMAXsup > low)

    #Edge tracking by hysteresis
    finalEdges = strongEdges.copy()
    currentPixels = []
    for i in range(1, shape[0]-1):
        for j in range(1, shape[1]-1):  
            if thresholdedEdges[i, j] != 1:
                continue #Not a weak pixel
             
            #Get 3x3 patch  
            localPatch = thresholdedEdges[i-1:i+2,j-1:j+2]
            patchMax = localPatch.max()
            if patchMax == 2:
                currentPixels.append((i, j))
                finalEdges[i, j] = 1
    #Extend strong edges based on current pixels
    while len(currentPixels) > 0:
        newPix = []
        for r, c in currentPixels:
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    if dr == 0 and dc == 0: continue
                    r2 = r+dr
                    c2 = c+dc
                    if thresholdedEdges[r2, c2] == 1 and finalEdges[r2, c2] == 0:
                        #Copy this weak pixel to final result
                        newPix.append((r2, c2))
                        finalEdges[r2, c2] = 1
        currentPixels = newPix
    return finalEdges.astype(float)
    
 

 
def fourierConvolve(x,y):
    s1 = np.array(x.shape)
    s2 = np.array(y.shape)
    size = s1 + s2 - 1
    fsize = 2 ** np.ceil(np.log2(size)).astype(int)
    fslice = tuple([slice(0, int(sz)) for sz in size])
    new_x = np.fft.fft2(x , fsize)
    new_y = np.fft.fft2(y , fsize)
    return np.fft.ifft2(np.multiply(new_x,new_y))[fslice].copy()

def giveMask(method, d):
    if method == 1:
        return prewitt(d)
    elif method == 2 or method == 4:
        return sobel(d)
    elif method == 3:
        return robert(d)
    else:
        print("Methoth " + method + " doesn't exist.")
        pass

print("Methods: \n [1] Prewitt \n [2] Sobel \n [3] Robert \n [4] Canny \n \n ")
method = int(input("Select a method: "))
size = int(input("Select size of kernel: " ))

selectImg = (input("name or path for image: "))
img = cv2.imread(selectImg)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

filterx, filtery = giveMask(method,size)
img_filterx = cv2.filter2D(img_gaussian, -1, filterx)
img_filtery = cv2.filter2D(img_gaussian, -1, filtery)

img_filter = np.abs(img_filterx) + np.abs(img_filtery)

img_filterfx = fourierConvolve(img_gaussian, filterx)
img_filterfy = fourierConvolve(img_gaussian, filtery)
img_filterfx= cv2.magnitude(np.real(img_filterfx),np.imag(img_filterfx))
img_filterfy= cv2.magnitude(np.real(img_filterfy),np.imag(img_filterfy))
img_filterf = (np.abs(img_filterfx) + np.abs(img_filterfy))
img_filterf = img_filterf/(img_filterf.max())
img_filterf = (img_filterf*255).astype(np.uint8)


if method ==4:
    img_filter=canny(img_gaussian.shape,img_filter,img_filterx,img_filtery)
    img_filterf=canny(img_gaussian.shape,img_filterf,img_filterfx,img_filterfy) 

cv2.imwrite("Filter.png", img_filter)
cv2.imwrite("FilterF.png", img_filterf)


##cv2.waitKey(0)
##cv2.destroyAllWindows() 
