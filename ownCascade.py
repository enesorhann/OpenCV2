import cv2 

cascade = cv2.CascadeClassifier("C:\\Users\\Coder\\MyAiLab\\OpenCv\\cascade.xml")

object_Name = "Telefon"
frameWidth=280
frameHeight = 360
color=(255,0,0)

cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)

def empty(a):pass

cv2.namedWindow("Sonuc")
cv2.resizeWindow("Sonuc",frameWidth,frameHeight+10)
cv2.createTrackbar("Scale","Sonuc",400,1000,empty)
cv2.createTrackbar("Neighboor","Sonuc",4,50,empty)

while True:
    success, frame= cap.read()
    if success:
        frameG = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        scale= 1 + (cv2.getTrackbarPos("Scale","Sonuc")/1000)
        neighboor= cv2.getTrackbarPos("Scale","Sonuc")
        rect_coord = cascade.detectMultiScale(frameG,scale,neighboor)

    for (x,y,w,h) in rect_coord:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),7)
    cv2.imshow("Sonuc",frame)
    cv2.putText(frame,object_Name,(x,y-10),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,color,4)
    
    if cv2.waitKey(1) & 0XFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()















































