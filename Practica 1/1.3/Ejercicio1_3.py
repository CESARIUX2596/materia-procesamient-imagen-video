import matplotlib.pyplot as plt
from scipy import misc
from tkinter import *
import numpy as np
import cv2

def mix():
    img1 = cv2.imread(selection1.get(), 1)
    img2 = cv2.imread(selection2.get(), 1)
    alpha = int(slider.get())
    alpha = alpha/100
    result = (alpha * img2 + (1 - alpha) * img1)
    cv2.imwrite('out.png',result)
    img3 = cv2.imread('out.png', )
    cv2.imshow('out',img3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#GUI
window = Tk()
window.title("Ejercicio 1.3")
window.geometry("800x630")

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
photo4 = PhotoImage(file = "mountains.png")
photo4 = photo4.zoom(1)
photo4 = photo4.subsample(5)
photo_label = Label(image = photo4)
photo_label.place(x = 400, y = 270)
photo_label.image = photo4

Label(window, text = "Select images to combine ").place(x = 325, y = 490)
selection1 = StringVar()
selection2 = StringVar()
slider = IntVar()
Label(window, text = "Image 1   =   ").place(x = 140, y = 515)
r1_1 = Radiobutton(window, text = "Image 1", value = "earth.png", variable = selection1).place(x = 210, y = 515)
r1_2 = Radiobutton(window, text = "Image 2", value = "sand.png", variable = selection1).place(x = 310, y = 515)
r1_3 = Radiobutton(window, text = "Image 3", value = "road.png", variable = selection1).place(x = 420, y = 515)
r1_4 = Radiobutton(window, text = "Image 4", value = "mountains.png", variable = selection1).place(x = 510, y = 515)
Label(window, text = "Image 2   =   ").place(x = 140, y = 540)
r2_1 = Radiobutton(window, text = "Image 1", value = "earth.png", variable = selection2).place(x = 210, y = 540)
r2_2 = Radiobutton(window, text = "Image 2", value = "sand.png", variable = selection2).place(x = 310, y = 540)
r2_3 = Radiobutton(window, text = "Image 3", value = "road.png", variable = selection2).place(x = 420, y = 540)
r2_4 = Radiobutton(window, text = "Image 4", value = "mountains.png", variable = selection2).place(x = 510, y = 540)

Label(window, text = " % of Transparency of image 2: ").place(x = 140, y = 580)
Scale(window, orient = HORIZONTAL, length = 250, variable = slider).place(x = 330, y = 560)
Button(window, text = "Mix", width=15, fg = "red", command = mix).place(x = 625, y = 545 )








window.mainloop()