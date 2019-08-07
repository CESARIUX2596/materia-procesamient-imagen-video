from scipy import misc
import matplotlib.pyplot as plt

f = misc.face()
misc.imsave('face.png', f)
#Image Shape
print(f.shape)
#RGB Channels
#red
red = f.copy()
red[:, :, 1]=0
red[:, :, 2]=0

#blue
blue = f.copy()
blue[:, :, 1]=0
blue[:, :, 0]=0
#green
green = f.copy()
green[:, :, 0]=0
green[:, :, 2]=0

#Grayscale
gray = f.copy()
gray[:] = gray.mean(axis=-1, keepdims=1)


plt.imshow(gray)
plt.show()

