import matplotlib.pyplot as plt
from scipy import misc
from tkinter import *
import numpy as np
import cv2

def blur():
    img1 = cv2.imread(imgSelect.get(), 1)
    x,y,z = (img1.shape)
    img2= np.zeros((x,y,3))

    value = nValue.get()
   

    for i in range(0,x,value):
        for j in range(0,y, value):
            for k in range (z):
                v_min= 255
                v_max= 0
                for l in range (value):
                    for m in range (value):
                        try:
                            if (img1[i+l,j+m,k] < v_min):
                                v_min = img1[i+l,j+m,k]
                            if (img1[i+l,j+m,k] > v_min):
                                v_max = img1[i+l,j+m,k]
                        except Exception as e:
                            pass
                for n in range (value):
                    for o in range (value):
                        try:
                            if(minMax.get() == 0):
                                img2[i+n,j+o,k] = v_min
                            else:
                                img2[i+n,j+o,k] = v_max
                        except Exception as e:
                            pass
    cv2.imwrite('out.png',img2)
    img3 = cv2.imread('out.png', )
    cv2.imshow('out',img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#GUI
window = Tk()
window.title("Ejercicio 1.3")
window.geometry("800x630")
imageSelected = StringVar()

#image 1    
Label(window, text = "Image 1").place(x = 180, y = 5)
photo = PhotoImage(file = "earth.png")
photo = photo.zoom(1)
photo = photo.subsample(5)
photo_label = Label(image = photo)
photo_label.place(x = 10, y = 25)
photo_label.image = photo

#image 2
Label(window, text = "Image 2").place(x = 580, y = 5)
photo2 = PhotoImage(file = "sand.png")
photo2 = photo2.zoom(1)
photo2 = photo2.subsample(5)
photo_label = Label(image = photo2)
photo_label.place(x = 400, y = 25)
photo_label.image = photo2

#image 3
Label(window, text = "Image 3").place(x = 180, y = 248)
photo3 = PhotoImage(file = "road.png")
photo3 = photo3.zoom(1)
photo3 = photo3.subsample(5)
photo_label = Label(image = photo3)
photo_label.place(x = 10, y = 270)
photo_label.image = photo3

#image 4
Label(window, text = "Image 4").place(x = 580, y = 248)
photo4 = PhotoImage(file = "rick.png")
photo4 = photo4.zoom(1)
photo4 = photo4.subsample(5)
photo_label = Label(image = photo4)
photo_label.place(x = 400, y = 270)
photo_label.image = photo4

Label(window, text = "Value for n: ").place(x = 365, y = 500)
nValue = IntVar()
minMax = IntVar()
imgSelect = StringVar()
Radiobutton(window, text = "1", value = 1, variable = nValue).place(x = 55, y = 515)
Radiobutton(window, text = "3", value = 3, variable = nValue).place(x = 145, y = 515)
Radiobutton(window, text = "5", value = 5, variable = nValue).place(x = 235, y = 515)
Radiobutton(window, text = "7", value = 7, variable = nValue).place(x = 325, y = 515)
Radiobutton(window, text = "9", value = 9, variable = nValue).place(x = 415, y = 515)
Radiobutton(window, text = "11", value = 11, variable = nValue).place(x = 505, y = 515)
Radiobutton(window, text = "13", value = 13, variable = nValue).place(x = 595, y = 515)
Radiobutton(window, text = "15", value = 15, variable = nValue).place(x = 685, y = 515)

Label(window, text = "Image to blur: ").place(x = 130, y = 540)
r2_1 = Radiobutton(window, text = "Image 1", value = "earth.png", variable = imgSelect).place(x = 210, y = 540)
r2_2 = Radiobutton(window, text = "Image 2", value = "sand.png", variable = imgSelect).place(x = 310, y = 540)
r2_3 = Radiobutton(window, text = "Image 3", value = "road.png", variable = imgSelect).place(x = 420, y = 540)
r2_4 = Radiobutton(window, text = "Image 4", value = "rick.png", variable = imgSelect).place(x = 510, y = 540)

Radiobutton(window, text = "Min", value = 0, variable = minMax).place(x = 320, y = 565)
Radiobutton(window, text = "Max", value = 1, variable = minMax).place(x = 420, y = 565)

Button(window, text = "Blur", width=15, fg = "red", command = blur).place(x = 330, y = 600 )








window.mainloop()