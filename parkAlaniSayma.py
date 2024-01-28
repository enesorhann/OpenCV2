import numpy as np 
import cv2 
import pickle

width= 13
height=27

def checkParkSpace(image):
    spaceCounter= 0
    for pos in posList:
        x,y= pos
        image_cropped= image[y: y+height,x: x+width]
        count= cv2.countNonZero(image_cropped)
        print("Count: ",count)
        #220-85
 
        if count <110:
            spaceCounter+=1
            color = (0,255,0)
        else:
            color= (0,0,255)
            
            cv2.rectangle(frame,pos,(pos[0]+height,pos[1]+width),color,2)
            cv2.putText(frame,str(count),(x,y+height-2),cv2.FONT_HERSHEY_PLAIN,1,(color),1)
        
    cv2.putText(frame,f"Free: {spaceCounter}/{len(posList)}",(15,24),cv2.FONT_HERSHEY_PLAIN,2,(0,255,255),4)



cap= cv2.VideoCapture("C:\\Users\\Coder\\MyAiLab\\OpenCv\\video.mp4")

with open("ParkPosition","rb") as f:
        posList= pickle.load(f)
        
while True:
    success, frame = cap.read()
    
    #Detaylari azaltmak icin gaussian blur uygulayalim
    imgGRAY= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gb = cv2.GaussianBlur(imgGRAY,ksize=(3,3),sigmaX=7)
    thresh= cv2.adaptiveThreshold(gb,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
    #arabalarin ustu siyah oralari bos yer sanabiilir bu yuzden biraz daha bulaniklastiralim.
    mb= cv2.medianBlur(thresh,5)
    #bu haliyle de arabalar inceldi gibi o yuzden 1 kat kalinlastiralim
    imgDilate= cv2.dilate(mb,np.ones((3,3)),iterations=1)
    #Artik daha iyi ayirt ediliyor.
    checkParkSpace(imgDilate)
    
    cv2.imshow("Park Sayma: ",frame)
    #cv2.imshow("Orijinal: ",frame)
    #cv2.imshow("Gray: ",imgGRAY)
    #cv2.imshow("Gauss Bulanikligi: ",gb)
    #cv2.imshow("Threshold ",thresh)
    #cv2.imshow("Median Blur ",mb)
    #cv2.imshow("Genisletme ",imgDilate)
    cv2.waitKey(50)