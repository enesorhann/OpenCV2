import cv2
import matplotlib.pyplot as plt
import numpy as np

img= cv2.imread("C:\\Users\\Coder\\MyAiLab\\OpenCv\\sudoku.jpg",0)
img= np.float32(img)
print(img.shape)
plt.figure()
plt.imshow(img,cmap="gray")
plt.title("Original")
plt.axis("off")
plt.show()

dst= cv2.cornerHarris(img,blockSize=2,ksize=3,k=0.07)
plt.figure()
plt.imshow(dst,cmap="gray")
plt.title("Corner Harris")
plt.axis("off")
plt.show()

dst= cv2.dilate(dst, None)
img[dst>0.2*dst.max()] = 1
plt.figure()
plt.imshow(dst,cmap="gray")
plt.title("Corner Harris + Dilate")
plt.axis("off")
plt.show()

img= cv2.imread("C:\\Users\\Coder\\MyAiLab\\OpenCv\\sudoku.jpg",0)
img= np.float32(img)
corners= cv2.goodFeaturesToTrack(img,120,0.07,11)
corners= np.int64(corners)

for i in corners:
    x,y= i.ravel()
    cv2.circle(img,(x,y),3,(155,155,155),cv2.FILLED)
    
plt.figure()
plt.imshow(img)
plt.title("Tomasi Corners with circle")
plt.axis("off")
plt.show()


