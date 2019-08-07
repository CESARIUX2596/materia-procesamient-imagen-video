from scipy import misc
import matplotlib.pyplot as plt
import numpy as np

f = misc.imread("./sunflowers.jpg")

x,y,rgb=f.shape

for i in range(x):
    for j in range(y):
        if (f[i,j,0]<210 and f[i,j,1]<160):
            f[i,j]= np.mean(f[i,j])
#Yellow = 255 214 8
plt.imshow(f)
plt.show()