import cv2 
import numpy as np 

yayalar =  cv2.imread("C:\\Users\\Coder\\MyAiLab\\OpenCv\\odev2.jpg",0)
cv2.imshow("Original",yayalar)
cv2.waitKey(0)

imgBlurred = cv2.blur(yayalar,(6,6))
gauss = cv2.GaussianBlur(imgBlurred,(3,3),sigmaX=7)

median_val = np.median(yayalar)
low = int(max(0,(1-0.33)*median_val))
high = int(min(255,(1+0.33)*median_val))

imgCanny = cv2.Canny(gauss,threshold1=low,threshold2=high)
cv2.imshow("Edges Detection",imgCanny)
cv2.waitKey(0)

faceCascade = cv2.CascadeClassifier("C:\\Users\\Coder\\MyAiLab\\OpenCv\\haarcascade_frontalface_default.xml")
face_rect_coords = faceCascade.detectMultiScale(yayalar,minNeighbors=3)

for (x,y,w,h) in face_rect_coords:
    cv2.rectangle(yayalar,(x,y),(x+w,y+h),(255,255,255),4)
cv2.imshow("Face Detection",yayalar)
cv2.waitKey(0)

hog= cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

rects,weights = hog.detectMultiScale(yayalar,scale=1.12,padding=(8,8))

for (x,y,w,h) in rects:
    cv2.rectangle(yayalar,(x,y),(x+w,y+h),(255,255,255),3)
cv2.imshow("Human Detection",yayalar)
cv2.waitKey(0)
