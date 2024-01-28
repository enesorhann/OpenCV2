import cv2
import numpy as np

img = cv2.imread("kart.png")
#cv2.imshow("İmage",img)

width = 400
height = 500

pers= np.float32([[203,1],[1,472],[540,150],[338,617]])
new_pers= np.float32([[0,0],[0,height],[width,0],[width,height]])

matrix = cv2.getPerspectiveTransform(pers,new_pers)
print(matrix)

imgOutput = cv2.warpPerspective(img,matrix,(width,height))
#cv2.imshow("İmage",img)
cv2.imshow("Son Hali",imgOutput)