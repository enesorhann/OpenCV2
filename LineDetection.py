import cv2
import numpy as np
  
cap = cv2.VideoCapture("C:\\Users\\Coder\\MyAiLab\\OpenCv\\video1.mp4")

def drawLines(image,lines):
    img= np.copy(image)
    blankImage= np.zeros((img.shape[0],img.shape[1],3),dtype=np.uint8)

    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(img,(x1,y1),(x2,y2),(0,255,0),thickness=10)
        sonHali= cv2.addWeighted(img,0.8,blankImage,1,0.0)
            
    return sonHali

def RegionVertices(image,vertices):
    mask= np.zeros_like(image)
    match_mask_color = 255
    
    cv2.fillPoly(mask,vertices,match_mask_color)
    maskedImage= cv2.bitwise_and(image,mask)
    
    return maskedImage

def process(image):
    height, width= image.shape[0],image.shape[1]
    regionofInterestVertices= [(0,height),(width/2,height/2),(width,height)]
    
    grayImage= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cannyImage= cv2.Canny(grayImage,250,120)
    croppedImage= RegionVertices(cannyImage,np.array([regionofInterestVertices],np.int32))
    
    lines= cv2.HoughLinesP(croppedImage,rho = 2, theta = np.pi/180, threshold = 200, lines = np.array([]),minLineLength = 150, maxLineGap = 4)
    withLines= drawLines(image,lines)
    
    return withLines
    

while True:
    success, frame= cap.read()
    frame= process(frame)
    cv2.imshow("Orijinal",frame)
    cv2.waitKey(33)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    