import cv2
import pickle

width= 13
height=27

try:
    with open("ParkPosition","rb") as f:
        posList= pickle.load(f)
except:
    posList= []

def mouseClickis(events,x,y,flags,params):
    
    if events==cv2.EVENT_LBUTTONDOWN:
        posList.append((x,y))
        
    if events==cv2.EVENT_RBUTTONDOWN:
        for index,pos in enumerate(posList):
            x1,y1= pos
            if x1<x<x1+width and y1<y<y+height:
                posList.pop(index)
    
    with open("ParkPosition","wb") as f:
        pickle.dump(posList,f)
        
while True:    
    img= cv2.imread("C:\\Users\\Coder\\MyAiLab\\OpenCv\\first_frame.png")
    
    for pos in posList:
        cv2.rectangle(img,pos,(pos[0]+height,pos[1]+width),(0,255,0),2)
    
    cv2.imshow("Park Alanlari",img)
    cv2.setMouseCallback("Park Alanlari",mouseClickis)
    cv2.waitKey(1)