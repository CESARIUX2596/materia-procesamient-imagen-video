from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
import math

f = misc.imread("./sunflowers.jpg")
fgray = f.copy()
euclidean = f.copy()
manhattan = f.copy()
chessboard = f.copy()

#image parameters
x,y,rgb=fgray.shape

for i in range(x):
    for j in range(y):
        if (fgray[i,j,0]<210 and fgray[i,j,1]<160):
            fgray[i,j]= np.mean(fgray[i,j])

euclidean = np.zeros((x,y))
manhattan = np.zeros((x,y))
chessboard = np.zeros((x,y))

for i in range(x):
	for j in range(y):
		euclidean[i,j] = pow((pow(f[i,j,0]-fgray[i,j,0],2) + pow(f[i,j,1]-fgray[i,j,1],2) + pow(f[i,j,2]-fgray[i,j,2],2)),0.5)
		manhattan[i,j] = abs(f[i,j,0]-fgray[i,j,0]) + abs(f[i,j,1]-fgray[i,j,1]) + abs(f[i,j,2]-fgray[i,j,2])
		chessboard[i,j] = max(abs(f[i,j,0]-fgray[i,j,0]) , abs(f[i,j,1]-fgray[i,j,1]) , abs(f[i,j,2]-fgray[i,j,2]))
		

plt.imshow(euclidean)
plt.show()

plt.imshow(manhattan)
plt.show()

plt.imshow(chessboard)
plt.show()

	


