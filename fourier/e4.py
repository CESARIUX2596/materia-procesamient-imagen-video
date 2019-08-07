import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('rick.png')
kernel = np.ones((101,101),np.float32)/(101*101)
dst = cv.filter2D(img,-1,kernel)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()