import cv2
import math 
import mediapipe as mp 
import numpy as np

def findAngle(frame,p1,p2,p3,lmList,draw=True):
    x1,y1 = lmList[p1][1:]
    x2,y2 = lmList[p2][1:]
    x3,y3 = lmList[p3][1:]
    
    angle= math.degrees( math.atan2(x3-x2,y3-y2) - math.atan2(x1-x2,y1-y2) )
    
    if angle<0:
        angle += 360
    
    if draw:

        cv2.line(frame,(x1,y1),(x2,y2),(0,255,50),3)
        cv2.line(frame,(x3,y3),(x2,y2),(0,255,50),3)
        
        cv2.circle(frame,(x1,y1),10,(0,255,0),cv2.FILLED)
        cv2.circle(frame,(x1,y1),10,(0,255,0),cv2.FILLED)
        cv2.circle(frame,(x1,y1),10,(0,255,0),cv2.FILLED)
        
        cv2.circle(frame,(x1,y1),15,(0,255,0))
        cv2.circle(frame,(x1,y1),15,(0,255,0))
        cv2.circle(frame,(x1,y1),15,(0,255,0))
        
        cv2.putText(frame,str(int(angle)),(x2-44,y2+44),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
        
    return angle
    

mpPose= mp.solutions.pose
pose= mpPose.Pose()
mpDraw= mp.solutions.drawing_utils

cap = cv2.VideoCapture("C:\\Users\\Coder\\MyAiLab\\OpenCv\\video1.mp4")

dir=0
count=0
while True:
    success, frame= cap.read()
    frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results= pose.process(frameRGB)
    
    lmList=[]
    if results.pose_landmarks:
        mpDraw.draw_landmarks(frame,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h,w,_= frame.shape
            cx,cy= int(lm.x*w),int(lm.y*h)
            cv2.circle(frame,(cx,cy),1,(255,0,0),cv2.FILLED)
            lmList.append([id,cx,cy])
            
        if len(lmList) != 0:
        
            angle= findAngle(frame,11,13,15,lmList)
            per= np.interp(angle,(75,178),(0,100))
            
            if per==0:
                if dir==1:
                    count += 0.5
                    dir=0
                
            if per==100:
                if dir==0:
                    count += 0.5
                    dir=1
                    
            cv2.putText(frame,str(int(count)),(44,165),cv2.FONT_HERSHEY_PLAIN,10,(0,255,0),10)
                    
    cv2.imshow("AcidanHareketSayma",frame)
    cv2.waitKey(50)
            
    