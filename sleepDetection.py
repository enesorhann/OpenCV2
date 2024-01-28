import cv2 
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot

cap= cv2.VideoCapture("C:\\Users\\Coder\\MyAiLab\\OpenCv\\video1.mp4")
detector= FaceMeshDetector()
plotY= LivePlot(540,360,(10,60))

eyesId= [22, 23, 24, 26, 110, 157, 158, 159, 160, 161, 130, 243]
counter=0
blinkCounter=0
ratioList=[]
color= (0,0,255)


while True:
    success,frame= cap.read()
    frame, faces= detector.findFaceMesh(frame,draw=False)
    
    if faces:
        face= faces[0]
        for id in eyesId:
            #Gozu okudugumuzu belli eden mesh atalim
            cv2.circle(frame,face[id],5,color,cv2.FILLED)
    #kameranin solu bizim sag gozumuzun sag,sol,ust,alt kenarlarinin id'si        
    leftUp= face[159]
    leftDown= face[23]
    leftLeft= face[130]
    leftRight= face[243]
    
    lengtVer,_ = detector.findDistance(leftUp,leftDown)
    lengtHor,_ = detector.findDistance(leftLeft,leftRight)
    
    cv2.line(frame,leftUp,leftDown,(0,255,255),3)
    cv2.line(frame,leftLeft,leftRight,(0,255,255),3)

    ratio= int((lengtVer/lengtHor)*100)
    ratioList.append(ratio)
    if len(ratioList)>3:
        ratioList.pop(0)
    
    ratioAvg=sum(ratioList)/len(ratioList)
    print(ratioAvg)
    
    if ratioAvg < 35 and counter == 0:
        blinkCounter+=1
        counter=1
        color= (0,255,0)
    if counter != 0:
        counter+=1
        if counter > 10:
            counter=0
            color=(0,0,255)
    
    cvzone.putTextRect(frame,f"Blink Count: {blinkCounter}",(50,100),colorR=color)
    imgPlot= plotY.update(ratioAvg,color)
    img= cv2.resize(frame,(540,360))
    imgStack= cvzone.stackImages([frame,imgPlot],2,1)
    
    cv2.imshow("Original",imgStack)
    cv2.waitKey(25)
    