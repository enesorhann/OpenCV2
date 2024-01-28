import matplotlib.pyplot as plt 
import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Coder\\MyAiLab\\OpenCv\\adaLovelace.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img = img.astype(np.float32)
plt.figure()
plt.imshow(img,cmap="gray")
plt.title("Orijinal")
plt.axis("off")
plt.show()

thresh1= cv2.threshold(img,thresh=60,maxval=255,type=cv2.THRESH_BINARY)
plt.figure()
plt.imshow(thresh1,cmap="gray")
plt.title("Thresh1")
plt.axis("off")
plt.show()

thresh2= cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)
plt.figure()
plt.imshow(thresh2,cmap="gray")
plt.title("Thresh2")
plt.axis("off")
plt.show()