import numpy as np
import cv2 as cv2

f = np.full((512,512), False, dtype=bool)
g = np.full((512,512), False, dtype=bool)

f[180:315, 200:380] = True
g[250:414, 320:430] = True
#not f
calc1 = np.logical_not(f)
#f and g
calc2 = np.logical_and(f,g)
#f or g
calc3 = np.logical_or(f,g)
#f xor g
calc4 = np.logical_xor(f,g)
#[not (f)]and g
calc5 = np.logical_and(np.logical_not(f),g)

f = np.asarray(f,dtype=np.float32)
g = np.asarray(g,dtype=np.float32)
calc1 = np.asarray(calc1,dtype=np.float32)
calc2 = np.asarray(calc2,dtype=np.float32)
calc3 = np.asarray(calc3,dtype=np.float32)
calc4 = np.asarray(calc4,dtype=np.float32)
calc5 = np.asarray(calc5,dtype=np.float32)
cv2.imshow('not f', calc1)
cv2.imshow('f and g', calc2)
cv2.imshow('f or g', calc3)
cv2.imshow('f xor g', calc4)
cv2.imshow('[not (f)]and g', calc5)
cv2.imshow('f',f)
cv2.imshow('g',g)
cv2.waitKey(0)