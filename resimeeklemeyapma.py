import cv2
import numpy as np

img= np.zeros((512,512,3),np.uint8)
print("Orijinal Boyut: ",img.shape)
cv2.imshow("Orijinal ",img)

cv2.line(img,(256,0),(0,256),(0,200,0),3)
cv2.imshow("Line",img)

cv2.rectangle(img,(480,480),(720,720),(200,0,0),cv2.FILLED) #baslangic,bitis,renk,kalinlik
cv2.imshow("Rectangle",img)

cv2.circle(img,(530,530),30,(0,0,200),cv2.FILLED) #merkez,yaricap
cv2.imshow("Circle",img)

cv2.putText(img,"Circle",(530,530),cv2.FONT_HERSHEY_COMPLEX,1,(55,55,95))
cv2.imshow("Text",img)