import matplotlib.pyplot as plt
import cv2
import numpy as np

chocolates= cv2.imread("C:\\Users\\Coder\\MyAiLab\\OpenCv\\chocolates.jpg")
chocolates= cv2.cvtColor(chocolates,cv2.COLOR_BGR2RGB)
plt.figure(),plt.axis("off"),plt.imshow(chocolates),plt.show()

nestle = cv2.imread("C:\\Users\\Coder\\MyAiLab\\OpenCv\\nestle.jpg")
nestle= cv2.cvtColor(nestle,cv2.COLOR_BGR2RGB)
plt.figure(),plt.axis("off"),plt.imshow(nestle),plt.show()

orb= cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(nestle,None)
kp2, des2 = orb.detectAndCompute(chocolates,None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING)
matches = bf.match(des1,des2)
matches = sorted(matches,key=lambda x: x.distance)
plt.figure()
orb_match= cv2.drawMatches(nestle,kp1,chocolates,kp2,matches[:20],None,flags=2)
plt.title("ORB Egrileri"),plt.axis("off"),plt.imshow(orb_match,cmap="gray"),plt.show()


sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(nestle,None)
kp2, des2 = sift.detectAndCompute(chocolates,None)
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2,k=2)

guzel_eslestirme= []

for match1,match2 in matches:
    if match1.distance < 0.75*match2.distance:
        guzel_eslestirme.append([match1])
        
plt.figure()
sift_match= cv2.drawMatchesKnn(nestle,kp1,chocolates,kp2,guzel_eslestirme,None,flags=2)
plt.title("SIFT Egrileri"),plt.axis("off"),plt.imshow(sift_match,cmap="gray"),plt.show()






















