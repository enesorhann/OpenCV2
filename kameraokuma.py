import cv2

cap = cv2.VideoCapture(0)

#Yuksekligini ve genisligini ogrenelim.
width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width)
print(height)

#Videodaki frameleri depolayip video haline getirir.
writer = cv2.VideoWriter("CODER_CAM.mp4",cv2.VideoWriter.fourcc(*"DIVX"),20,(width,height))

while True:
    ret,frame = cap.read()
    writer.write(frame)
    cv2.imshow("CODER_CAM",frame)
    if cv2.waitKey(150) & 0xFF == ord("q"):
        break
    
cap.release()
writer.release()
cv2.destroyAllWindows()