import cv2
import mediapipe as mp 

mpfaceDetection = mp.solutions.face_detection
faceDetection= mpfaceDetection.FaceDetection()
mpDraw= mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results= faceDetection.process(frameRGB)
    
    if results.detections:
        for id, detection in enumerate(results.detections):
            bboxC = detection.location_data.relative_bounding_box
            print(bboxC) #xmin,ymin,width,height alanlarini yazdirir.
            
            h,w,_ = frame.shape
            bbox= int(bboxC.xmin*w),int(bboxC.ymin*h),int(bboxC.width*w),int(bboxC.height*h)
            #print(bbox)
            cv2.rectangle(frame,bbox,(0,255,255),2)
            #print((cv2.rectangle(frame,bbox,(0,255,255),2)).shape)
    cv2.imshow("Face Detection",frame)
    cv2.waitKey(100)