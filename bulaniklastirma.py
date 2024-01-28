import numpy as np
import matplotlib.pyplot as plt
import cv2
import random

img= cv2.imread("C:\\Users\\Coder\\MyAiLab\\OpenCv\\NYC.jpg")
img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img)
plt.title("Orijinal")
plt.axis("off")

dst2= cv2.blur(img,ksize=(3,3))
plt.figure()
plt.imshow(dst2)
plt.title("Ortalama Blur")
plt.axis("off")

gb= cv2.GaussianBlur(img,ksize=(3,3),sigmaX=7)
plt.figure()
plt.imshow(gb)
plt.title("Gaussian Blur")
plt.axis("off")

mb=cv2.medianBlur(img,ksize=3)
plt.figure()
plt.imshow(mb)
plt.title("Median Blur")
plt.axis("off")

def GaussianGurultusu(image):
    row,col,ch= image.shape
    mean = 0
    var = 0.05
    sigma = var**0.5
    gauss= np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(((row,col,ch)))
    noisy = gauss+image
    return noisy

def tuzBiberGurultusu(image):
    row,col,ch= image.shape
    tuzbiber = 0.5
    amount = 0.004
    noisy = np.copy(image)
    # Salt mode
    num_tuz = np.ceil(amount * image.size * tuzbiber)
    coords = [np.random.randint(0, i - 1, int(num_tuz)) for i in image.shape]
    noisy[coords] = 1
    
    num_biber = np.ceil(amount * image.size * tuzbiber)
    coords = [np.random.randint(0, i - 1, int(num_biber)) for i in image.shape]
    noisy[coords] = 0
    
    return noisy

img= cv2.imread("C:\\Users\\Coder\\MyAiLab\\OpenCv\\NYC.jpg")
img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img)
plt.title("Orijinal")
plt.axis("off")

gaussNoisy = GaussianGurultusu(img)
plt.figure()
plt.imshow(gaussNoisy)
plt.title("Gauss Gurultusu")
plt.axis("off")

tuzbiber= tuzBiberGurultusu(img)
plt.figure()
plt.imshow(tuzbiber)
plt.title("Tuz Biber Gurultusu")
plt.axis("off")

gb= cv2.GaussianBlur(gaussNoisy,ksize=(3,3),sigmaX=7)
plt.figure()
plt.imshow(gb)
plt.title("Gaussian Blur")
plt.axis("off")

mb=cv2.medianBlur(tuzbiber.astype(np.float32),ksize=3)
plt.figure()
plt.imshow(mb)
plt.title("Median Blur")
plt.axis("off")
    
    
    









