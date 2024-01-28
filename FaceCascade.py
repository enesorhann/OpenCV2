import cv2 
import matplotlib.pyplot as plt 

face_cascade= cv2.CascadeClassifier("C:\\Users\\Coder\\MyAiLab\\OpenCv\\haarcascade_frontalface_default.xml")

einstein = cv2.imread("C:\\Users\\Coder\\MyAiLab\\OpenCv\\einstein.jpg",0)
plt.figure(),plt.imshow(einstein,cmap="gray"),plt.axis("off"),plt.show()

face_rect_koordinat = face_cascade.detectMultiScale(einstein)

for (x,y,w,h) in face_rect_koordinat:
    cv2.rectangle(einstein,(x,y),(x+w,y+h),(255,255,255),6)
plt.figure(),plt.imshow(einstein,cmap="gray"),plt.axis("off"),plt.show()
    
    
barce = cv2.imread("C:\\Users\\Coder\\MyAiLab\\OpenCv\\barcelona.jpg",0)
plt.figure(),plt.imshow(barce,cmap="gray"),plt.axis("off"),plt.show()

face_rect_koordinat = face_cascade.detectMultiScale(barce,minNeighbors=7)

for (x,y,w,h) in face_rect_koordinat:
    cv2.rectangle(barce,(x,y),(x+w,y+h),(255,255,255),11)
plt.figure(),plt.imshow(barce,cmap="gray"),plt.axis("off"),plt.show()

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if success:
        face_rect_koordinat = face_cascade.detectMultiScale(frame,minNeighbors=7)

        for (x,y,w,h) in face_rect_koordinat:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),11)
        plt.figure(),plt.imshow(frame,cmap="gray"),plt.axis("off"),plt.show()     
    else:
        break
cap.release()
cv2.destroyAllWindows()







