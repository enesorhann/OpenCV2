import os 
import cv2

files = os.listdir("C:\\Users\\Coder\\MyAiLab\\OpenCv")
#print(files)
img_path_list = []

for f in files:
    if f.startswith("img") & f.endswith(".jpg"):
        img_path_list.append(f)
print(img_path_list)
    
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

for img_path in img_path_list:
    print(img_path)
    image = cv2.imread(img_path)
    
    (rects,weights) = hog.detectMultiScale(image,padding=(0,0),scale=(1.05))
    
    for (x,y,w,h) in rects:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,255),7)
    cv2.imshow("Yaya",image)
    if cv2.waitKey(0) & 0XFF == ord("q"): continue
    
cv2.destroyAllWindows()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    