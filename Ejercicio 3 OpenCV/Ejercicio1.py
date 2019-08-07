import matplotlib.pyplot as plt
import PIL.Image, PIL.ImageTk
from scipy import misc
from tkinter import *
import numpy as np
import cv2
#Sub-Routines:
def speak():
    print("Wubba Lubba Dub Dub!!!")
#GUI
window = Tk()
window.title("Ejercicio 1")
window.geometry("800x600")

canvas = Canvas(window, width=800, height=450)
canvas.pack()

img = PhotoImage(file="rick.jpg")    
canvas.create_image(20, 20, anchor=NW, image=img)

Button(window, text = "Image 1", width = 6, command = speak).place(x = 80, y = 500)
Button(window, text = "Image 2", width = 6, command = speak).place(x = 350, y = 500)
Button(window, text = "Image 3", width = 6, command = speak).place(x = 617, y = 500)





window.mainloop()
