import cv2 
import matplotlib.pyplot as plt
import numpy as np

paraciklarim = cv2.imread("C:\\Users\\Coder\\MyAiLab\\OpenCv\\coins.jpg")
plt.figure(),plt.axis("off"),plt.imshow(paraciklarim),plt.show()

blurluParaciklarim = cv2.medianBlur(paraciklarim,13)
plt.figure(),plt.axis("off"),plt.imshow(blurluParaciklarim),plt.show()

griParaciklarim = cv2.cvtColor(blurluParaciklarim,cv2.COLOR_BGR2GRAY)
plt.figure(),plt.axis("off"),plt.imshow(griParaciklarim,cmap="gray"),plt.show()

ret, threshPara = cv2.threshold(griParaciklarim,75,255,cv2.THRESH_BINARY)
plt.figure(),plt.axis("off"),plt.imshow(threshPara,cmap="gray"),plt.show()

contours, hierarchy = cv2.findContours(threshPara.copy(),cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
for i in range(len(contours)):
    
    if hierarchy[0][i][3]:
        cv2.drawContours(paraciklarim,contours,i,(0,255,0),10)

plt.figure(),plt.axis("off"),plt.imshow(paraciklarim,cmap="gray"),plt.show()


paraciklarim = cv2.imread("C:\\Users\\Coder\\MyAiLab\\OpenCv\\coins.jpg")
plt.figure(),plt.axis("off"),plt.imshow(paraciklarim),plt.show()
blurluParaciklarim = cv2.medianBlur(paraciklarim,13)
plt.figure(),plt.axis("off"),plt.imshow(blurluParaciklarim),plt.show()
griParaciklarim = cv2.cvtColor(blurluParaciklarim,cv2.COLOR_BGR2GRAY)
plt.figure(),plt.axis("off"),plt.imshow(griParaciklarim,cmap="gray"),plt.show()
ret, threshPara = cv2.threshold(griParaciklarim,75,255,cv2.THRESH_BINARY)
plt.figure(),plt.axis("off"),plt.imshow(threshPara,cmap="gray"),plt.show()

kernel = np.ones((3,3),np.uint8)
opening= cv2.morphologyEx(threshPara,cv2.MORPH_OPEN,kernel,3)
plt.figure(),plt.axis("off"),plt.imshow(opening,cmap="gray"),plt.show()

distance = cv2.distanceTransform(opening,cv2.DIST_L2,3)
plt.figure(),plt.axis("off"),plt.imshow(distance,cmap="gray"),plt.show()

ret, sureForeground = cv2.threshold(distance,0.4*np.max(distance),255,0)
plt.figure(),plt.axis("off"),plt.imshow(sureForeground,cmap="gray"),plt.show()

sureBackground = cv2.dilate(opening,kernel,iterations=1)
sureForeground= np.uint8(sureForeground)
unknown = cv2.subtract(sureBackground,sureForeground)
plt.figure(),plt.axis("off"),plt.imshow(unknown,cmap="gray"),plt.show()

ret, marker = cv2.connectedComponents(sureForeground)
marker += 1
marker[unknown == 255] = 0
plt.figure(),plt.axis("off"),plt.imshow(marker,cmap="gray"),plt.show()

marker = cv2.watershed(paraciklarim,marker)
plt.figure(),plt.axis("off"),plt.imshow(marker,cmap="gray"),plt.show()

for i in range(len(contours)):
    
    if hierarchy[0][i][3]:
        cv2.drawContours(paraciklarim,contours,i,(0,255,0),10)

plt.figure(),plt.axis("off"),plt.imshow(paraciklarim),plt.show()












