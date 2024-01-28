import cv2
import matplotlib.pyplot as plt 
import numpy as np

img= cv2.imread("C:\\Users\\Coder\\MyAiLab\\OpenCv\\cat.jpg")
print(img.shape)
sablon= cv2.imread("C:\\Users\\Coder\\MyAiLab\\OpenCv\\cat_face.jpg")
print(sablon.shape)
h, w,_ = sablon.shape

methodlar= ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for i in methodlar:
    #Methodlarimiz string olarak gozukuyor normal fonk haline getirelim.
    method= eval(i)
    
    sablon_eslestirme = cv2.matchTemplate(img,sablon,method)
    print(cv2.minMaxLoc(sablon_eslestirme))
    min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(sablon_eslestirme)
    
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
        
    bottom_right = (top_left[0]+w,top_left[1]+h)
        
    cv2.rectangle(img,top_left,bottom_right,(0,255,0),2)
    
    plt.figure()
    plt.title("Eslesen Resim")
    plt.axis("off")
    plt.subplot(121)
    plt.imshow(sablon_eslestirme)
    plt.show()

    plt.figure()
    plt.title("Original Resim")
    plt.axis("off")
    plt.subplot(122)
    plt.imshow(img)
    plt.show()