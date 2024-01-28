import cv2
import mediapipe as mp

cap= cv2.VideoCapture(0)

mpHand= mp.solutions.hands
hands = mpHand.Hands()
mpDraw= mp.solutions.drawing_utils

parmakID=[4,8,12,16,20]
while True:
    ret,frame= cap.read()
    imgRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results= hands.process(imgRGB)
    
    lmList=[]
    if results.multi_hand_landmarks:
        for hlms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame,hlms,mpHand.HAND_CONNECTIONS)
            
            for id,lm in enumerate(hlms.landmark):
                h,w,c = frame.shape
                cx,cy= int(lm.x*w),int(lm.y*h)
                lmList.append([id,cx,cy])
                
                
    if len(lmList) !=0:
        fingers=[]
        
        if lmList[parmakID[0]][1] < lmList[parmakID[0] -1 ][1]:
            fingers.append(1)
        else:
            fingers.append(0)
            
        for id in range(1,5):
            if lmList[parmakID[id]][2] < lmList[parmakID[id] -1 ][2]:
                fingers.append(1)
            else:
                fingers.append(0)
                
        totalFinger = fingers.count(1)
        
        cv2.putText(frame,"Total: "+str(totalFinger),(30,125),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),5)
        
    cv2.imshow("El Sayma",frame)
    if(cv2.waitKey(1)==ord("q")):
        cap.release()
        cv2.destroyAllWindows()