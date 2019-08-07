import matplotlib.pyplot as plt
from scipy import misc
from tkinter import *
import numpy as np
import cv2
#Sub-Routines:
def speak1():
    img = cv2.imread('lena.png')
    Z = img.reshape((-1,3))
    # convert to np.float32
    Z = np.float32(Z) 
    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    inp = inputBox.get()
    K = int(inp)
    ret,label,center=cv2.kmeans(Z,K+1,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))

    cv2.imshow('res2',res2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def speak2():
    img = cv2.imread('racoon.png')
    Z = img.reshape((-1,3))
    # convert to np.float32
    Z = np.float32(Z) 
    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    inp = inputBox.get()
    K = int(inp)
    ret,label,center=cv2.kmeans(Z,K+1,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))

    cv2.imshow('res2',res2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def speak3():
    img = cv2.imread('hedgehog.png')
    Z = img.reshape((-1,3))
    # convert to np.float32
    Z = np.float32(Z) 
    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    inp = inputBox.get()
    K = int(inp)
    ret,label,center=cv2.kmeans(Z,K+1,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))

    cv2.imshow('res2',res2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#GUI
window = Tk()
window.title("Ejercicio 1.1")
window.geometry("800x450")


photo = PhotoImage(file = "lena.png")
photo = photo.zoom(30)
photo = photo.subsample(64)
photo_label = Label(image = photo)
photo_label.place(x = 15, y = 25)
photo_label.image = photo

photo2 = PhotoImage(file = "racoon.png")
photo2 = photo2.zoom(30)
photo2 = photo2.subsample(64)
photo_label2 = Label(image = photo2)
photo_label2.place(x = 280, y = 25)
photo_label2.image = photo2

photo3 = PhotoImage(file = "hedgehog.png")
photo3 = photo3.zoom(30)
photo3 = photo3.subsample(64)
photo_label3 = Label(image = photo3)
photo_label3.place(x = 565, y = 25)
photo_label3.image = photo3

#Input Box
Label(window, text = "K Value = ").place(x = 325, y = 280)
inputBox = Entry(window, width = 10, bg = "white")
inputBox.place(x = 385, y = 280)
inputBox.insert(END, '1')


Button(window, text = "Image 1", width = 6, command = speak1).place(x = 80, y = 350)
Button(window, text = "Image 2", width = 6, command = speak2).place(x = 350, y = 350)
Button(window, text = "Image 3", width = 6, command = speak3).place(x = 617, y = 350)
Label(window, text = "Image 1 ").place(x = 105, y = 5)
Label(window, text = "Image 2 ").place(x = 375, y = 5)
Label(window, text = "Image 3 ").place(x = 642, y = 5)




window.mainloop()
