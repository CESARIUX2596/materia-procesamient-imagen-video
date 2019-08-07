import numpy as np
import cv2

#Image to negative
img = cv2.imread('aerial.png', 0)
img2 = img.astype(np.float32) / 255.0

c = 1
e = 0.000001
gamma = 3.0

s = c * (img2 + e)**gamma

cv2.imwrite('gamma.png',s)
cv2.imshow('gamma',s)
cv2.waitKey(0)
cv2.destroyAllWindows()