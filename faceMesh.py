import cv2
import mediapipe as mp 
import time

mpFaceMesh= mp.solutions.face_mesh
faceMesh= mpFaceMesh.FaceMesh()
mpDraw= mp.solutions.drawing_utils
drawSpec = mpDraw.DrawingSpec(thickness=1,circle_radius=1)

cap = cv2.VideoCapture(0)

ptime=0
while True:
    success, frame= cap.read()
    frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results= faceMesh.process(frameRGB)
    #print(results.multi_face_landmarks)
    
    if results.multi_face_landmarks:
        for flms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(frame,flms,mpFaceMesh.FACEMESH_TESSELATION,drawSpec,drawSpec,drawSpec)
            
            for id,lm in enumerate(flms.landmark):
                h,w,_ = frame.shape
                cx,cy= int(lm.x*w),int(lm.y*h)
                #print(id,cx,cy)
        
    ctime= time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    cv2.putText(frame,str(int(fps)),(10,65),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),5)
        
    cv2.imshow("Face Mesh",frame)
    cv2.waitKey(100)