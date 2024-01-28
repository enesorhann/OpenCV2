import cv2
import mediapipe as mp
import time

mpPose= mp.solutions.pose 
pose= mpPose.Pose()
mpDraw= mp.solutions.drawing_utils

cap= cv2.VideoCapture("C:\\Users\\Coder\\MyAiLab\\OpenCv\\video4.mp4")

ptime=0
while True:
    success,frame= cap.read()
    frameRGB= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results= pose.process(frameRGB)
    
    if results.pose_landmarks:
            mpDraw.draw_landmarks(frame,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
            
            for id, lm in enumerate(results.pose_landmarks.landmark):
                h,w,c= frame.shape
                cx,cy= int(lm.x*w),int(lm.y*h)
                cv2.circle(frame,(cx,cy),2,(255,0,0),cv2.FILLED)
                
    ctime= time.time()
    fps= 1/(ctime-ptime)
    ptime=ctime
    cv2.putText(frame,"FPS: "+str(int(fps)),(10,55),cv2.FONT_HERSHEY_PLAIN,5,(0,255,0),8)
    cv2.imshow("Pose: ",frame)
    cv2.waitKey(50)