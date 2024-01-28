import cv2
import time
import mediapipe as mp 

cap = cv2.VideoCapture(0)

mpHand= mp.solutions.hands
hands=mpHand.Hands()
mpDraw= mp.solutions.drawing_utils

ctime=0
ptime=0
while True:
    ret, frame = cap.read()
    imgRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    
    results= hands.process(imgRGB)
    print(results.multi_hand_landmarks) #Kamera el gorurse hemen koordinatlari yazdirir
    
    if results.multi_hand_landmarks: #None degilse
        for hlms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame,hlms,mpHand.HAND_CONNECTIONS)
            
            for id,lm in enumerate(hlms.landmark):
                h,w,c = frame.shape
                cx,cy= int(lm.x*w),int(lm.y*h)
                
                if id==4:
                    cv2.circle(frame,(cx,cy),9,(200,200,200),cv2.FILLED)
            
    ctime= time.time()
    fps= 1/(ctime-ptime)
    ptime=ctime
    
    cv2.imshow("El Yakalama",frame)
    cv2.waitKey(1)
    