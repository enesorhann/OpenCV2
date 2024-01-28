import cv2 
import numpy as np
from collections import deque

kuyruk_size=16
pts= deque(maxlen=kuyruk_size) #Nesne merkezini depolamak icin kullaniyoruz.

#Hsv tipinde blue araligi tanimlayalim
blueLower = (84,  98,  0)
blueUpper = (179, 255, 255)

cap = cv2.VideoCapture(0)

while True:
    success,frame= cap.read()
    
    if success:
        
        gauusBlur= cv2.GaussianBlur(frame,(11,11),3)
        frameHSV = cv2.cvtColor(gauusBlur,cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(frameHSV,blueLower,blueUpper)
        mask = cv2.erode(mask,None,2)
        mask = cv2.dilate(mask,None,2)
        
        contours,hierarchy = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        center= None
        
        if len(contours) > 0:
            
            c= max(contours,key = cv2.contourArea)
            
            rect= cv2.minAreaRect(c)
            
            ((x,y),(width,height),rotation) = rect
            
            s = "x: {},y: {},width: {},height: {},rotation: {}".format(np.round(x),np.round(y),np.round(width),np.round(height),np.round(rotation))
            
            box= cv2.boxPoints(rect)
            box = np.int64(box)
            
            M= cv2.moments(c)
            center= ((int((M["m10"])/(M["m00"]))),((int((M["m01"])/(M["m00"])))))
            
            cv2.drawContours(frame,[box],0,(0,255,0),2)
            cv2.circle(frame,center,5,(0,255,255),-1)
            cv2.putText(frame,s,(20,70),cv2.FONT_HERSHEY_COMPLEX_SMALL,3,(255,255,255),2)
            
        pts.appendleft(center)
        
        for i in range(len(pts)):
            
            if pts[i-1] is None or pts[i] is None: 
                continue
            else:
                cv2.line(frame,pts[i-1],pts[i],(0,255,0),3)
    
    cv2.imshow("Original",frame)       
    if cv2.waitKey(1) & 0xFF == ord("q"): 
        break
            
cap.release()
cv2.destroyAllWindows()
    



























