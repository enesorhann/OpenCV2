import matplotlib.pyplot as plt 
import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Coder\\MyAiLab\\OpenCv\\odev1.jpg",0)
plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("Orijinal")
print(img.shape)

yeni_boyut = cv2.resize(img,(688,454))
plt.figure()
plt.imshow(yeni_boyut)
plt.axis("off")
plt.title("Boyutlandirilmis Resim")
plt.show()
print(yeni_boyut.shape)

plt.figure()
plt.imshow(img)
plt.title("Hayvanat:))")
plt.axis("off")
plt.show()

_,img_thresh= cv2.threshold(img,thresh=50,maxval=255,type=cv2.THRESH_BINARY)
plt.figure()
plt.imshow(img_thresh)
plt.axis("off")
plt.title("Thresh Edilmis")
plt.show()

gb= cv2.GaussianBlur(img,ksize=(3,3),sigmaX=7)
plt.figure()
plt.imshow(gb)
plt.axis("off")
plt.title("Gauss Blurlama")
plt.show()

laplacian= cv2.Laplacian(img,ddepth=cv2.CV_16S)
plt.figure()
plt.imshow(laplacian)
plt.axis("off")
plt.title("Laplace edilen resim")
plt.show()

