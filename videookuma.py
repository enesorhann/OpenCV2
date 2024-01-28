import cv2
import time

video_name = "MOT17-04-DPM.mp4"

cap = cv2.VideoCapture(video_name)

if cap.isOpened == False:
    print("Error!")

width = cap.get(3)
height = cap.get(4)

print("Yukseklik: ",height)
print("Genislik: ",width)

while True:
    ret,frame = cap.read()
    #frame= cv2.resize(frame,(width,height))
    
    if ret == True:
        
        time.sleep(0.01)
        cv2.imshow("Video",frame)
        
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break
    else:
        break
    
cap.release()
cv2.destroyAllWindows()
    
    