import numpy as np
import cv2

#Image to negative
img1 = cv2.imread('earth.png', 1)
img2 = cv2.imread('sand.png', )

alpha = 0.25

result = (alpha * img1 + (1 - alpha) * img2)
cv2.imwrite('out.png',result)
img3 = cv2.imread('out.png', )
cv2.imshow('out',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()