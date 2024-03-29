import cv2
import matplotlib.pyplot as plt
import numpy as np

img= cv2.imread("C:\\Users\\Coder\\MyAiLab\\OpenCv\\contour.jpg",0)
plt.figure()
plt.imshow(img,cmap="gray")
plt.title("Original")
plt.axis("off")
plt.show()

contours,hierarchy= cv2.findContours(img,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)

external_contour= np.zeros(img.shape)
internal_contour= np.zeros(img.shape)

for i in range(len(contours)):
    #external contour
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(external_contour,contours,i,255,-1)
    #internal contour
    else:
        cv2.drawContours(internal_contour,contours,i,255,-1)

plt.figure(),plt.imshow(external_contour,cmap="gray"),plt.title("External Contour"),plt.axis("off"),plt.show()
plt.figure(),plt.imshow(internal_contour,cmap="gray"),plt.title("Internal Contour"),plt.axis("off"),plt.show()