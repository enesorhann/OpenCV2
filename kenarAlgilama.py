import cv2
import numpy as np 
import matplotlib.pyplot as plt

img= cv2.imread("C:\\Users\\Coder\\MyAiLab\\OpenCv\\london.jpg",0)
plt.figure()
plt.imshow(img,cmap="gray")
plt.title("Original")
plt.axis("off")
plt.show()

edges= cv2.Canny(img,threshold1=0,threshold2=255)
plt.figure()
plt.imshow(edges,cmap="gray")
plt.title("Kenar Algilama 0-255 pikseller")
plt.axis("off")
plt.show()

med_value= np.median(img)
print(med_value)

low= int(max(0,(1-0.33)*med_value))
high= int(min(255,(1+0.33)*med_value))
print(low)
print(high)

edges= cv2.Canny(img,threshold1=low,threshold2=high)
plt.figure()
plt.imshow(edges,cmap="gray")
plt.title("Kenar Algilama low,high pikseller")
plt.axis("off")
plt.show()

#Original resmimizdeki detaylari azaltip deneyelim bir de
blurred_img= cv2.blur(img,ksize=(4,4))
plt.figure()
plt.imshow(blurred_img,cmap="gray")
plt.title("Bulanik Hali")
plt.axis("off")
plt.show()

edges= cv2.Canny(blurred_img,threshold1=0,threshold2=255)
plt.figure()
plt.imshow(edges,cmap="gray")
plt.title("Kenar Algilama tum pikseller")
plt.axis("off")
plt.show()

med_value= np.median(img)
print(med_value)

low= int(max(0,(1-0.33)*med_value))
high= int(min(255,(1+0.33)*med_value))
print(low)
print(high)


edges= cv2.Canny(blurred_img,threshold1=low,threshold2=high)
plt.figure()
plt.imshow(edges,cmap="gray")
plt.title("Kenar Algilama low,high pikseller")
plt.axis("off")
plt.show()