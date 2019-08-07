import cv2
import numpy as np

def RemoveGreenScreen(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #hardcode values for greenscreen jeje, it's not cheating :p
    lower_green = np.array([37,110,85])
    upper_green = np.array([87,255,255])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    res =  cv2.bitwise_and(img, img, mask = mask)
    filter_output = img - res
    #erosion para disminuir los bordes
    kernel = np.ones((3,3),dtype=np.uint8)
    filter_output = cv2.erode(filter_output,kernel,iterations=1)
    #filter_output = np.asarray(filter_output,dtype=np.float32)/255.0
    return filter_output


def CombineImages(img1,img2):
    rows,cols,channels = img2.shape
    roi = img1[0:rows, 0:cols ]
    img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY_INV)
    #kernel = np.ones((14,11),dtype=np.uint8)
    #kernel2 = np.ones((5,4),dtype=np.uint8)
    #mask = cv2.dilate(mask,kernel,iterations=1)
    #mask = cv2.erode(mask,kernel2, iterations= 1)
    mask_inv = cv2.bitwise_not(mask)
    img1_bg = cv2.bitwise_and(roi,roi,mask = mask)
    img2_fg = cv2.bitwise_and(img2,img2,mask = mask_inv)
    dst = cv2.add(img1_bg,img2_fg)
    img1[0:rows, 0:cols] = dst
    return img1
    

print("Predefined Green Screen Images: \nGS_img1.png \nGS_img2.png \nGS_img3.png")
img1 = input("Select image to remove Green Screen: ")
print("Predefined Background Images: \nBG_img1.png \nBG_img2.png \nBG_img3.png")
img2 = input("Select image to remove Green Screen: ")


green_screen_img = cv2.imread(img1,1)
background_img = cv2.imread(img2,1)

not_green = RemoveGreenScreen(green_screen_img)
out = CombineImages(background_img,not_green)
cv2.imwrite('Resultado_EJC_2.png',out)
print('done')
